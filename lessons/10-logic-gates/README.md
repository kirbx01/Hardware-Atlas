# Lesson 10: Logic Gates

## What you are building

Truth tables using a 74HC00 NAND or 74HC08 AND gate IC, LEDs, switches, and defined input states.

## What you will learn

Boolean logic, CMOS voltage levels, pull resistors, propagation delay, decoupling, and why inputs must not float.

## Prerequisites

Level 1 switch circuits and basic binary notation.

## Components and tools

- 1x 74HC00 or 74HC08, verify the exact datasheet
- LEDs and 1k ohm resistors
- 10k ohm resistors for pull-ups or pull-downs
- Pushbuttons, 100nF capacitor, breadboard, wires, 5V supply, multimeter

## Software

Use [Tinkercad Circuits](https://www.tinkercad.com/circuits) or [Wokwi](https://wokwi.com/) to check the truth table.

## Build

Connect the IC ground and supply first, add the 100nF capacitor close to the IC, then connect each unused input to a defined logic level. Wire two switches to the gate inputs and an LED through a resistor to the output.

## Test

Write the expected truth table before pressing buttons. Check all input combinations and measure logic-low and logic-high voltage. Never leave a CMOS input disconnected.

## Resources

- [Texas Instruments SN74HC00 datasheet](https://www.ti.com/lit/ds/symlink/sn74hc00.pdf)
- [SparkFun logic levels](https://learn.sparkfun.com/tutorials/logic-levels)

## What to build next

[Lesson 11: Flip-Flop and Counter](../11-flip-flop-counter/README.md).
