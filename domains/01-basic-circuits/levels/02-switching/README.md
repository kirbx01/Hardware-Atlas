# Basic Circuits Level 02 -- Switching

Controlling current with a mechanical button and then with a transistor. Both build the same habit: never leave a digital input floating, and size the base resistor on purpose.

## Lessons

| # | Lesson | What it builds | Status |
|---|---|---|---|
| 03 | [Button and LED](../../../../lessons/03-button-and-led/README.md) | Switches, pull-ups, defined logic states | ✅ |
| 04 | [Transistor switch](../../../../lessons/04-transistor-switch/README.md) | Low-side switching with a sized base resistor | ✅ |

## Why these two next

Every microcontroller domain after this one reads buttons and drives loads. A floating input behaves like a random number; the pull-up is the cure, and it is easier to learn here than while debugging I2C later.

## Where to go from here

- [Basic Circuits Level 03 -- Time Constants](../03-time-constants/README.md) to see what a capacitor does to a switching signal.
- Back to [Domain 01 overview](../../README.md).