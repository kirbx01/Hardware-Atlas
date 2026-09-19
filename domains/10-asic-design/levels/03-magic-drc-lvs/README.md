# VLSI Level 03 -- Magic DRC and LVS

Verification short of tape-out: Magic checks the layout against the design rules, and layout-versus-schematic confirms the drawn geometry actually matches the netlist you intended.

## Lessons

| # | Lesson | What it builds | Status |
|---|---|---|---|
| 31 | [Magic DRC and LVS verification](../../../../lessons/31-magic-drc-lvs-verification/README.md) | Verify layout rules and connectivity | ✅ |

## Why a clean DRC is not a working chip

DRC says the layout obeys the rules; LVS says it matches the netlist; neither says the chip does what the RTL promised. Verification and an honest list of limitations come before anything gets taped out — the same discipline as a single LED measured against Ohm's law.

## Where to go from here

- [Domain 11 -- Semiconductor Devices](../../../11-semiconductor-devices/README.md) explains what the PDK is abstracting.
- [Domain 12 -- Semiconductor Fabrication](../../../12-semiconductor-fabrication/README.md) shows how the process this PDK models actually runs.
- Back to [Domain 10 overview](../../README.md).