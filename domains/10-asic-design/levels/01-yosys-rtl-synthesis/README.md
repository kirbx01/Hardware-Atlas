# VLSI Level 01 -- Yosys RTL Synthesis

The first step of the RTL-to-GDSII flow: Yosys maps the verified RTL from Domain 08 into gates against a standard-cell library, and the area report you actually read tells you what synthesis rewarded.

## Lessons

| # | Lesson | What it builds | Status |
|---|---|---|---|
| 29 | [Yosys RTL synthesis](../../../../lessons/29-yosys-rtl-synthesis/README.md) | Map RTL to gates and inspect area | ✅ |

## Why synthesis first

Place and route is only meaningful against the netlist synthesis produced. Seeing the gate count move when you change the RTL is the first honest answer to "how big is this thing."

## Where to go from here

- [VLSI Level 02 -- OpenLane Sky130 Flow](../02-openlane-sky130-flow/README.md) to take that netlist toward a chip.
- Back to [Domain 10 overview](../../README.md).