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
            standard_name=standard_nmae,
            long_name=long_name,
            units='m',
            dtype=np.float64,
            cell_methods=None,
            cf_group=mock.Mock(global_attributes={})
        return cf_var

    def test_all_none(self):
        cf_var = self._make_cf_var()
        coord_name = None
        res = get_names(cf_var, coord_name, {})
        standard_name, long_name, var_name = res
        self.assertIsNone(standard_name)
        self.assertIsNone(long_name)
        self.assertIsNone(var_name)

    def test_ 
        


if __name__ == "__main__":
    tests.main()
