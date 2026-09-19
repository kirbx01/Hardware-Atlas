# VLSI Level 02 -- OpenLane Sky130 Flow

The open RTL-to-GDSII flow: OpenLane runs the synthesized netlist through place and route against the open Sky130 PDK, and the timing and area reports it prints are the delay and power analysis from the syllabus, made concrete.

## Lessons

| # | Lesson | What it builds | Status |
|---|---|---|---|
| 30 | [OpenLane Sky130 flow](../../../../lessons/30-openlane-sky130-flow/README.md) | Run an open RTL-to-GDSII flow | ✅ |

## Why record every run

Rerunning the flow with a different tool setting and not recording why is a common mistake here. The PDK's documented limitations and your own run log are what make the difference reproducible.

## Where to go from here

- [VLSI Level 03 -- Magic DRC and LVS](../03-magic-drc-lvs/README.md) to check the layout your flow produced.
- Back to [Domain 10 overview](../../README.md).