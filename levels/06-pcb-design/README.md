# Level 06 -- PCB Design

Converting a tested breadboard circuit into a schematic and a real two-layer board. Footprints, design rules, decoupling, return paths, Gerbers, and revision control.

> [!NOTE]
> Start from a circuit you have already built and measured. The goal is to make the reliable thing reproducible, not to debug electronics while learning a CAD tool at the same time.

## What this level covers

- Schematic capture: symbols, nets, and a schematic that reads like a design document
- Footprints, and the packages they must match exactly
- Signed-off design rules: DRC for geometry, ERC for connectivity
- Decoupling placement and the return path under every trace
- Gerber generation and the review you do before ordering

## Lessons

| # | Lesson | What it builds |
|---|---|---|
| 19 | [KiCad schematic capture](../../lessons/19-kicad-schematic-capture/README.md) | Design the regulated microcontroller schematic |
| 20 | [Two-layer PCB routing](../../lessons/20-two-layer-pcb-routing/README.md) | Route, run DRC, generate Gerbers |

## From breadboard to board

```mermaid
flowchart LR
    A[Breadboard circuit] --> B[KiCad schematic]
    B --> C[Two-layer layout]
    C --> D[DRC and review]
    D --> E[Gerbers]
    E --> F[Ordered board]
```

## Common mistakes

- A footprint for one package variant while the part on hand is another
- Decoupling capacitor placed on the wrong side of the pin it is meant to protect
- Routing every trace first and remembering only later that there is a return path
- Shipping Gerbers without a final visual pass over every layer

## Where to go from here

- [Level 07](../07-hardware-interfaces/README.md) for bus-level debugging on something you actually routed.
- [Projects](../../projects/README.md) if a made-and-ordered board is your entry point for a contribution.

## Resources

- [Tools](../../resources/tools.md) for soldering kit and test gear.
- [Phil's Lab](https://www.youtube.com/@PhilsLab/playlists?app=desktop) and [Robert Feranec](https://www.youtube.com/@RobertFeranec/videos) show professional layout workflow end to end.