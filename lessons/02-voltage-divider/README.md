# Lesson 2: Voltage Divider

## What you are building

Three small circuits using two resistors in series: a fixed voltage divider you calculate and verify, an adjustable one using a potentiometer, and a light-sensitive one using a photoresistor (LDR). None of these light up an LED by themselves; the point of this lesson is learning to produce and measure a controlled voltage, which is the foundation for how sensors talk to circuits later on.

## What you will learn

- How two resistors in series split a supply voltage between them, and the voltage divider equation.
- Why a voltage divider should never be used to power a load directly (it can, but it shouldn't, and you'll see why).
- How to use a potentiometer as a manually adjustable divider.
- How a resistive sensor like a photoresistor (LDR) can be turned into a voltage that changes with a physical quantity (light, in this case), which is exactly how most analog sensors work.
- How to correctly place multimeter probes to measure voltage (in parallel, not in series).

## Prerequisites

[Lesson 1: LED Circuit](../01-led-circuit/README.md), specifically Ohm's law and comfort with a breadboard.

## Components required

- 2x resistors of different values (10k ohm and 10k ohm to start; then try 1k and 2k, or whatever you have)
- 1x potentiometer, 10k ohm
- 1x photoresistor (LDR)
- 1x fixed resistor to pair with the LDR (10k ohm works as a starting point)
- Breadboard, jumper wires
- 9V battery or similar DC supply

## Tools required

- Digital multimeter. This lesson is where a multimeter stops being optional. You cannot verify a divider's output by eye.

## Circuit explanation

A voltage divider is two resistors in series across a supply voltage, with the output taken from the point between them.

Call the resistor closest to the supply `R1`, and the one closest to ground `R2`. The voltage across `R2` is your divided output, `V_out`:

```
V_out = V_in * ( R2 / (R1 + R2) )
```

This works because the same current flows through both resistors (they're in series, current has nowhere else to go), and each resistor's voltage drop is proportional to its resistance. Make `R2` bigger relative to `R1`, and more of the total voltage appears across it.

**Why dividers shouldn't power a load directly:** the equation above assumes nothing is drawing current from the output point except the two resistors themselves. The moment you connect a load (an LED, a motor, another circuit) across `R2`, that load also draws current, which changes the current balance and pulls `V_out` down from what the formula predicts. This is called "loading" the divider. For high-impedance loads (like a microcontroller's analog input, which draws almost no current) this effect is negligible. For anything that draws real current, it's significant, and you should use something like a transistor (Lesson 4) instead of a divider to actually deliver power.

A potentiometer is just a variable divider: it's a single resistive element with a wiper that slides along it, so moving the wiper changes the ratio between the two "halves" the same way swapping R1 and R2 values would.

A photoresistor's resistance changes with light: it's typically very high in the dark (hundreds of kilo-ohms) and much lower in bright light (a few hundred ohms to a few kilo-ohms). Pair it with a fixed resistor as a divider, and the output voltage swings with the light level, this is the standard way a "simple" analog light sensor works, before you ever add a microcontroller.

## How to build it

**Part A: Fixed divider**
1. Place two 10k resistors in series on the breadboard (one end of the first touching one end of the second).
2. Connect the free end of the first resistor to your supply positive.
3. Connect the free end of the second resistor to ground.
4. The junction between them is `V_out`. Measure it with the multimeter (black probe to ground, red probe to the junction).

**Part B: Potentiometer**
1. Connect the potentiometer's two outer pins to supply positive and ground.
2. The middle pin (wiper) is your `V_out`. Measure it while turning the knob and watch the reading change continuously.

**Part C: LDR divider**
1. Put the LDR and a fixed 10k resistor in series, same layout as Part A.
2. Measure the voltage at the junction with the room lights on, then cover the LDR with your hand or a finger and measure again.
3. Note which side of the divider you put the LDR on. Depending on the order, the output voltage will rise or fall as light decreases; work out from the equation which arrangement gives you which behavior.

## What to measure or observe

- For Part A: calculate `V_out` from the equation before measuring, then compare it to what the multimeter shows. They should be close (small differences come from resistor tolerance, usually +/-5%).
- For Part A: try at least three different R1/R2 pairs and confirm the ratio, not the absolute resistor values, is what determines `V_out`.
- For Part B: confirm the output ranges from near 0V to near your supply voltage as you turn the potentiometer fully in each direction.
- For Part C: record the voltage in normal light and covered, and calculate the LDR's approximate resistance in each case using the divider equation solved for the unknown resistor.

## Common mistakes

- **Swapping R1 and R2 in the formula.** Always double check which resistor is actually closest to the supply versus closest to ground in your physical circuit before comparing to the calculation.
- **Measuring voltage with probes in series instead of parallel.** A multimeter set to measure voltage must be placed across two points, never inserted into the current path.
- **Forgetting a common ground reference.** All your voltage measurements are relative to the black probe's position; if it's not on your circuit's ground, your readings won't make sense.
- **Using very low resistor values (under ~100 ohm) for a divider you're just measuring.** This draws unnecessarily high current from the battery for no benefit at this stage.
- **Expecting the LDR divider to power an LED directly.** It won't reliably; this is a measurement circuit, not a driver circuit. That comes in Lesson 4.

## Useful resources

- SparkFun, Voltage Dividers: https://learn.sparkfun.com/tutorials/voltage-dividers
- SparkFun, Resistors: https://learn.sparkfun.com/tutorials/resistors
- DigiKey resistor color code calculator: https://www.digikey.com/en/resources/conversion-calculators/conversion-calculator-resistor-color-code

## What to build next

Move to [Lesson 3: Button and LED](../03-button-and-led/README.md). You now understand how series and parallel resistance affects voltage and current; the next lesson uses that same series/parallel intuition, but with switches instead of resistors, to build your first hardware logic.
