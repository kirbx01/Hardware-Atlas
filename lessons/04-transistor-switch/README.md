# Lesson 4: Transistor Switch

## What you are building

An LED switched on and off by a BJT transistor, controlled by a small base current from a button, instead of the LED sitting directly in the button's current path like it did in Lesson 3. You're replacing the finger-operated mechanical switch with an electrically-operated one.

## What you will learn

- How an NPN bipolar junction transistor (BJT) works as a switch: base, collector, and emitter, and what "saturation" means in practice.
- Why the base-emitter junction behaves like a diode with a threshold voltage (about 0.6-0.7V for silicon), and what that means for base current.
- How to calculate a base resistor value so you drive the transistor into full saturation without exceeding its current ratings.
- Why this matters: a transistor lets a small, low-current signal (like a microcontroller's GPIO pin output in Level 4) control a much larger current or voltage than that signal could handle on its own.
- How to read a transistor's pinout from a datasheet, since it varies by package and manufacturer, and should never be assumed from memory alone.

## Prerequisites

[Lesson 1: LED Circuit](../01-led-circuit/README.md), [Lesson 2: Voltage Divider](../02-voltage-divider/README.md), and [Lesson 3: Button and LED](../03-button-and-led/README.md). This lesson directly replaces the mechanical switch from Lesson 3 with a transistor, so that context matters.

## Components required

- 1x NPN transistor, BC547 (or BC548, or 2N2222; any general-purpose NPN works, but pin order differs between packages, check the datasheet)
- 1x LED
- 1x resistor, 220-330 ohm (collector side, current limiting for the LED)
- 1x resistor, 1k ohm (base side, current limiting into the transistor)
- 1x pushbutton
- Breadboard, jumper wires
- 9V battery

## Tools required

- Digital multimeter, to measure Vbe and Vce as described below.

## Circuit explanation

A BJT has three terminals: base, collector, and emitter. In an NPN transistor used as a switch, current flows from collector to emitter, but only when a small current is also flowing into the base.

The base-emitter junction behaves like a diode: once the voltage across it (V_be) reaches roughly 0.6-0.7V, it starts conducting and a base current flows. That base current, even though it's small (often under 1mA for this kind of circuit), allows a much larger current to flow from collector to emitter, this is the amplification/switching behavior transistors are built around.

When enough base current flows, the transistor enters "saturation": it behaves close to a closed switch, with only a small voltage drop between collector and emitter (V_ce, typically 0.1-0.3V when saturated). When there's no base current, the transistor is "cut off," behaving close to an open switch, with close to the full supply voltage across collector-emitter.

To size the base resistor, you need to know roughly how much collector current you want (set by your LED and its own resistor, same as Lesson 1), and the transistor's current gain (h_FE, listed on the datasheet, often 100-800 depending on the specific part and conditions). A safe design rule is to supply more base current than the strict minimum needed for saturation, which is why base resistors are often chosen more conservatively than the theoretical minimum:

```
I_base_needed >= I_collector / h_FE
R_base = (V_control - V_be) / I_base
```

For a 5V control signal, V_be of 0.7V, and wanting roughly 1mA of base current (comfortably enough to saturate a transistor switching a small LED load):

```
R_base = (5 - 0.7) / 0.001 = 4300 ohms
```

A 1k resistor here delivers noticeably more base current than this minimum, which safely oversaturates the transistor. That's normal and intentional for a simple switch like this; you're not trying to run it as a precise amplifier.

## How to build it

1. Build the LED + resistor circuit exactly as in Lesson 1, but instead of connecting the resistor directly to ground, connect it to the transistor's collector.
2. Connect the transistor's emitter to ground.
3. Connect the transistor's base, through the 1k base resistor, to one side of the pushbutton.
4. Connect the other side of the pushbutton to your supply positive.
5. Double check the transistor's pinout against its datasheet before inserting it; BC547 in a standard TO-92 package has a specific pin order (check the flat face orientation) that is easy to get backwards.
6. Power the circuit. Pressing the button should light the LED, same visible behavior as Lesson 3, but now current for the LED is coming through the transistor, not through the button.

## What to measure or observe

- With the button pressed (transistor on), measure V_be (across base-emitter). It should read close to 0.6-0.7V.
- With the button pressed, measure V_ce (across collector-emitter). It should be low, well under 1V, confirming saturation.
- With the button released (transistor off), measure V_ce again. It should now read close to your full supply voltage, confirming the transistor is fully off.
- Try replacing the 1k base resistor with something much larger, like 100k, and observe the LED dim or fail to light at all, this is base current becoming too small to saturate the transistor.

## Common mistakes

- **Wrong pinout.** Base, collector, and emitter order is not the same across every transistor package, and is not something to guess. Always check the datasheet for your exact part.
- **Missing the base resistor.** Connecting the base directly to a voltage source without a resistor can push far more current through the base-emitter junction than it's rated for, destroying the transistor.
- **Confusing collector and emitter.** The circuit may partially work if swapped (some current gain still occurs), but performance will be poor and unpredictable. Get the orientation right from the datasheet, don't rely on trial and error.
- **Driving an inductive load (a motor or relay coil) directly from the collector without a flyback diode.** Not used in this lesson's LED circuit, but worth knowing before you extend this pattern to a motor: switching off an inductive load can generate a voltage spike that damages the transistor unless a diode is placed across the load to absorb it.
- **Forgetting the load resistor**, i.e. treating this like Lesson 3 and wiring the LED with no current-limiting resistor at all, just because the transistor is doing something new. The LED still needs the same protection it always did.

## Useful resources

- SparkFun, Transistors: https://learn.sparkfun.com/tutorials/transistors
- BC546/BC547/BC548 datasheet (onsemi, official): https://www.onsemi.com/pdf/datasheet/bc546-d.pdf
- PrepFusion, Analog Electronics / BJT biasing and switching lecture series: https://www.youtube.com/@PrepFusion_GATE
- Falstad circuit simulator, useful for testing base resistor values before building: https://www.falstad.com/circuit/

## What to build next

Move to [Lesson 5: RC Circuit](../05-rc-circuit/README.md). You now have both a switch (Lesson 3) and an electrically-controlled switch (this lesson). The next step introduces the one component you haven't used yet, the capacitor, and combines it with the transistor here to build your first circuit with real timing behavior.
