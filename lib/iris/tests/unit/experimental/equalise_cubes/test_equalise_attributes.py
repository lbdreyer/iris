# (C) British Crown Copyright 2013 - 2014, Met Office
#
# This file is part of Iris.
#
# Iris is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Iris is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Iris.  If not, see <http://www.gnu.org/licenses/>.
"""
Unit tests for the :func:`iris.experimental.equalise_cubes.equalise_attributes`
function.

"""

from __future__ import (absolute_import, division, print_function)

# import iris tests first so that some things can be initialised
# before importing anything else.
import iris.tests as tests

import numpy as np

from iris.cube import Cube
from iris.experimental.equalise_cubes import equalise_attributes
import iris.tests.stock


class TestEqualiseAttributes(tests.IrisTest):
    def setUp(self):
        empty = Cube([])

        self.cube_no_attrs = empty.copy()

        self.cube_a1 = empty.copy()
        self.cube_a1.attributes.update({'a': 1})

        self.cube_a2 = empty.copy()
        self.cube_a2.attributes.update({'a': 2})

        self.cube_a1b5 = empty.copy()
        self.cube_a1b5.attributes.update({'a': 1, 'b': 5})

        self.cube_a1b6 = empty.copy()
        self.cube_a1b6.attributes.update({'a': 1, 'b': 6})

        self.cube_a2b6 = empty.copy()
        self.cube_a2b6.attributes.update({'a': 2, 'b': 6})

        self.cube_b5 = empty.copy()
        self.cube_b5.attributes.update({'b': 5})

        # Array attribute values
        v1 = np.array([11, 12, 13])
        v2 = np.array([11, 9999, 13])
        self.v1 = v1

        self.cube_a1b5v1 = empty.copy()
        self.cube_a1b5v1.attributes.update({'a': 1, 'b': 5, 'v': v1})

        self.cube_a1b6v1 = empty.copy()
        self.cube_a1b6v1.attributes.update({'a': 1, 'b': 6, 'v': v1})

        self.cube_a1b6v2 = empty.copy()
        self.cube_a1b6v2.attributes.update({'a': 1, 'b': 6, 'v': v2})

    def _test(self, cubes, expect_attributes):
        """Test."""
        working_cubes = [cube.copy() for cube in cubes]
        original_working_list = [cube for cube in working_cubes]
        # Exercise basic operation
        equalise_attributes(working_cubes)
        # Check they are the same cubes
        self.assertEqual(working_cubes, original_working_list)
        # Check resulting attributes all match the expected set
        for cube in working_cubes:
            self.assertEqual(cube.attributes, expect_attributes)
        # Check everything else remains the same
        for new_cube, old_cube in zip(working_cubes, cubes):
            cube_before_noatts = old_cube.copy()
            cube_before_noatts.attributes.clear()
            cube_after_noatts = new_cube.copy()
            cube_after_noatts.attributes.clear()
            self.assertEqual(cube_after_noatts, cube_before_noatts)

    def test_no_attrs(self):
        cubes = [self.cube_no_attrs]
        self._test(cubes, {})

    def test_single(self):
        cubes = [self.cube_a1]
        self._test(cubes, {'a': 1})

    def test_identical(self):
        cubes = [self.cube_a1, self.cube_a1.copy()]
        self._test(cubes, {'a': 1})

    def test_one_extra(self):
        cubes = [self.cube_a1, self.cube_a1b5.copy()]
        self._test(cubes, {'a': 1})

    def test_one_different(self):
        cubes = [self.cube_a1b5, self.cube_a1b6]
        self._test(cubes, {'a': 1})

    def test_common_no_diffs(self):
        cubes = [self.cube_a1b5, self.cube_a1b5.copy()]
        self._test(cubes, {'a': 1, 'b': 5})

    def test_common_all_diffs(self):
        cubes = [self.cube_a1b5, self.cube_a2b6]
        self._test(cubes, {})

    def test_none_common(self):
        cubes = [self.cube_a1, self.cube_b5]
        self._test(cubes, {})

    def test_array_extra(self):
        cubes = [self.cube_a1b6, self.cube_a1b6v1]
        self._test(cubes, {'a': 1, 'b': 6})

    def test_array_different(self):
        cubes = [self.cube_a1b5v1, self.cube_a1b6v2]
        self._test(cubes, {'a': 1})

    def test_array_same(self):
        cubes = [self.cube_a1b5v1, self.cube_a1b6v1]
        self._test(cubes, {'a': 1, 'v': self.v1})

    @tests.skip_data
    def test_complex_nonecommon(self):
        # Example with cell methods and factories, but no common attributes.
        cubes = [iris.tests.stock.global_pp(),
                 iris.tests.stock.hybrid_height()]
        self._test(cubes, {})

    @tests.skip_data
    def test_complex_somecommon(self):
        # Example with cell methods and factories, plus some common attributes.
        cubes = [iris.tests.stock.global_pp(), iris.tests.stock.simple_pp()]
        self._test(
            cubes,
            {'STASH': iris.fileformats.pp.STASH(model=1, section=16, item=203),
             'source': 'Data from Met Office Unified Model'})


if __name__ == "__main__":
    tests.main()
