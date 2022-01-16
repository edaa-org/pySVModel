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
# Copyright 2021-2022 Patrick Lehmann - Boetzingen, Germany                                                            #
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
"""
An abstract SystemVerilog language model.

:copyright: Copyright 2021-2022 Patrick Lehmann - Bötzingen, Germany
:license: Apache License, Version 2.0
"""
from enum import unique, Enum
from typing import Dict, Union

from pyTooling.Decorators import export


__author__ =    "Patrick Lehmann"
__email__ =     "Paebbels@gmail.com"
__copyright__ = "2021-2022, Patrick Lehmann"
__license__ =   "Apache License, Version 2.0"
__version__ =   "0.3.5"


@export
@unique
class VerilogVersion(Enum):
	Any =           -1
	Verilog95 =     95
	Verilog2001 = 2001
	Verilog2005 = 2005

	__VERSION_MAPPINGS__: Dict[Union[int, str], Enum] = {
		95:     Verilog95,
		1:      Verilog2001,
		5:      Verilog2005,
		1995:   Verilog95,
		2001:   Verilog2001,
		2005:   Verilog2005,
		"Any":  Any,
		"95":   Verilog95,
		"01":   Verilog2001,
		"05":   Verilog2005,
		"1995": Verilog95,
		"2001": Verilog2001,
		"2005": Verilog2005,
	}

	def __init__(self, *_):
		"""Patch the embedded MAP dictionary"""
		for k, v in self.__class__.__VERSION_MAPPINGS__.items():
			if (not isinstance(v, self.__class__)) and (v == self.value):
				self.__class__.__VERSION_MAPPINGS__[k] = self

	@classmethod
	def Parse(cls, value):
		try:
			return cls.__VERSION_MAPPINGS__[value]
		except KeyError:
			ValueError("Value '{0!s}' cannot be parsed to member of {1}.".format(value, cls.__name__))

	def __lt__(self, other):
		return self.value < other.value

	def __le__(self, other):
		return self.value <= other.value

	def __gt__(self, other):
		return self.value > other.value

	def __ge__(self, other):
		return self.value >= other.value

	def __ne__(self, other):
		return self.value != other.value

	def __eq__(self, other):
		if (self is self.__class__.Any) or (other is self.__class__.Any):
			return True
		else:
			return self.value == other.value

	def __str__(self):
		return "Verilog'" + str(self.value)[-2:]

	def __repr__(self):
		return str(self.value)


@export
@unique
class SystemVerilogVersion(Enum):
	Any =                 -1
	SystemVerilog2005 = 2005
	SystemVerilog2009 = 2009
	SystemVerilog2012 = 2012
	SystemVerilog2017 = 2017

	__VERSION_MAPPINGS__: Dict[Union[int, str], Enum] = {
		5:      SystemVerilog2005,
		9:      SystemVerilog2009,
		12:     SystemVerilog2012,
		17:     SystemVerilog2017,
		2005:   SystemVerilog2005,
		2009:   SystemVerilog2009,
		2012:   SystemVerilog2012,
		2017:   SystemVerilog2017,
		"Any":  Any,
		"05":   SystemVerilog2005,
		"09":   SystemVerilog2009,
		"12":   SystemVerilog2012,
		"17":   SystemVerilog2017,
		"2005": SystemVerilog2005,
		"2009": SystemVerilog2009,
		"2012": SystemVerilog2012,
		"2017": SystemVerilog2017,
	}

	def __init__(self, *_):
		"""Patch the embedded MAP dictionary"""
		for k, v in self.__class__.__VERSION_MAPPINGS__.items():
			if (not isinstance(v, self.__class__)) and (v == self.value):
				self.__class__.__VERSION_MAPPINGS__[k] = self

	@classmethod
	def Parse(cls, value):
		try:
			return cls.__VERSION_MAPPINGS__[value]
		except KeyError:
			ValueError("Value '{0!s}' cannot be parsed to member of {1}.".format(value, cls.__name__))

	def __lt__(self, other):
		return self.value < other.value

	def __le__(self, other):
		return self.value <= other.value

	def __gt__(self, other):
		return self.value > other.value

	def __ge__(self, other):
		return self.value >= other.value

	def __ne__(self, other):
		return self.value != other.value

	def __eq__(self, other):
		if (self is self.__class__.Any) or (other is self.__class__.Any):
			return True
		else:
			return self.value == other.value

	def __str__(self):
		return "SV'" + str(self.value)[-2:]

	def __repr__(self):
		return str(self.value)
