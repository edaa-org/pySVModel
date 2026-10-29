.. _GLOSSARY:

Glossary
########

.. glossary::

   Accellera
   Accellera Systems Initiative
     `Accellera Systems Initiative <https://www.accellera.org/>`__ is the standards organization of the electronic
     design automation industry, formed from Open Verilog International (OVI) and VHDL International, later joined by
     The SPIRIT Consortium and the Open SystemC Initiative (OSCI).

     Accellera developed :term:`SystemVerilog` up to version 3.1a and handed it over to the :term:`IEEE`, which
     standardized it as IEEE Std. 1800.

   HDL
   Hardware Description Language
     A language describing the structure and behavior of digital circuits, for simulation and synthesis, e.g.
     :term:`Verilog` or VHDL.

     Wikipedia: :wiki:`Hardware description language <Hardware_description_language>`

   IEEE
     The `Institute of Electrical and Electronics Engineers <https://www.ieee.org/>`__. Its standards association
     `IEEE SA <https://standards.ieee.org/>`__ publishes the :term:`LRMs <LRM>` of :term:`Verilog` (IEEE Std. 1364) and
     :term:`SystemVerilog` (IEEE Std. 1800).

   LRM
   Language Reference Manual
     The standard defining a language's syntax and semantics.

     IEEE Standard for SystemVerilog - Unified Hardware Design, Specification, and Verification Language:

     * `1800-2023 <https://ieeexplore.ieee.org/document/10458102>`__.
     * `1800-2017 <https://ieeexplore.ieee.org/document/8299595>`__.
     * `1800-2012 <https://ieeexplore.ieee.org/document/6469140>`__.
     * `1800-2009 <https://ieeexplore.ieee.org/document/5354441>`__.
     * `1800-2005 <https://ieeexplore.ieee.org/document/1560791>`__.

     IEEE Standard for Verilog Hardware Description Language:

     * `1364-2005 <https://ieeexplore.ieee.org/document/1620780>`__.
     * `1364-2001 <https://ieeexplore.ieee.org/document/954909>`__.
     * `1364-1995 <https://ieeexplore.ieee.org/document/803556>`__.

   SystemVerilog
     A unified hardware design, specification and verification language, standardized as IEEE Std. 1800 (see
     :term:`LRM`). It extends :term:`Verilog` by verification features like assertions, constrained random stimulus,
     functional coverage and object-oriented testbenches. Since IEEE Std. 1800-2009, SystemVerilog includes Verilog.

     pySVModel names the language revisions in :class:`~pySVModel.SystemVerilogVersion`.

     Wikipedia: :wiki:`SystemVerilog`

   Verilog
     A :term:`hardware description language <HDL>`, standardized as IEEE Std. 1364 in 1995, 2001 and 2005 (see
     :term:`LRM`). IEEE Std. 1800-2009 merged it into :term:`SystemVerilog`.

     Wikipedia: :wiki:`Verilog`
