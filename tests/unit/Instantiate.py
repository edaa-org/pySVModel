# ==================================================================================================================== #
#              ______     ____  __           _      _                                                                  #
#  _ __  _   _/ ___\ \   / /  \/  | ___   __| | ___| |                                                                 #
# | '_ \| | | \___ \\ \ / /| |\/| |/ _ \ / _` |/ _ \ |                                                                 #
# | |_) | |_| |___) |\ V / | |  | | (_) | (_| |  __/ |                                                                 #
# | .__/ \__, |____/  \_/  |_|  |_|\___/ \__,_|\___|_|                                                                 #
# |_|    |___/                                                                                                         #
# ==================================================================================================================== #
# Authors:                                                                                                             #
#   Patrick Lehmann                                                                                                    #
#                                                                                                                      #
# License:                                                                                                             #
# ==================================================================================================================== #
# Copyright 2021-2026 Patrick Lehmann - Boetzingen, Germany                                                            #
#                                                                                                                      #
# Licensed under the Apache License, Version 2.0 (the "License");                                                      #
# you may not use this file except in compliance with the License.                                                     #
# You may obtain a copy of the License at                                                                              #
#                                                                                                                      #
#   http://www.apache.org/licenses/LICENSE-2.0                                                                         #
#                                                                                                                      #
# Unless required by applicable law or agreed to in writing, software                                                  #
# distributed under the License is distributed on an "AS IS" BASIS,                                                    #
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.                                             #
# See the License for the specific language governing permissions and                                                  #
# limitations under the License.                                                                                       #
#                                                                                                                      #
# SPDX-License-Identifier: Apache-2.0                                                                                  #
# ==================================================================================================================== #
#
"""Instantiation tests for the language model."""
from unittest  import TestCase

from pySVModel import SystemVerilogVersion


if __name__ == "__main__":  # pragma: no cover
	print("ERROR: you called a testcase declaration file as an executable module.")
	print("Use: 'python -m unitest <testcase module>'")
	exit(1)


class SVVersion(TestCase):
	def test_Any(self) -> None:
		versions = (
			SystemVerilogVersion.Parse(-1),
			SystemVerilogVersion.Parse("Any"),
		)

		for version in versions:
			self.assertIs(SystemVerilogVersion.Any, version)

		print()
		print(version)
		print(version.value)

	def test_V1995(self) -> None:
		versions = (
			SystemVerilogVersion.Parse(95),
			SystemVerilogVersion.Parse(1995),
			SystemVerilogVersion.Parse("95"),
			SystemVerilogVersion.Parse("1995"),
		)

		for version in versions:
			self.assertIs(SystemVerilogVersion.Verilog95, version)

		print()
		print(version)
		print(version.value)

	def test_V2001(self) -> None:
		versions = (
			SystemVerilogVersion.Parse(1),
			SystemVerilogVersion.Parse(2001),
			SystemVerilogVersion.Parse("01"),
			SystemVerilogVersion.Parse("2001"),
		)

		for version in versions:
			self.assertIs(SystemVerilogVersion.Verilog2001, version)

		print()
		print(version)
		print(version.value)

	def test_V2005(self) -> None:
		versions = (
			SystemVerilogVersion.Parse(5),
			# SystemVerilogVersion.Parse(2005),
			SystemVerilogVersion.Parse("05"),
			# SystemVerilogVersion.Parse("2005"),
		)

		for version in versions:
			self.assertIs(SystemVerilogVersion.Verilog2005, version)

		print()
		print(version)
		print(version.value)

	def test_SV2005(self) -> None:
		versions = (
			# SystemVerilogVersion.Parse(5),
			SystemVerilogVersion.Parse(2005),
			# SystemVerilogVersion.Parse("05"),
			SystemVerilogVersion.Parse("2005"),
		)

		for version in versions:
			self.assertIs(SystemVerilogVersion.SystemVerilog2005, version)

		print()
		print(version)
		print(version.value)

	def test_SV2009(self) -> None:
		versions = (
			SystemVerilogVersion.Parse(9),
			SystemVerilogVersion.Parse(2009),
			SystemVerilogVersion.Parse("09"),
			SystemVerilogVersion.Parse("2009"),
		)

		for version in versions:
			self.assertIs(SystemVerilogVersion.SystemVerilog2009, version)

		print()
		print(version)
		print(version.value)

	def test_SV2012(self) -> None:
		versions = (
			SystemVerilogVersion.Parse(12),
			SystemVerilogVersion.Parse(2012),
			SystemVerilogVersion.Parse("12"),
			SystemVerilogVersion.Parse("2012"),
		)

		for version in versions:
			self.assertIs(SystemVerilogVersion.SystemVerilog2012, version)

		print()
		print(version)
		print(version.value)

	def test_SV2017(self) -> None:
		versions = (
			SystemVerilogVersion.Parse(17),
			SystemVerilogVersion.Parse(2017),
			SystemVerilogVersion.Parse("17"),
			SystemVerilogVersion.Parse("2017"),
		)

		for version in versions:
			self.assertIs(SystemVerilogVersion.SystemVerilog2017, version)

		print()
		print(version)
		print(version.value)

	def test_IntError(self) -> None:
		with self.assertRaises(ValueError):
			_ = SystemVerilogVersion.Parse(0)

		with self.assertRaises(ValueError):
			_ = SystemVerilogVersion.Parse(13)

	def test_StrError(self) -> None:
		with self.assertRaises(ValueError):
			_ = SystemVerilogVersion.Parse("0")

		with self.assertRaises(ValueError):
			_ = SystemVerilogVersion.Parse("13")
