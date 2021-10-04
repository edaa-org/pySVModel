.. _dependency:

Dependency
##########

.. |img-pySVModel-lib-status| image:: https://img.shields.io/librariesio/release/pypi/pySVModel
   :alt: Libraries.io status for latest release
   :height: 22
   :target: https://libraries.io/github/edaa-org/pySVModel
.. |img-pySVModel-req-status| image:: https://img.shields.io/requires/github/edaa-org/pySVModel
   :alt: Requires.io
   :height: 22
   :target: https://requires.io/github/edaa-org/pySVModel/requirements/?branch=main

+------------------------------------------+------------------------------------------+
| `Libraries.io <https://libraries.io/>`_  | `Requires.io <https://requires.io/>`_    |
+==========================================+==========================================+
| |img-pySVModel-lib-status|               | |img-pySVModel-req-status|               |
+------------------------------------------+------------------------------------------+


.. _dependency-package:

pySVModel Package
*****************

+-----------------------------------------------------+-------------+---------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| **Package**                                         | **Version** | **License**                                                         | **Dependencies**                                                                                                                |
+=====================================================+=============+=====================================================================+=================================================================================================================================+
| `pydecor <https://github.com/mplanchard/pydecor>`__ | ≥2.0.1      | `MIT <https://github.com/mplanchard/pydecor/blob/master/LICENSE>`__ | * `dill <https://github.com/uqfoundation/dill>`__ (`BSD 3-clause <https://github.com/uqfoundation/dill/blob/master/LICENSE>`__) |
|                                                     |             |                                                                     | * `six <https://github.com/benjaminp/six>`__ (`MIT <https://github.com/benjaminp/six/blob/master/LICENSE>`__)                   |
+-----------------------------------------------------+-------------+---------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+


.. _dependency-testing:

Unit Testing / Coverage
***********************

Additional Python packages needed for testing and code coverage collection.
These packages are only needed for developers or on a CI server, thus
sub-dependencies are not evaluated further.

+-----------------------------------------------------------+-------------+----------------------------------------------------------------------------------------+----------------------+
| **Package**                                               | **Version** | **License**                                                                            | **Dependencies**     |
+===========================================================+=============+========================================================================================+======================+
| `pytest <https://github.com/pytest-dev/pytest>`__         | ≥6.2.4      | `MIT <https://github.com/pytest-dev/pytest/blob/master/LICENSE>`__                     | *Not yet evaluated.* |
+-----------------------------------------------------------+-------------+----------------------------------------------------------------------------------------+----------------------+
| `pytest-cov <https://github.com/pytest-dev/pytest-cov>`__ | ≥2.12.1     | `MIT <https://github.com/pytest-dev/pytest-cov/blob/master/LICENSE>`__                 | *Not yet evaluated.* |
+-----------------------------------------------------------+-------------+----------------------------------------------------------------------------------------+----------------------+
| `Coverage <https://github.com/nedbat/coveragepy>`__       | ≥6.0        | `Apache License, 2.0 <https://github.com/nedbat/coveragepy/blob/master/LICENSE.txt>`__ | *Not yet evaluated.* |
+-----------------------------------------------------------+-------------+----------------------------------------------------------------------------------------+----------------------+


.. _dependency-documentation:

Sphinx Documentation
********************

Additional Python packages needed for documentation generation. These packages
are only needed for developers or on a CI server, thus sub-dependencies are not
evaluated further.

+-------------------------------------------------------------------------------------------------+--------------+----------------------------------------------------------------------------------------------------------+----------------------+
| **Package**                                                                                     | **Version**  | **License**                                                                                              | **Dependencies**     |
+=================================================================================================+==============+==========================================================================================================+======================+
| `Sphinx <https://github.com/sphinx-doc/sphinx>`__                                               | ≥4.2.0       | `BSD 3-Clause <https://github.com/sphinx-doc/sphinx/blob/master/LICENSE>`__                              | *Not yet evaluated.* |
+-------------------------------------------------------------------------------------------------+--------------+----------------------------------------------------------------------------------------------------------+----------------------+
| `sphinx_btd_theme <https://github.com/buildthedocs/sphinx.theme>`__                             |              | `MIT <https://github.com/buildthedocs/sphinx.theme/blob/master/LICENSE>`__                               | *Not yet evaluated.* |
+-------------------------------------------------------------------------------------------------+--------------+----------------------------------------------------------------------------------------------------------+----------------------+
| `autoapi <https://github.com/carlos-jenkins/autoapi>`__                                         |              | `Apache License, 2.0 <https://github.com/carlos-jenkins/autoapi/blob/master/LICENSE>`__                  | *Not yet evaluated.* |
+-------------------------------------------------------------------------------------------------+--------------+----------------------------------------------------------------------------------------------------------+----------------------+
| !! `sphinx_fontawesome <https://github.com/fraoustin/sphinx_fontawesome>`__                     | ≥0.0.6       | `GPL 2.0 <https://github.com/fraoustin/sphinx_fontawesome/blob/master/LICENSE>`__                        | *Not yet evaluated.* |
+-------------------------------------------------------------------------------------------------+--------------+----------------------------------------------------------------------------------------------------------+----------------------+
| `sphinx_autodoc_typehints <https://github.com/agronholm/sphinx-autodoc-typehints>`__            | ≥1.12.0      | `MIT <https://github.com/agronholm/sphinx-autodoc-typehints/blob/master/LICENSE>`__                      | *Not yet evaluated.* |
+-------------------------------------------------------------------------------------------------+--------------+----------------------------------------------------------------------------------------------------------+----------------------+
| `Pygments <https://github.com/pygments/pygments>`__                                             | ≥2.9.0       | `BSD 2-Clause <https://github.com/pygments/pygments/blob/master/LICENSE>`__                              | *Not yet evaluated.* |
+-------------------------------------------------------------------------------------------------+--------------+----------------------------------------------------------------------------------------------------------+----------------------+
