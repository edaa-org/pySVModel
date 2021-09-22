.. include:: shields.inc

.. raw:: latex

   \part{Introduction}

.. only:: html

   |  |SHIELD:svg:pySVModel-github| |SHIELD:svg:pySVModel-src-license| |SHIELD:svg:pySVModel-tag| |SHIELD:svg:pySVModel-release| |SHIELD:svg:pySVModel-date| |SHIELD:svg:pySVModel-lib-dep|
   |  |SHIELD:svg:pySVModel-gha-test| |SHIELD:svg:pySVModel-codacy-quality| |SHIELD:svg:pySVModel-codacy-coverage| |SHIELD:svg:pySVModel-codecov-coverage| |SHIELD:svg:pySVModel-lib-rank|
   |  |SHIELD:svg:pySVModel-gha-release| |SHIELD:svg:pySVModel-pypi-tag| |SHIELD:svg:pySVModel-pypi-status| |SHIELD:svg:pySVModel-pypi-python| |SHIELD:svg:pySVModel-lib-status| |SHIELD:svg:pySVModel-req-status|
   |  |SHIELD:svg:pySVModel-gha-doc| |SHIELD:svg:pySVModel-doc-license| |SHIELD:svg:pySVModel-ghp-doc|

.. only:: latex

   |SHIELD:png:pySVModel-github| |SHIELD:png:pySVModel-src-license| |SHIELD:png:pySVModel-tag| |SHIELD:png:pySVModel-release| |SHIELD:png:pySVModel-date| |SHIELD:png:pySVModel-lib-dep|
   |SHIELD:png:pySVModel-gha-test| |SHIELD:png:pySVModel-codacy-quality| |SHIELD:png:pySVModel-codacy-coverage| |SHIELD:png:pySVModel-codecov-coverage| |SHIELD:png:pySVModel-lib-rank|
   |SHIELD:png:pySVModel-gha-release| |SHIELD:png:pySVModel-pypi-tag| |SHIELD:png:pySVModel-pypi-status| |SHIELD:png:pySVModel-pypi-python| |SHIELD:png:pySVModel-lib-status| |SHIELD:png:pySVModel-req-status|
   |SHIELD:png:pySVModel-gha-doc| |SHIELD:png:pySVModel-doc-license| |SHIELD:png:pySVModel-ghp-doc|

--------------------------------------------------------------------------------

The pySystemVerilogModel Documentation
######################################

An abstract SystemVerilog language model.



.. _goals:

Main Goals
**********

This package provides a unified abstract language model for SystemVerilog (incl.
Verilog). Projects reading from source files can derive own classes and implement
additional logic to create a concrete language model for their tools.

Projects consuming pre-processed VHDL data (parsed, analyzed or elaborated) can
build higher level features and services on such a model, while supporting multiple
frontends.



.. _usecase:

Use Cases
*********

* TBD



.. _news:

News
****

.. only:: html

   Sep. 2021 - New Repository Created
   ==================================

.. only:: latex

   .. rubric:: New Repository Created

* Moved ``VerilogVersion`` and ``SystemVerilogVersion`` classes from ``pyEDAA.ProjectModel``
  to this new repository.


.. _contributors:

Contributors
************

* `Patrick Lehmann <https://github.com/Paebbels>`__ (Maintainer)
* `Unai Martinez-Corral <https://github.com/umarcor/>`__
* `and more... <https://github.com/edaa-org/pyVHDLModel/graphs/contributors>`__


License
*******

.. only:: html

   This Python package (source code) is licensed under `Apache License 2.0 <Code-License.html>`__. |br|
   The accompanying documentation is licensed under `Creative Commons - Attribution 4.0 (CC-BY 4.0) <Doc-License.html>`__.

.. only:: latex

   This Python package (source code) is licensed under **Apache License 2.0**. |br|
   The accompanying documentation is licensed under **Creative Commons - Attribution 4.0 (CC-BY 4.0)**.

------------------------------------

.. |docdate| date:: %d.%b %Y - %H:%M

.. only:: html

   This document was generated on |docdate|.


.. toctree::
   :caption: Introduction
   :hidden:

   Installation
   Dependency


.. raw:: latex

   \part{Main Documentation}

.. toctree::
   :caption: Main Documentation
   :hidden:

   LanguageModel/index


.. raw:: latex

   \part{References}

.. toctree::
   :caption: References
   :hidden:

   pySystemVerilogModel/index


.. raw:: latex

   \part{Appendix}

.. toctree::
   :caption: Appendix
   :hidden:

   ChangeLog/index
   License
   Doc-License
   Glossary
   genindex

.. #
   py-modindex