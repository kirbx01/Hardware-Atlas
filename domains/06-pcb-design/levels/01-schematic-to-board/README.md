# PCB Design Level 01 -- Schematic to Board

A tested breadboard circuit becomes a schematic that reads like a design document, then a real two-layer board with signed-off DRC, honest footprints, and a Gerber review before anything ships.

## Lessons

| # | Lesson | What it builds | Status |
|---|---|---|---|
| 19 | [KiCad schematic capture](../../../../lessons/19-kicad-schematic-capture/README.md) | Design the regulated microcontroller schematic | ✅ |
| 20 | [Two-layer PCB routing](../../../../lessons/20-two-layer-pcb-routing/README.md) | Route, run DRC, generate Gerbers | ✅ |

## Why review is the skill

This is the only domain whose deliverable ships to a factory. The discipline is review, not routing: a footprint for the wrong package variant or a decoupling cap on the wrong side of its pin costs money and days, not just a redraw.

## Where to go from here

- [Domain 07 -- Hardware Interfaces](../../../07-hardware-interfaces/README.md) for bus-level debugging on something you actually routed.
- Back to [Domain 06 overview](../../README.md).