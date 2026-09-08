# Lesson 5: RC Circuit

## What you are building

Two circuits: first, a plain resistor-capacitor (RC) network where you measure the capacitor's voltage over time as it charges and discharges, to see the RC time constant with your own numbers instead of just a formula. Second, a capacitor combined with the transistor switch from Lesson 4 to build an LED that fades out gradually after you release a button, instead of switching off instantly.

## What you will learn

- What a capacitor is and how it stores charge, in contrast to a resistor, which simply dissipates energy.
- The RC time constant (`tau = R x C`) and what it physically means: the time for the capacitor's voltage to reach about 63% of its target value while charging, or fall to about 37% of its starting value while discharging.
- Why charging and discharging are exponential, not linear, and the practical "5 time constant" rule for when a capacitor is considered fully charged or discharged.
- How to combine a capacitor with a transistor to build simple timing behavior without a microcontroller or a dedicated timer IC, and develop intuition for what circuits like the 555 timer do internally.

## Prerequisites

[Lesson 1: LED Circuit](../01-led-circuit/README.md), [Lesson 2: Voltage Divider](../02-voltage-divider/README.md), and [Lesson 4: Transistor Switch](../04-transistor-switch/README.md). The second circuit in this lesson directly extends Lesson 4's transistor switch.

## Components required

- 1x electrolytic capacitor, 100-470uF
- The capacitor should be rated for at least 16V when using a 9V battery
- 1x resistor, 10k-100k ohm (larger values make the timing slow enough to watch and time by hand)
- 1x NPN transistor (same as Lesson 4, e.g. BC547)
- 1x LED
- 1x resistor, 220-330 ohm (LED current limiting)
- 1x resistor, 1k ohm (transistor base, same as Lesson 4)
- 1x pushbutton
- Breadboard, jumper wires
- 9V battery

## Tools required

- Digital multimeter, with a stopwatch or phone timer alongside it, since this lesson is about voltage changing over time.

## Circuit explanation

A capacitor stores electrical charge on two conductive plates separated by an insulator. Unlike a resistor, which converts electrical energy to heat continuously, a capacitor holds energy and releases it later. Its behavior is described by `Q = C x V`, charge stored equals capacitance times voltage across it.

When you connect a capacitor to a supply through a resistor, the resistor limits how fast current can flow to charge the capacitor. The voltage across the capacitor doesn't jump instantly to the supply voltage, it rises exponentially, fast at first, then slower as it approaches the target. The rate is described by the time constant:

```
tau = R * C
```

`tau` is measured in seconds when R is in ohms and C is in farads. After one time constant, the capacitor has reached about 63.2% of its final voltage. After roughly five time constants (5 x tau), it's considered fully charged for practical purposes, over 99% of the way there. Discharging follows the same shape in reverse: after one time constant, the voltage has fallen to about 36.8% of where it started.

For a 100k ohm resistor and a 470uF capacitor:

```
tau = 100,000 * 0.00047 = 47 seconds
```

That's slow enough to time with a stopwatch, which is exactly why this lesson recommends resistor values in that range rather than something that charges in milliseconds.

**The fade-off circuit** combines this with Lesson 4's transistor: instead of the button feeding the base resistor directly, it charges a capacitor connected between the transistor base and ground. While the button is held, the capacitor charges and the transistor saturates normally, lighting the LED fully. When the button is released, the capacitor discharges through the transistor's base-emitter path and other leakage paths. The base voltage falls nonlinearly, so the transistor conducts less and the LED may fade rather than switch off instantly. This demonstrates stored charge controlling timing, but it is not a precise RC timer. A 555 timer or a microcontroller gives more predictable timing.

## How to build it

**Part A: Charge/discharge measurement**
1. Connect the resistor in series with the capacitor across your battery. Connect the capacitor's negative leg to ground and check the polarity markings before applying power.
2. Connect the multimeter across the capacitor only, set to DC voltage.
3. Connect the battery and immediately start your stopwatch. Record the voltage reading every 5-10 seconds until it stops changing.
4. Disconnect the battery. Move the series resistor so it sits directly across the capacitor, or use a second resistor of the same value, to provide a controlled discharge path. Do not short a charged capacitor directly with a wire. Time the voltage falling in the same way.

**Part B: Transistor fade-off**
1. Build the transistor + LED circuit from Lesson 4 exactly as before.
2. Add the capacitor between the transistor's base and ground (in parallel with the base-emitter junction), keeping the base resistor and pushbutton wired the same way as Lesson 4.
3. Press and hold the button; the LED should light fully, same as before.
4. Release the button and watch the LED fade rather than switching off instantly.
5. Try a larger capacitor value and observe the fade taking noticeably longer.

## What to measure or observe

- For Part A, plot (even just on paper) voltage against time for both charging and discharging, and mark the point where the voltage crosses 63% (charging) or 37% (discharging) of the total range. Compare that time to your calculated `tau = R x C`.
- For Part A, confirm that after roughly 5 x tau, the voltage has essentially stopped changing.
- For Part B, compare the fade with two capacitor values and record the result as an observation, not a precise timing law. The transistor's base-emitter junction makes this discharge nonlinear, so doubling the capacitance will not necessarily double the visible fade time.

## Common mistakes

- **Electrolytic capacitor polarity reversed.** Electrolytic capacitors are polarized (unlike ceramic ones) and connecting one backwards can damage it or, at higher voltages, cause it to vent or fail. Always check the marked negative stripe against your ground connection.
- **Resistor value too small.** With a small resistor, charging happens in well under a second, too fast to time by hand. Start with values in the 10k-100k range for this lesson specifically.
- **Multimeter loading the circuit.** At very high resistor values (megaohms), a multimeter's own input resistance can slightly affect your readings. Not usually significant at the values used here, but worth knowing as you go to more sensitive circuits later.
- **Not letting the capacitor fully discharge between repeated tests.** If you start a new charging test with residual charge still on the capacitor, your curve won't match the calculated one, since it isn't starting from zero.
- **Expecting a perfectly linear fade in Part B.** The fade follows the same exponential shape as any RC discharge; it will look faster at the start and slower near the end, not constant.

## Useful resources

- SparkFun, Capacitors: https://learn.sparkfun.com/tutorials/capacitors
- Electronics Tutorials, RC Charging Circuit and Time Constant: https://www.electronics-tutorials.ws/rc/rc_1.html
- Electronics Tutorials, RC Discharging Circuit: https://www.electronics-tutorials.ws/rc/rc_2.html
- PrepFusion, Network Theory series (starts from KVL/KCL and builds up to RC circuit analysis in depth): https://www.youtube.com/@PrepFusion_GATE
- Falstad circuit simulator, good for watching an RC charge curve animate in real time before or after building it physically: https://www.falstad.com/circuit/

## What's next

This closes out the first five lessons of the roadmap. The next project is [Lesson 6: Light Sensor](../06-light-sensor/README.md), which reuses the voltage-divider idea to turn light into a measured signal.

The later route is [Level 2: Analog Electronics](../../levels/02-analog/README.md), followed by [Level 3: Digital Electronics](../../levels/03-digital/README.md), [Level 4: Microcontrollers](../../levels/04-microcontrollers/README.md), and [Level 5: Embedded Systems](../../levels/05-embedded/README.md). Those levels now have detailed lessons of their own.
