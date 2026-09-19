# Analog Electronics Level 02 -- Op-Amp Stages

Same signal chain, better clothes: an op-amp conditions a weak sensor signal with two resistors, and a capacitor in the feedback path turns that stage into a frequency-selective filter. No fiddly per-transistor bias tuning.

## Lessons

| # | Lesson | What it builds | Status |
|---|---|---|---|
| 08 | [Op-amp signal conditioner](../../../../lessons/08-op-amp-conditioner/README.md) | Feedback and supply limits | ✅ |
| 09 | [Active filter](../../../../lessons/09-active-filter/README.md) | Cutoff frequency and measured response | ✅ |

## Why feedback is the point

Gain is set by resistors, not by the part. The rails still cap everything: an amplifier that "should" give 10x giving 6x is information about headroom, not a broken circuit.

## Where to go from here

- [Domain 03 -- Digital Electronics](../../../03-digital-electronics/README.md) once clean analog edges start feeding logic chips.
- Back to [Domain 02 overview](../../README.md).