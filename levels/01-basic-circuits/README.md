# Level 01 -- Basic Circuits

Ohm's law, polarity, switches, charge and discharge, and time constants: the vocabulary every other level reuses.

## Prerequisites

Work through [Level 00](../00-getting-started/README.md) if wiring a breadboard or reading a multimeter is new. If you can already predict the current through a resistor from the drop across it, this level goes fast. Read the lesson you are missing and move on.

## Core concepts

- Ohm's law as a working tool, not a formula to memorise
- Kirchhoff's laws as the accounting rules behind every divider and node you measure
- Voltage dividers, and why a load changes the number you measure
- Pull-up and pull-down resistors for defined logic states
- A BJT as a low-side switch, with the base resistor sized on purpose
- RC charge and discharge, and the tau = RC relation

Your two resistors in the divider lesson are the first live example of Kirchhoff's current law. Superposition, Thevenin, and Norton theorems are the same ideas pushed further; AICTE's *Network Theory* (EC06) teaches them formally, and they become mandatory once you start diagnosing real circuits in Level 02.

## Lessons

| # | Lesson | What it builds |
|---|---|---|
| 01 | [LED circuit](../../lessons/01-led-circuit/README.md) | Current limiting and polarity in the first safe build |
| 02 | [Voltage divider](../../lessons/02-voltage-divider/README.md) | Node voltage, and what a load does to it |
| 03 | [Button and LED](../../lessons/03-button-and-led/README.md) | Switches, pull-ups, defined logic states |
| 04 | [Transistor switch](../../lessons/04-transistor-switch/README.md) | Low-side switching with a sized base resistor |
| 05 | [RC circuit](../../lessons/05-rc-circuit/README.md) | Time constants and charge/discharge curves |

## How the pieces connect

```mermaid
flowchart LR
    A[Ohm's law] --> B[Voltage divider]
    A --> C[Transistor switch]
    B --> D[Loading]
    A --> E[RC time constant]
    C --> F[Defined logic states]
```

## Common mistakes

- Measuring a divider with a meter that loads it harder than the circuit you are testing
- Leaving a button input floating with no pull-up
- Sizing the base resistor right up against the absolute maximum, or skipping it entirely
- Reading tau as the time to fully charge instead of ~63%

## Resources

- [Simulation](../../resources/simulation.md) to check a circuit before you build it.
- [Tools](../../resources/tools.md) for the meter and power source you will use here.
- [Opportunities](../../opportunities/README.md) for entry-level hardware roles built on these fundamentals.

## Where to go from here

- [Level 02](../02-analog-electronics/README.md) for sensors, amplifiers, and filters.
- [Level 03](../03-digital-electronics/README.md) if digital logic pulls harder.
- Back to [Level 00](../00-getting-started/README.md) to retrace any measurement habit you skipped.