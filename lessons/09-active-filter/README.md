# Lesson 9: Active Filter

## What you are building

A first-order active low-pass filter that amplifies slow changes and attenuates faster ones.

## What you will learn

Cutoff frequency, frequency response, gain-bandwidth limits, and how measured circuits differ from ideal transfer functions.

## Prerequisites

[RC Circuit](../05-rc-circuit/README.md) and [Op-Amp Signal Conditioner](../08-op-amp-conditioner/README.md).

## Components and tools

- Suitable single-supply op amp
- 10k ohm resistor and 100nF capacitor for an approximately 159Hz RC corner
- 2x 10k ohm resistors and 10uF capacitor to make a 2.5V mid-supply reference
- Feedback resistors for unity or modest gain
- Breadboard, 5V supply, multimeter, and signal generator or Wokwi/Falstad equivalent

## Build

Make a mid-supply reference with the two 10k resistors, bypass it with the 10uF capacitor, and use that reference as the circuit's signal return. Drive the filter with a signal centred around the same reference, or AC-couple the source into the filter node and bias that node to the reference. Put the 10k filter resistor in series with the input and the 100nF capacitor from the op-amp input node to the mid-supply reference. Buffer or amplify that node with the op amp. Keep the first test at low amplitude so the output cannot clip or fall below ground.

## Test

Apply a small sine wave centred around the mid-supply reference at roughly 10Hz, 100Hz, 160Hz, 1kHz, and 10kHz. Record output amplitude relative to the reference and calculate gain. The cutoff is where the AC amplitude is about 0.707 of its passband value.

## Resources

- [Analog Devices, MT-220 filters](https://www.analog.com/media/en/training-seminars/tutorials/MT-220.pdf)
- [Falstad Circuit Simulator](https://www.falstad.com/circuit/)

## What to build next

[Level 3: Logic Gates](../10-logic-gates/README.md).
