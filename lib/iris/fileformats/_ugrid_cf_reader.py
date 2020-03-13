# Copyright Iris contributors
#
# This file is part of Iris and is released under the LGPL license.
# See COPYING and COPYING.LESSER in the root of the repository for full
# licensing details.
"""
Adds a UGRID extension layer to netCDF file loading.

"""
import os

import netCDF4

from gridded.pyugrid.ugrid import UGrid
from gridded.pyugrid.read_netcdf import (
    find_mesh_names,
    load_grid_from_nc_dataset,
)
from iris.fileformats.cf import CFReader


_UGRID_ELEMENT_TYPE_NAMES = ("node", "edge", "face", "volume")

_UGRID_LINK_PROPERTIES = [
    "{}_coordinates".format(elem) for elem in _UGRID_ELEMENT_TYPE_NAMES
]
_UGRID_LINK_PROPERTIES += [
    "{}_{}_connectivity".format(e1, e2)
    for e1 in _UGRID_ELEMENT_TYPE_NAMES
    for e2 in _UGRID_ELEMENT_TYPE_NAMES
]

# print('')
# print('Ugrid link properties ...')
# print('\n'.join(_UGRID_LINK_PROPERTIES))


class UGridCFReader:
    def __init__(self, filename, *args, **kwargs):
        self.filename = os.path.expanduser(filename)
        dataset = netCDF4.Dataset(self.filename, mode="r")
        self.dataset = dataset
        meshes = {}
        for meshname in find_mesh_names(self.dataset):
            mesh = UGrid()
            load_grid_from_nc_dataset(dataset, mesh, mesh_name=meshname)
            meshes[meshname] = mesh
        self.meshes = meshes
        # Generate list of excluded variable names.
        exclude_vars = list(meshes.keys())
        for mesh in meshes.values():
            mesh_var = dataset.variables[mesh.mesh_name]
            for attr in mesh_var.ncattrs():
                if attr in _UGRID_LINK_PROPERTIES:
                    exclude_vars.extend(mesh_var.getncattr(attr).split())
        print("")
        print("File {}".format(filename, meshes))
        print("File meshes={}".format(meshes))
        print("")
        print("File exclude vars={}".format(exclude_vars))
        print("")
        print(
            "File remaining vars={}".format(
                [x for x in dataset.variables.keys() if x not in exclude_vars]
            )
        )
        kwargs["exclude_var_names"] = exclude_vars
        self.cfreader = CFReader(self.dataset, *args, **kwargs)

    def complete_ugrid_cube(self, cube):
        pass

    def __del__(self):
        # Explicitly close dataset to prevent file remaining open.
        self.dataset.close()
