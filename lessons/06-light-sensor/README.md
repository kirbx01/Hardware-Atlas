# Lesson 6: Light Sensor

## What you are building

An LDR voltage divider whose output changes with light, measured with a multimeter.

## What you will learn

How a sensor becomes a voltage, why the response is not perfectly linear, and how divider loading affects a measurement.

## Prerequisites

[Voltage Divider](../02-voltage-divider/README.md).

## Components and tools

- 1x LDR
- 1x 10k ohm resistor
- Breadboard and jumper wires
- 3.3V or 5V supply
- Digital multimeter

## Software

None. Use [Falstad](https://www.falstad.com/circuit/) if you want to vary the divider values first.

## Build

Place the LDR and 10k resistor in series between the supply and ground. Measure the midpoint relative to ground. Cover the LDR, expose it to a lamp, and record the voltage each time. Swap the LDR and fixed resistor if you want the voltage to move in the opposite direction.

## Test

Record supply voltage, light condition, midpoint voltage, and the calculated resistance. Do not call the result a lux measurement without calibration and a specified LDR.

## Common mistakes

Do not measure current by placing the meter across the divider. Keep the meter on voltage mode and connect it in parallel.

## Resources

- [SparkFun voltage dividers](https://learn.sparkfun.com/tutorials/voltage-dividers)
- [Circuit Digest LDR tutorial](https://circuitdigest.com/electronic-circuits/ldr-circuit-diagram)

## What to build next

[Lesson 7: Transistor Amplifier](../07-transistor-amplifier/README.md).
