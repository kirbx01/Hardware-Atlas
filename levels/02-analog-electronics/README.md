# Level 02 -- Analog Electronics

Bias, gain, loading, clipping, noise, and bandwidth. This is where ideal circuit models start showing their limits.

> [!TIP]
> Keep the meter on the bench for this whole level. An amplifier that "should" give 10x gain giving 6x is information, not failure.

## What this level covers

- Turning a physical quantity into a measurable voltage
- BJT small-signal amplification: bias, gain, and clipping
- Op-amp feedback, and the rails the output actually lives between
- First-order active filters: cutoff frequency and the response you measure

## Lessons

| # | Lesson | What it builds |
|---|---|---|
| 06 | [Light sensor](../../lessons/06-light-sensor/README.md) | Light into a measurable voltage |
| 07 | [Transistor amplifier](../../lessons/07-transistor-amplifier/README.md) | Bias, gain, clipping |
| 08 | [Op-amp signal conditioner](../../lessons/08-op-amp-conditioner/README.md) | Feedback and supply limits |
| 09 | [Active filter](../../lessons/09-active-filter/README.md) | Cutoff frequency and measured response |

## Signal chain

```mermaid
flowchart LR
    S[Sensor] --> C[Signal conditioner] --> F[Active filter] --> V[Measured output]
```

## Common mistakes

- Driving an op-amp output into a rail and calling the resulting flat line "gain"
- Measuring gain at one frequency and assuming it holds everywhere
- Forgetting that your meter probe itself loads a high-impedance node
- Diagnosing a part as broken when the circuit is simply biased wrong

## Where to go from here

- [Level 03](../03-digital-electronics/README.md) if you want logic next.
- [Level 06](../06-pcb-design/README.md) once you want an analog circuit that stops being a pile of jumper wires.

## Resources

- [Simulation](../../resources/simulation.md) is worth more here than anywhere else in the early levels.
- [Tools](../../resources/tools.md) if an oscilloscope is one of the purchases you are planning.