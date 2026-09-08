# Lesson 1: LED Circuit

## What you are building

A single LED lit up safely by a battery, using a resistor to protect it. This is the smallest complete circuit that teaches you the four ideas everything else in electronics is built on: voltage, current, resistance, and Ohm's law.

## What you will learn

- What voltage, current, and resistance actually mean, not just as words but as things you can predict with a formula.
- Ohm's law (`V = I x R`) and how to use it to pick a resistor value instead of guessing.
- Why an LED needs a current-limiting resistor in series with it, and what happens if you skip it.
- LED polarity: why it only lights up one way around, and how to tell anode from cathode by looking at it.
- How to read a resistor's value from its color bands.
- Basic breadboard wiring: how the rows and rails are connected internally.

## Prerequisites

None. This is the starting point.

## Components required

- 1x LED (5mm, any color; red and green have the lowest forward voltage and are the most forgiving to start with)
- 1x resistor, 220 ohm to 330 ohm (330 ohm is the standard safe default for a 9V or two AA battery supply)
- 1x breadboard
- 2-3x jumper wires
- 1x power source: either a 9V battery with a snap connector, or a 2xAA battery holder (3V)

## Tools required

None strictly required for this lesson, though if you already have a multimeter, bring it, you'll use it in "What to measure."

## Circuit explanation

An LED is a diode: current can only flow through it in one direction, from the anode (positive leg, usually the longer one) to the cathode (negative leg, usually the shorter one, next to a flat edge on the LED's plastic body).

An LED also has a forward voltage (V_f), the voltage it "uses up" once it's conducting. A typical red LED has V_f around 1.8-2.2V. This isn't optional or adjustable, it's a property of the semiconductor junction inside the LED.

If you connected an LED directly across a battery with nothing else in the circuit, the LED would try to draw far more current than it's rated for, because its resistance drops sharply once it starts conducting. That extra current shows up as heat, and the LED burns out, sometimes instantly. This is why every LED circuit needs a resistor in series to limit current to a safe value, usually somewhere in the 10-20 mA range for a standard 5mm LED.

The resistor value comes straight from Ohm's law. The battery's voltage gets split between the resistor and the LED. The part left over for the resistor is:

```
V_resistor = V_supply - V_f
```

And from Ohm's law, the resistor needed to get a target current `I` is:

```
R = V_resistor / I = (V_supply - V_f) / I
```

For a 9V battery, a red LED (V_f ~ 2V), and a target current of 15mA (0.015A):

```
R = (9 - 2) / 0.015 = 467 ohms
```

330 ohm is a common standard value that gives a bit more current than this (brighter, still safe) and is what most kits include, which is why it's the usual recommendation.

## How to build it

1. Insert the LED into the breadboard so its two legs are in different rows (not the same row, or you'll short it).
2. Insert the resistor so one end shares a row with the LED's anode (longer leg), and the other end is free.
3. Connect a jumper wire from the resistor's free end to the battery's positive terminal (via the breadboard's positive rail if you're using it).
4. Connect a jumper wire from the LED's cathode (shorter leg, flat-edge side) to the battery's negative terminal / ground rail.
5. Connect the battery. The LED should light immediately.
6. If it doesn't light, don't assume it's broken. Flip the LED around first, it's the single most common mistake at this stage.

## What to measure or observe

If you have a multimeter:

- Measure the voltage across the LED alone (probe its two legs). It should read close to its rated forward voltage (~1.8-2.2V for red).
- Measure the voltage across the resistor alone. It should be roughly `V_supply - V_LED`.
- Using the resistor's measured voltage and its labeled value, calculate the current with Ohm's law (`I = V/R`) and compare it to what you were targeting.
- Try swapping in a different resistor value (say, 1k ohm instead of 330 ohm) and observe that the LED gets noticeably dimmer. This is you directly seeing current control brightness.

If you don't have a multimeter yet, at minimum observe: the LED lights when correctly oriented, and does not light (but is undamaged) when reversed, since the diode simply blocks current in that direction.

## Common mistakes

- **LED inserted backwards.** It won't be damaged, it just won't light. Flip it.
- **No resistor at all.** The LED may briefly light very brightly, then dim permanently or die outright as internal damage accumulates. Never skip the resistor, even "just to test."
- **Both LED legs in the same breadboard row.** This shorts the LED and prevents current from ever reaching it properly.
- **Resistor value far too low** (say, 10 ohm instead of 330 ohm) still lets through too much current for the LED's rating, especially with a 9V supply. When in doubt, start with a slightly higher resistor value; you can always go lower if it's too dim.
- **Loose breadboard connections.** LEDs and resistor legs that aren't pushed in fully lead to an intermittent circuit that looks like a bad component but isn't.

## Useful resources

- SparkFun, Light-Emitting Diodes (LEDs): https://learn.sparkfun.com/tutorials/light-emitting-diodes-leds
- SparkFun, Resistors (color codes and how to pick a value): https://learn.sparkfun.com/tutorials/resistors
- SparkFun, Diodes (the general theory an LED is a special case of): https://learn.sparkfun.com/tutorials/diodes
- DigiKey resistor color code calculator: https://www.digikey.com/en/resources/conversion-calculators/conversion-calculator-resistor-color-code
- Falstad circuit simulator, to test resistor values on a virtual LED circuit before you build: https://www.falstad.com/circuit/

## What to build next

Move to [Lesson 2: Voltage Divider](../02-voltage-divider/README.md). You already understand Ohm's law and a single resistor's effect on current; the next step is what happens with two resistors in series and how that lets you create any voltage you want from a fixed supply.
