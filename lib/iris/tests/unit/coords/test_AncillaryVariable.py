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
"""Unit tests for the :class:`iris.coords.AncillaryVariable` class."""

# Import iris.tests first so that some things can be initialised before
# importing anything else.
import iris.tests as tests

import numpy as np

from iris.coords import AncillaryVariable


class Test(tests.IrisTest):
    def setUp(self):
        self.values = np.array((2, 3, 5, 8))
        self.measure = AncillaryVariable(
            self.values, units='1',
            standard_name='status_flag',
            long_name='location of bad data',
            var_name='status_flag',
            attributes={'notes': 'Additional data mask'})

    def test_data_values(self):
        self.assertEqual(self.measure.data, self.values)