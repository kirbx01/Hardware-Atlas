# Lesson 7: Transistor Amplifier

## What you are building

A small-signal common-emitter amplifier using an NPN transistor and a bias network.

## What you will learn

Bias point, gain, saturation, cutoff, loading, and why an amplifier needs a stable operating point before an input signal is applied.

## Prerequisites

[Transistor Switch](../04-transistor-switch/README.md), [Voltage Divider](../02-voltage-divider/README.md), and basic KCL/KVL.

## Components and tools

- 1x BC547 or 2N3904, use the exact datasheet pinout
- 2x 10k ohm resistors for a bias divider
- 1x 1k ohm collector resistor
- 1x 1k ohm emitter resistor
- 2x 10uF capacitors for input and output coupling
- Breadboard, jumpers, 5V supply, multimeter
- Oscilloscope or USB audio source optional

## Build

Use the equal 10k bias divider to set the base near 2.5V on a 5V supply. The transistor and emitter resistor load the divider, so the measured base voltage will be somewhat lower, around 2.4V in this example. Put the collector resistor to 5V and emitter resistor to ground. Couple an input signal into the base through a capacitor and observe the collector through another capacitor. Start with a few tens of millivolts.

## Test

Before applying a signal, measure base, emitter, and collector DC voltages. Then increase the input slowly and observe gain and clipping. A large collector signal that hits either rail means the bias or input amplitude needs adjustment.

## Common mistakes

Transistor pinouts differ between packages and manufacturers. Do not trust the flat side alone. Check the datasheet for the exact part.

## Resources

- [All About Circuits, BJT amplifier](https://www.allaboutcircuits.com/textbook/experiments/chpt-4/common-emitter-amplifier/)
- [Nexperia BC547 datasheet](https://assets.nexperia.com/documents/data-sheet/BC546_BC547_BC548.pdf)

## What to build next

[Lesson 8: Op-Amp Signal Conditioner](../08-op-amp-conditioner/README.md).
