<p align="center">
  <a title="edaa-org.github.io/pySVModel" href="https://edaa-org.github.io/pySVModel"><img height="80px" src="doc/_static/logo.svg"/></a>
</p>

[![Sourcecode on GitHub](https://img.shields.io/badge/pyEDAA-pySVModel-29b6f6.svg?longCache=true&style=flat-square&logo=GitHub&labelColor=0277bd)](https://GitHub.com/edaa-org/pySVModel)
[![Sourcecode License](https://img.shields.io/pypi/l/pySVModel?longCache=true&style=flat-square&logo=Apache&label=code)](LICENSE.md)
[![Documentation](https://img.shields.io/website?longCache=true&style=flat-square&label=edaa-org.github.io%2FpySVModel&logo=GitHub&logoColor=fff&up_color=blueviolet&up_message=Read%20now%20%E2%9E%9A&url=https%3A%2F%2Fedaa-org.github.io%2FpySVModel%2Findex.html)](https://edaa-org.github.io/pySVModel/)
[![Documentation License](https://img.shields.io/badge/doc-CC--BY%204.0-green?longCache=true&style=flat-square&logo=CreativeCommons&logoColor=fff)](LICENSE.md)
[![Gitter](https://img.shields.io/badge/chat-on%20gitter-4db797.svg?longCache=true&style=flat-square&logo=gitter&logoColor=e8ecef)](https://gitter.im/hdl/community)  
[![PyPI](https://img.shields.io/pypi/v/pySVModel?longCache=true&style=flat-square&logo=PyPI&logoColor=FBE072)](https://pypi.org/project/pySVModel/)
![PyPI - Status](https://img.shields.io/pypi/status/pySVModel?longCache=true&style=flat-square&logo=PyPI&logoColor=FBE072)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pySVModel?longCache=true&style=flat-square&logo=PyPI&logoColor=FBE072)  
[![GitHub Workflow - Build and Test Status](https://img.shields.io/github/workflow/status/edaa-org/pySVModel/Pipeline/main?longCache=true&style=flat-square&label=Build%20and%20Test&logo=GitHub%20Actions&logoColor=FFFFFF)](https://GitHub.com/edaa-org/pySVModel/actions/workflows/Pipeline.yml)
[![Libraries.io status for latest release](https://img.shields.io/librariesio/release/pypi/pySVModel?longCache=true&style=flat-square&logo=Libraries.io&logoColor=fff)](https://libraries.io/github/edaa-org/pySVModel)
[![Codacy - Quality](https://img.shields.io/codacy/grade/39d312bf98244961975559f141c3e000?longCache=true&style=flat-square&logo=Codacy)](https://app.codacy.com/gh/edaa-org/pySVModel)
[![Codacy - Coverage](https://img.shields.io/codacy/coverage/39d312bf98244961975559f141c3e000?longCache=true&style=flat-square&logo=Codacy)](https://app.codacy.com/gh/edaa-org/pySVModel)
[![Codecov - Branch Coverage](https://img.shields.io/codecov/c/github/edaa-org/pySVModel?longCache=true&style=flat-square&logo=Codecov)](https://codecov.io/gh/edaa-org/pySVModel)

<!--
[![Dependent repos (via libraries.io)](https://img.shields.io/librariesio/dependent-repos/pypi/pySVModel?longCache=true&style=flat-square&logo=GitHub)](https://GitHub.com/edaa-org/pySVModel/network/dependents)
[![Requires.io](https://img.shields.io/requires/github/edaa-org/pySVModel?longCache=true&style=flat-square)](https://requires.io/github/EDAA-ORG/pySVModel/requirements/?branch=main)
[![Libraries.io SourceRank](https://img.shields.io/librariesio/sourcerank/pypi/pySVModel?longCache=true&style=flat-square)](https://libraries.io/github/edaa-org/pySVModel/sourcerank)
-->

An abstract language model of SystemVerilog (incl. Verilog) written in Python.


## Main Goals

This package provides a unified abstract language model for SystemVerilog (incl. Verilog).
Projects reading from source files can derive own classes and implement additional logic to create a concrete language
model for their tools.

Projects consuming pre-processed System Verilog data (parsed, analyzed or elaborated) can build higher level features
and services on such a model, while supporting multiple frontends.


## Use Cases

### pySVModel Generators

* See [#11: Interfacing Surelog/UHDM](https://GitHub.com/edaa-org/pySVModel/issues/11)

*TBD*

### pySVModel Consumers

* [Electronic Design Automation Abstraction (EDA²)](https://edaa-org.github.io/)

*TBD*

## Examples

### List all Modules with Parameters and Ports

*TBD*

## Contributors

* [Patrick Lehmann](https://GitHub.com/Paebbels) (Maintainer)
* [Unai Martinez-Corral](https://GitHub.com/umarcor)
* [and more...](https://GitHub.com/edaa-org/pySVModel/graphs/contributors)

## License

This Python package (source code) licensed under [Apache License 2.0](LICENSE.md).  
The accompanying documentation is licensed under [Creative Commons - Attribution 4.0 (CC-BY 4.0)](doc/Doc-License.rst).

-------------------------
SPDX-License-Identifier: Apache-2.0
