# Lesson 3: Button and LED

## What you are building

Three variations of a switch-controlled LED circuit: a single button turning an LED on and off, two buttons wired so that either one lights the LED (OR), and two buttons wired so that both must be pressed together to light it (AND). You're building hardware logic gates out of nothing but mechanical switches.

## What you will learn

- How a momentary pushbutton works, and the difference between normally-open (NO) and normally-closed (NC) switches.
- Why parallel switch paths implement OR logic, and series switch paths implement AND logic, as a direct consequence of how current finds a path.
- Contact bounce: why a real mechanical switch doesn't produce one, clean voltage transition, and why this matters more once you're reading buttons electronically (a preview of what Level 4, Microcontrollers, will deal with directly).
- How to build and read a truth table from a physical circuit instead of just a textbook.

## Prerequisites

[Lesson 1: LED Circuit](../01-led-circuit/README.md) and [Lesson 2: Voltage Divider](../02-voltage-divider/README.md). You need to be comfortable with series and parallel current paths from Lesson 2 before this will click.

## Components required

- 2x momentary pushbuttons (normally-open, 4-pin tactile type is fine)
- 1x LED
- 1x resistor, 220-330 ohm
- Breadboard, jumper wires
- 9V battery or 2xAA holder

## Tools required

- Multimeter, set to continuity/beep mode, to verify each switch and each build before powering it.

## Circuit explanation

A pushbutton is just a mechanical way of opening or closing a gap in a circuit. A normally-open (NO) button has no connection between its two sides until you press it; a normally-closed (NC) button is the opposite. Most tactile buttons sold for breadboarding are NO, and that's what this lesson uses. On a standard 4-pin tactile button, pins are internally joined in pairs across the button (two pins on one side are always connected to each other, two on the other side are always connected to each other), and pressing the button joins the two sides. Always check the datasheet or test with continuity mode before assuming which pins do what.

**Single switch:** the button sits in series with the LED and resistor. Current can only complete the loop when the button is pressed. This is the simplest possible circuit and behaves exactly like a manual version of Lesson 1's circuit with an on/off control added.

**Two switches in parallel (OR):** put button A and button B side by side, each providing its own independent path from supply to the LED's series resistor. If either button is pressed, current has a path through; it doesn't matter if the other is also pressed. This is an OR gate: `LED = A OR B`.

**Two switches in series (AND):** put button A and button B one after another in the same current path. Current can only complete the loop if both are pressed at once, because a single open switch anywhere in a series path blocks the whole path. This is an AND gate: `LED = A AND B`.

This is the same principle behind how actual logic gate ICs work internally (with transistors instead of mechanical switches), and it's the physical intuition Level 3 (Digital Electronics) builds on when it introduces Boolean algebra and IC logic gates properly.

## How to build it

**Single switch**
1. Wire the LED and resistor in series as in Lesson 1, but insert the pushbutton between the resistor and the supply rail instead of connecting directly.
2. Confirm the LED only lights while the button is held down.

**OR (parallel)**
1. Keep the LED and resistor in series, feeding into a shared node.
2. Run separate wires from that node through button A to the supply rail, and through button B to the same supply rail, in parallel.
3. Press each button individually, then both together, and confirm the LED lights in all three cases.

**AND (series)**
1. Keep the LED and resistor in series.
2. Wire button A and button B one after another, in series, between the LED's series resistor and the supply rail.
3. Press only A, only B, then both, and confirm the LED only lights when both are pressed simultaneously.

## What to measure or observe

- Before wiring each configuration, test each button individually in continuity mode: probe across it, confirm no beep when unpressed, a beep when pressed.
- For each of the three configurations, press every combination of the two buttons (neither, A only, B only, both) and record whether the LED is on or off. You'll end up with a 4-row truth table for each circuit, matching the standard AND/OR truth tables.
- If you have a multimeter with a fast enough display, briefly hold a probe across a bouncing switch's contacts while pressing it slowly; on some meters you can catch the reading flicker during the bounce.

## Common mistakes

- **Confusing NO and NC buttons**, or misreading which pins are internally linked, leading to a circuit that behaves backwards from what you expect. Test with continuity mode first, every time.
- **Bridging unrelated breadboard rows** when wiring parallel or series switch paths; it's easy to accidentally short both switch paths together if your wiring isn't deliberate about which rows are used for what.
- **Assuming "series" and "parallel" only apply to resistors.** They apply to any two-terminal component, including switches; the logic is identical to what you saw with resistors in Lesson 2.
- **Not accounting for bounce** if you ever try to count button presses electronically later; a single "press" can register as several rapid on/off transitions at the electrical level, which is why debouncing exists as a real topic in both hardware and firmware.

## Useful resources

- SparkFun, Button and Switch Basics: https://learn.sparkfun.com/tutorials/button-and-switch-basics
- SparkFun, Pull-up Resistors (forward reference for when you connect a button to a microcontroller input in Level 4, where a floating pin becomes a real problem): https://learn.sparkfun.com/tutorials/pull-up-resistors
- Gate Smashers, Digital Logic playlist (forward reference for Level 3, where AND/OR/NOT get formalized with Boolean algebra and built from ICs): https://www.youtube.com/@GateSmashers

## What to build next

Move to [Lesson 4: Transistor Switch](../04-transistor-switch/README.md). A mechanical switch needs a finger to operate it. A transistor lets a small electrical signal do the same job, which is the step that makes it possible for a circuit to switch itself.
