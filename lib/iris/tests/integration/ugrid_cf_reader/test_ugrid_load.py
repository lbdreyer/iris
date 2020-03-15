# Copyright Iris contributors
#
# This file is part of Iris and is released under the LGPL license.
# See COPYING and COPYING.LESSER in the root of the repository for full
# licensing details.
"""
Integration tests for the
:mod:`iris.fileformats._ugrid_cf_reader.UGridCFReader` class.

"""

# Import iris.tests first so that some things can be initialised before
# importing anything else.
import iris.tests as tests


from iris.cube import CubeList
from iris import Constraint
from iris.fileformats.netcdf import load_cubes


class TestUgrid(tests.IrisTest):
    def test_basic_load(self):
        fp = "/project/avd/ng-vat/data/sam_adams_tiny_test_files/lfric_diag.nc"

        # cube = iris.load_cube(fp, "theta")
        # Note: cannot use iris.load, as merge does not yet preserve
        # the cube 'ugrid' properties.

        loaded_cubes = CubeList(load_cubes(fp))

        # Here's a thing that at least works.  Just print some details.
        # TODO: write some actual tests later...
        print("")
        print("All loaded cubes:")
        print(loaded_cubes)

        def select_cube_function(cube):
            return cube.var_name == "theta"

        (cube,) = loaded_cubes.extract(
            Constraint(cube_func=lambda cube: cube.var_name == "theta")
        )

        print("")
        print("Theta cube:")
        print(cube)
        print(cube.ugrid)

        (cube,) = loaded_cubes.extract(
            Constraint(cube_func=lambda cube: cube.var_name == "rho")
        )

        print("")
        print("Rho cube (which is on a different grid):")
        print(cube)
        print(cube.ugrid)


if __name__ == "__main__":
    tests.main()
