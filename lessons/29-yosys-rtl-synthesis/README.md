# Lesson 29: Yosys RTL Synthesis

## What you are building

A reproducible RTL-to-netlist flow for a synthesizable hardware block.

## What you will learn

RTL elaboration, optimization, technology mapping, cell counts, area estimates, and gate-level inspection.

## Prerequisites

[Combinational Arithmetic RTL](../23-combinational-arithmetic-rtl/README.md) and [cocotb Python Testbench](../25-cocotb-python-testbench/README.md).

## Tools and software

- Yosys
- RTL source and constraints
- Netlist viewer or text inspection tools

## Build and test

Write a script that reads RTL, checks hierarchy, optimizes it, maps it to a target library, and reports statistics. Compare two equivalent RTL implementations and explain changes in cell count or timing assumptions.

## What to build next

[Lesson 30: OpenLane Sky130 Flow](../30-openlane-sky130-flow/README.md).
