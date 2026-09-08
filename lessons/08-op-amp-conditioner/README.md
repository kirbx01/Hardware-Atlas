# Lesson 8: Op-Amp Signal Conditioner

## What you are building

A non-inverting op-amp amplifier for the LDR signal, with a selectable gain.

## What you will learn

Feedback, gain setting, input common-mode limits, output swing, decoupling, and the difference between an amplifier and a comparator.

## Prerequisites

[Light Sensor](../06-light-sensor/README.md) and [Transistor Amplifier](../07-transistor-amplifier/README.md).

## Components and tools

- Rail-to-rail single-supply op amp suitable for your supply voltage
- 10k ohm and 100k ohm resistors
- 100nF decoupling capacitor
- LDR divider from Lesson 6
- Breadboard, jumpers, 3.3V or 5V supply, multimeter

## Software

Use [Falstad](https://www.falstad.com/circuit/) to check the gain before wiring.

## Build

Connect the LDR divider to the non-inverting input. Set the non-inverting gain with a resistor from output to inverting input and another from inverting input to ground. Start with gain 2: equal-value resistors give `1 + Rf/Rg = 2`.

## Test

Measure the input and output at darkness, room light, and bright light. Confirm the output stays inside the op amp supply range. Add the 100nF capacitor close to the supply pins.

## Common mistakes

An op amp is not automatically safe at any input voltage or supply. Read the input common-mode and output swing specifications in its datasheet.

## Resources

- [Texas Instruments op-amp basics](https://www.ti.com/lit/an/slod006b/slod006b.pdf)
- [Analog Devices op-amp applications](https://www.analog.com/en/technical-articles/op-amp-applications.html)

## What to build next

[Lesson 9: Active Filter](../09-active-filter/README.md).
