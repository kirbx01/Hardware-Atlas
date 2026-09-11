# Level 10 -- ASIC Design

Synthesizable RTL through gates, standard-cell layout, and an open shuttle flow. Verification and documented limitations come before anything gets taped out.

> [!WARNING]
> A DRC-clean GDSII is not a working chip. The flow tells you the layout obeys the rules; it still needs verification and an honest list of what it does not guarantee.

## What this level covers

- Synthesis with Yosys: RTL into gates, and the area report you actually read
- Place and route with OpenLane against the Sky130 PDK
- Standard cells, and the library that constrains everything above them
- Magic for design rule checking and layout versus schematic
- GDSII as the final, shipable representation

## Lessons

| # | Lesson | What it builds |
|---|---|---|
| 29 | [Yosys RTL synthesis](../../lessons/29-yosys-rtl-synthesis/README.md) | Map RTL to gates and inspect area |
| 30 | [OpenLane Sky130 flow](../../lessons/30-openlane-sky130-flow/README.md) | Run an open RTL-to-GDSII flow |
| 31 | [Magic DRC and LVS verification](../../lessons/31-magic-drc-lvs-verification/README.md) | Verify layout rules and connectivity |

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

## Where to go from here

- [Level 11](../11-semiconductor-devices/README.md) and [Level 12](../12-semiconductor-fabrication/README.md) cover what the PDK is abstracting.
- [OpenLane](https://github.com/The-OpenROAD-Project/OpenLane) and [Magic](https://opencircuitdesign.com/magic/) documentation for deeper configuration.