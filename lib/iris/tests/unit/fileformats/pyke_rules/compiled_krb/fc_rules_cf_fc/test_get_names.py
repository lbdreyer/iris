# (C) British Crown Copyright 2019, Met Office
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
Test function :func:`iris.fileformats._pyke_rules.compiled_krb.\
fc_rules_cf_fc.get_names`.

"""

from __future__ import (absolute_import, division, print_function)
from six.moves import (filter, input, map, range, zip)  # noqa

# import iris tests first so that some things can be initialised before
# importing anything else
import iris.tests as tests

import numpy as np

from iris.cube import Cube
from iris.fileformats._pyke_rules.compiled_krb.fc_rules_cf_fc import get_names
from iris.tests import mock


class TestGetNames(tests.IrisTest):
    @staticmethod
    def _make_cf_var(cf_name=None, standard_name=None, long_name=None):
        cf_var = mock.Mock(
            cf_name=cf_name,
            standard_name=standard_name,
            long_name=long_name,
            units='m',
            dtype=np.float64,
            cell_methods=None,
            cf_group=mock.Mock(global_attributes={}))
        return cf_var

    def repeat_test(self, inputs, expected):
        # Inputs - what would be written in the file
        standard_name, long_name, cf_name, coord_name = inputs
        # Expected - The expected results
        exp_standard_name, exp_long_name, exp_cf_name, exp_attributes = expected

        cf_var = self._make_cf_var(standard_name, long_name, cf_name)
        attributes = {}

        res_standard_name, res_long_name, res_cf_name = get_names(
            cf_var, coord_name, attributes)

        self.assertEqual(res_standard_name, exp_standard_name)
        self.assertEqual(res_long_name, exp_long_name)
        self.assertEqual(res_cf_name, exp_cf_name)
        self.assertEqual(attributes, exp_attributes)

    def test_0(self):
        inputs = (None, None, 'grid_latitude', None)
        expected = ('grid_latitude', None, 'grid_latitude', {})
        self.repeat_test(inputs, expected)
        
    def test_1(self):
        inputs = (None, None, 'grid_latitude', 'latitude')
        expected = ('latitude', None, 'grid_latitude', {})
        self.repeat_test(inputs, expected)

    def test_2(self):
        inputs = (None, None, 'lat_var_name', None)
        expected = (None, None, 'lat_var_name', {})
        self.repeat_test(inputs, expected)

    def test_3(self):
        inputs = (None, None, 'lat_var_name', 'latitude')
        expected = ('latitude', None, 'lat_var_name', {})
        self.repeat_test(inputs, expected)

    def test_4(self):
        inputs = (None, 'lat_long_name', 'grid_latitude', None)
        expected = ('grid_latitude', 'lat_long_name', 'grid_latitude', {})
        self.repeat_test(inputs, expected)
        
    def test_5(self):
        inputs = (None, 'lat_long_name', 'grid_latitude', 'latitude')
        expected = ('latitude', 'lat_long_name', 'grid_latitude', {})
        self.repeat_test(inputs, expected)

    def test_6(self):
        inputs = (None, 'lat_long_name', 'lat_var_name', None)
        expected = (None, 'lat_long_name', 'lat_var_name', {})
        self.repeat_test(inputs, expected)

    def test_7(self):
        inputs = (None, 'lat_long_name', 'lat_var_name', 'latitude')
        expected = ('latitude', 'lat_long_name', 'lat_var_name', {})
        self.repeat_test(inputs, expected)

    def test_8(self):
        inputs = ('projection_y_coordinate', None, 'grid_latitude', None)
        expected = ('projection_y_coordinate', None, 'grid_latitude', {})
        self.repeat_test(inputs, expected)

    def test_9(self):
        inputs = ('projection_y_coordinate', None, 'grid_latitude', 'latitude')
        expected = ('projection_y_coordinate', None, 'grid_latitude', {})
        self.repeat_test(inputs, expected)

    def test_10(self):
        inputs = ('projection_y_coordinate', None, 'lat_var_name', None)
        expected = ('projection_y_coordinate', None, 'lat_var_name', {})
        self.repeat_test(inputs, expected)

    def test_11(self):
        inputs = ('projection_y_coordinate', None, 'lat_var_name', 'latitude')
        expected = ('projection_y_coordinate', None, 'lat_var_name', {})
        self.repeat_test(inputs, expected)

    def test_12(self):
        inputs = ('projection_y_coordinate', 'lat_long_name', 'grid_latitude', None)
        expected = ('projection_y_coordinate', 'lat_long_name', 'grid_latitude', {})
        self.repeat_test(inputs, expected)

    def test_13(self):
        inputs = ('projection_y_coordinate', 'lat_long_name', 'grid_latitude', 'latitude')
        expected = ('projection_y_coordinate', 'lat_long_name', 'grid_latitude', {})
        self.repeat_test(inputs, expected)

    def test_14(self):
        inputs = ('projection_y_coordinate', 'lat_long_name', 'lat_var_name', None)
        expected = ('projection_y_coordinate', 'lat_long_name', 'lat_var_name', {})
        self.repeat_test(inputs, expected)

    def test_15(self):
        inputs = ('projection_y_coordinate', 'lat_long_name', 'lat_var_name', 'latitude')
        expected = ('projection_y_coordinate', 'lat_long_name', 'lat_var_name', {})
        self.repeat_test(inputs, expected)

    def test_16(self):
        inputs = ('latitude_coord', None, 'grid_latitude', None)
        expected = ('grid_latitude', 'latitude_coord', 'grid_latitude', {'invalid_standard_name': 'latitude_coord'})
        self.repeat_test(inputs, expected)

    def test_17(self):
        inputs = ('latitude_coord', None, 'grid_latitude', 'latitude')
        expected = ('latitude', None, 'grid_latitude', {})
        self.repeat_test(inputs, expected)

    def test_18(self):
        inputs = ('latitude_coord', None, 'lat_var_name', None)
        expected = (None, 'latitude_coord', 'lat_var_name', {'invalid_standard_name': 'latitude_coord'})
        self.repeat_test(inputs, expected)

    def test_19(self):
        inputs = ('latitude_coord', None, 'lat_var_name', 'latitude')
        expected = ('latitude', None, 'lat_var_name', {})
        self.repeat_test(inputs, expected)

    def test_20(self):
        inputs = ('latitude_coord', 'lat_long_name', 'grid_latitude', None)
        expected = ('grid_latitude', 'lat_long_name', 'grid_latitude', {'invalid_standard_name': 'latitude_coord'})
        self.repeat_test(inputs, expected)

    def test_21(self):
        inputs = ('latitude_coord', 'lat_long_name', 'grid_latitude', 'latitude')
        expected = ('latitude', 'lat_long_name', 'grid_latitude', {})
        self.repeat_test(inputs, expected)

    def test_22(self):
        inputs = ('latitude_coord', 'lat_long_name', 'lat_var_name', None)
        expected = (None, 'lat_long_name', 'lat_var_name', {'invalid_standard_name': 'latitude_coord'})
        self.repeat_test(inputs, expected)

    def test_23(self):
        inputs = ('latitude_coord', 'lat_long_name', 'lat_var_name', 'latitude')
        expected = ('latitude', 'lat_long_name', 'lat_var_name', {})
        self.repeat_test(inputs, expected)


if __name__ == "__main__":
    tests.main()
