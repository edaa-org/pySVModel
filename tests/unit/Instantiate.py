# =============================================================================
#              ____            _              __     __        _ _             __  __           _      _
#  _ __  _   _/ ___| _   _ ___| |_ ___ _ __ __\ \   / /__ _ __(_) | ___   __ _|  \/  | ___   __| | ___| |
# | '_ \| | | \___ \| | | / __| __/ _ \ '_ ` _ \ \ / / _ \ '__| | |/ _ \ / _` | |\/| |/ _ \ / _` |/ _ \ |
# | |_) | |_| |___) | |_| \__ \ ||  __/ | | | | \ V /  __/ |  | | | (_) | (_| | |  | | (_) | (_| |  __/ |
# | .__/ \__, |____/ \__, |___/\__\___|_| |_| |_|\_/ \___|_|  |_|_|\___/ \__, |_|  |_|\___/ \__,_|\___|_|
# |_|    |___/       |___/                                               |___/
# ==============================================================================
# Authors:            Patrick Lehmann
#
# Python unittest:    Instantiation tests for the language model.
#
# License:
# ==============================================================================
# Copyright 2021-2021 Patrick Lehmann - Boetzingen, Germany
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# SPDX-License-Identifier: Apache-2.0
# ==============================================================================
#
from unittest import TestCase

from pySystemVerilogModel import VerilogVersion, SystemVerilogVersion


if __name__ == "__main__":
	print("ERROR: you called a testcase declaration file as an executable module.")
	print("Use: 'python -m unitest <testcase module>'")
	exit(1)


class Instantiate(TestCase):
	def test_VerilogVersion(self):
		version = VerilogVersion.Parse("95")

		self.assertIsNotNone(version)

	def test_SystemVerilogVersion(self):
		version = SystemVerilogVersion.Parse("2017")

		self.assertIsNotNone(version)