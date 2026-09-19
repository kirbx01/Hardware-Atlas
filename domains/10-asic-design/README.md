# Domain 10 -- ASIC Design (VLSI)

Synthesizable RTL through gates, standard-cell layout, and an open shuttle flow. Verification and documented limitations come before anything gets taped out.

> [!WARNING]
> A DRC-clean GDSII is not a working chip. The flow tells you the layout obeys the rules; it still needs verification and an honest list of what it does not guarantee.

## Prerequisites

Verified RTL from [Domain 08](../08-fpga-and-rtl/README.md). A rough feel for what the gates represent helps; [Domain 11](../11-semiconductor-devices/README.md) explains what those gates are made of afterward.

## Core concepts

- Synthesis with Yosys: RTL into gates, and the area report you actually read
- Place and route with OpenLane against the Sky130 PDK
- Standard cells, and the library that constrains everything above them
- Magic for design rule checking and layout versus schematic
- GDSII as the final, shipable representation

AICTE's *VLSI Design* (EC24) teaches the transistor and delay half of this flow — MOS modelling, noise margins, delay and power models, interconnect parasitics — and this domain runs the layout half: stick-diagram-era layout by hand is what Magic and the open PDK automate for you. The delay and power analysis EC24 spends a unit on is the report your OpenLane run prints at the end; [VLSI Level 02](levels/02-openlane-sky130-flow/README.md) is where the two halves meet.

## Levels

Each lesson here is its own level in the flow, named after what it builds:

| Level | Name | Lesson | What it covers |
|---|---|---|---|
| 01 | [Yosys RTL synthesis](levels/01-yosys-rtl-synthesis/README.md) | 29 | Map RTL to gates and inspect area |
| 02 | [OpenLane Sky130 flow](levels/02-openlane-sky130-flow/README.md) | 30 | Run an open RTL-to-GDSII flow |
| 03 | [Magic DRC and LVS](levels/03-magic-drc-lvs/README.md) | 31 | Verify layout rules and connectivity |

## The flow, start to finish

```mermaid
flowchart LR
    A[RTL] --> B[Synthesis] --> C[Place and route] --> D[DRC / LVS] --> E[GDSII]
```

## Common mistakes

- Treating a clean DRC as proof the layout is right, and skipping LVS
- Ignoring the PDK's documented limitations until a check fails for an unknown reason
- Rerunning the flow with a different tool setting and not recording why
- Fine-tuning the layout before the RTL is actually verified

## Resources

- [OpenLane](https://github.com/The-OpenROAD-Project/OpenLane) and [Magic](https://opencircuitdesign.com/magic/) documentation for deeper configuration.
- [Tiny Tapeout](https://tinytapeout.com/) if you want a real shuttle run to land on your bench.
- [Opportunities](../../opportunities/README.md) for RTL, ASIC, and physical-design roles.

## Where to go from here

- [Domain 11](../11-semiconductor-devices/README.md) and [Domain 12](../12-semiconductor-fabrication/README.md) cover what the PDK is abstracting.
- Back to [Domain 09](../09-computer-architecture/README.md) to re-architect the core now that you know what synthesis rewards.
- **Related in [Opportunities](../../opportunities/README.md):** CHIPS Alliance (OpenLane, OpenROAD), SEMICON India Hackathon, ChipVerse, ChipCraft, and FOSSEE all run student VLSI and EDA tracks; the ACM SIGDA SRC is the research route.