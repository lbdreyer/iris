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

import iris


class TestUgrid(tests.IrisTest):
    def test_basic_load(self):
        fp = "/project/avd/ng-vat/data/sam_adams_tiny_test_files/lfric_diag.nc"
        cubes = iris.load(fp)
        print(cubes)
        cube = iris.load_cube(fp, "theta")
        print(cube)


if __name__ == "__main__":
    tests.main()
