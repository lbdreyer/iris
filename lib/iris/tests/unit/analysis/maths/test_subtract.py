# (C) British Crown Copyright 2014, Met Office
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
"""Unit tests for the :func:`iris.analysis.maths.subtract` function."""

from __future__ import (absolute_import, division, print_function)

# Import iris.tests first so that some things can be initialised before
# importing anything else.
import iris.tests as tests

import operator

from iris.analysis.maths import subtract
from iris.tests.unit.analysis.maths import \
    CubeArithmeticBroadcastingTestMixin, CubeArithmeticMaskingTestMixin


class TestBroadcasting(tests.IrisTest, CubeArithmeticBroadcastingTestMixin):
    @property
    def data_op(self):
        return operator.sub

    @property
    def cube_func(self):
        return subtract


class TestMasking(tests.IrisTest, CubeArithmeticMaskingTestMixin):
    @property
    def data_op(self):
        return operator.sub

    @property
    def cube_func(self):
        return subtract


if __name__ == "__main__":
    tests.main()
