# 20-Two-Layer PCB Routing

The schematic from Lesson 19 becomes an actual board here: parts get placed on a board outline, traces get routed between them on two copper layers, and the whole thing gets checked against a Design Rule Check (DRC) before it's ready to send to a fabricator.

- **Difficulty:** Intermediate
- **Prerequisites:** [Lesson 19: KiCad Schematic Capture](../19-kicad-schematic-capture/README.md)
- **Approximate time:** 2 to 3 hours
- **What you'll build:** A two-layer (top and bottom copper) PCB layout in KiCad for the LED/resistor circuit, routed by hand, with a clean DRC pass and manufacturing files ready for export

## Why build this?

A schematic tells you *what* connects to *what*. A PCB layout decides *where* everything physically sits and *how* copper gets from one pin to another without shorting against something else. This is the first project in the repository where geometry, not just electrical connectivity, is the thing you're solving for — trace width has to carry the current safely, and two crossing nets need two different layers or a via to get past each other without touching.

This directly follows [Lesson 19](../19-kicad-schematic-capture/README.md) and sets up later fabrication-adjacent lessons like [Lesson 30: OpenLane Sky130 Flow](../30-openlane-sky130-flow/README.md), where an analogous place-and-route process happens for silicon instead of a PCB.

## What you'll learn

- The difference between a schematic net and a physical trace, and what a "ratsnest" line represents before routing.
- Why two-layer boards use a top and bottom copper layer, and how a via moves a trace between them.
- How trace width relates to current-carrying capacity, and why signal traces and power traces are often sized differently.
- What a Design Rule Check (DRC) verifies that ERC cannot: clearances, trace widths, and via sizes against your fabricator's actual capabilities.
- How to generate Gerber and drill files, the actual format a PCB fabricator consumes.

## What you need

| Item | Type | Quantity | Purpose |
|---|---|---:|---|
| KiCad (version 7 or later) | Tool | 1 install | Same tool used for schematic capture; layout is a different editor within the same project |
| Completed schematic from Lesson 19 | File | 1 | The starting point for this layout; footprints must already be assigned |

## Before you build

When you switch from the Schematic Editor to the PCB Editor in KiCad, every net from your schematic appears as a thin, straight "ratsnest" line connecting the relevant footprint pads — a visual to-do list, not a real electrical connection yet. Routing is the process of replacing each ratsnest line with an actual copper trace.

A two-layer board gives you a **top copper layer** and a **bottom copper layer**, separated by an insulating substrate. When two traces need to cross without touching, one of them moves to the other layer through a **via** — a small plated hole connecting the two copper layers electrically. Simple boards like this one can often be routed almost entirely on one layer, using the second layer only where a crossing is unavoidable.

Trace width matters because copper has resistance, and current through a too-narrow trace generates heat. For the tiny current in an LED circuit (well under 50mA), a standard 0.25mm (10 mil) trace is far more than adequate; the concern here is mostly about learning the *habit* of choosing width deliberately rather than accepting a default blindly, since later projects in this series will carry meaningfully more current.

A **Design Rule Check (DRC)** verifies your layout against a set of manufacturing constraints: minimum trace width, minimum clearance between copper features, minimum via drill size. These constraints come from what a real fabricator can physically etch and drill reliably — violate them and the board may not be manufacturable, or may fail electrically even if it looks fine on screen.

## How it works

```mermaid
flowchart LR
    Net["Import Netlist\n(Ratsnest)"] --> Place["Place Footprints\non Board Outline"]
    Place --> Route["Route Traces\n(Top + Bottom Copper)"]
    Route --> DRC["Run DRC"]
    DRC -->|Errors| Route
    DRC -->|Clean| Gerber["Export Gerbers + Drill Files"]
```

| Component | Role |
|---|---|
| Board outline | Defines the physical size and shape the copper and parts must fit within |
| Footprints | The physical land pattern for each part, placed at an actual X/Y position on the board |
| Copper traces | The actual conductive paths replacing each ratsnest connection |
| Vias | Plated holes that move a trace from one copper layer to the other |
| DRC | Final manufacturability check against clearance, width, and drill-size rules |

## Build it

1. Open your Lesson 19 project and switch to the PCB Editor (**Tools → Update PCB from Schematic** if footprints haven't synced yet).
2. Draw a simple rectangular board outline on the `Edge.Cuts` layer, sized to comfortably fit the three footprints (roughly 20mm x 15mm is plenty for this circuit).
3. Place the battery connector footprint, the resistor footprint, and the LED footprint inside the outline, following the ratsnest lines as a rough guide for a sensible physical layout.
4. Set your default trace width (Route → Line Width, or the toolbar dropdown) to 0.25mm for this low-current design.
5. Route each ratsnest connection by clicking one pad and drawing a trace to the next, replacing the thin gray lines with solid copper.
6. If any two traces would need to cross, route one of them on the bottom copper layer instead, placing a via where it transitions.
7. Run **Inspect → Design Rules Checker** and resolve every violation.
8. Once clean, run **File → Fabrication Outputs → Gerbers** and **Drill Files** to generate the manufacturing files.

## Verify it

- Confirm DRC reports zero violations after routing.
- Use KiCad's 3D viewer (**View → 3D Viewer**) to visually confirm the board looks physically sensible — no footprint overlapping another, no trace running off the board edge.
- Open the generated Gerber files in a Gerber viewer (KiCad's built-in Gerber viewer, or an online one) and confirm the top and bottom copper layers show the traces you expect on the layers you expect.

## What should you see?

A compact two-layer board with every ratsnest line replaced by a solid copper trace, zero DRC violations, and a clean set of Gerber and drill files ready to upload to a fabricator's website.

## Troubleshooting

| Symptom | Possible cause | What to check |
|---|---|---|
| DRC reports a clearance violation | Two traces or pads routed too close together | Increase spacing, or check your board's design rules match your fabricator's actual minimum clearance |
| Ratsnest line remains after "routing" it | Trace didn't actually connect to the pad center | Zoom in and confirm the trace endpoint snaps onto the pad, not near it |
| Via appears but net still shows unrouted on one layer | Trace segment on one side of the via wasn't drawn | Check both layers around the via for a continuous copper path |
| Gerber viewer shows a layer that looks empty | Wrong layer selected during routing (drew on a silkscreen or a mechanical layer by mistake) | Re-check the active layer indicator in KiCad before re-routing that segment |

Debug DRC violations one at a time from the top of the report; layout errors are usually local to one specific trace or pad, not systemic.

## Common mistakes

- **Placing parts before knowing which nets need to be close together.** A rough glance at the ratsnest before placing footprints saves a lot of later re-routing.
- **Ignoring DRC until the very end.** Running it after every few traces catches a clearance problem while it's one trace, not fifteen.
- **Using a trace width far below what your fabricator can reliably etch,** just because it looks cleaner on screen — thinner isn't better, it's riskier.
- **Forgetting to add a via when moving a trace to the other layer,** leaving two disconnected trace segments that look continuous on screen but aren't electrically joined.

## Think about it

- Why is a two-layer board sufficient for this circuit, but not for something like the RISC-V datapath board this lesson eventually feeds into?
- What determines the *minimum* trace width a fabricator can reliably produce, physically?
- Why might a designer deliberately route a power net wider than a signal net even at the same current, for reasons beyond current-carrying capacity?
- What does a via cost in terms of board real estate and reliability that a same-layer trace doesn't?

## Experiment with it

- Re-route the same three-part circuit using zero vias, keeping everything on a single copper layer, and see if it's possible for this simple case.
- Deliberately violate a clearance rule, run DRC, and read exactly how KiCad reports it, so the message is recognizable later in a denser board.
- Widen the power trace to 0.5mm and observe how it changes the routing options for the remaining connections.

## Simulation

KiCad's built-in 3D viewer functions as a lightweight physical simulation of the finished board, useful for a sanity check before committing to fabrication:

Accessible via **View → 3D Viewer** inside the KiCad PCB Editor, with the current project open.

## Recommended viewing

### PCB routing basics: from ratsnest to finished board.

A hands-on walkthrough of placing parts and routing a small two-layer board end to end, useful for seeing the placement-then-routing workflow in real time.

[Watch on YouTube](https://www.youtube.com/results?search_query=kicad+pcb+routing+two+layer+tutorial)

## Further reading

- **Tutorial:** [KiCad Official Documentation, PCB Editor](https://docs.kicad.org/) — the canonical reference for routing tools and DRC configuration.
- **Tutorial:** [SparkFun, PCB Basics](https://learn.sparkfun.com/tutorials/pcb-basics) — background on layer stackups, copper weight, and trace width tables.
- **Reference:** [Fabricator-specific design rule pages (e.g., JLCPCB, PCBWay)](https://jlcpcb.com/capabilities) — the actual manufacturing limits your DRC rules should be set to match.

## Hardware Atlas resources

### Tools
For choosing a PCB fabricator and understanding turnaround/cost tradeoffs: [See Tools](../../resources/tools.md)

### Help
If DRC won't clear or Gerbers look wrong in the viewer: [See Hardware Help](../../resources/help.md)

## Sourcing

Two-layer prototype boards are inexpensive from most fabricators for small quantities. For India-specific fabrication and component sourcing: [See India Resources](../../resources/india.md)

## Going deeper

Placement and routing here — deciding where things go, then connecting them without violating physical constraints — is the same fundamental problem OpenLane and Magic solve automatically for silicon in [Lesson 30](../30-openlane-sky130-flow/README.md) and [Lesson 31](../31-magic-drc-lvs-verification/README.md). Doing it by hand once, on a simple three-part board, makes the automated version far less mysterious later.

## Where this fits in Hardware Atlas

```mermaid
flowchart LR
    Prev["19: KiCad Schematic Capture"] --> Current["20: Two-Layer PCB Routing"]
    Current --> Next["21: Logic Analyzer Decode"]
```

Move to [Lesson 21: Logic Analyzer Decode](../21-logic-analyzer-decode/README.md). You've now designed a board from schematic to manufacturable Gerbers; the next lesson shifts to test and measurement, capturing and decoding real digital signals off a working circuit.