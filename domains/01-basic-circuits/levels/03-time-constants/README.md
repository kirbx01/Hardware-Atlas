# Basic Circuits Level 03 -- Time Constants

One idea isolated: a capacitor resists sudden changes in voltage, and the RC product sets how quickly charge and discharge happen. Everything from switch debounce to active filters depends on this single curve.

## Lessons

| # | Lesson | What it builds | Status |
|---|---|---|---|
| 05 | [RC circuit](../../../../lessons/05-rc-circuit/README.md) | Time constants and charge/discharge curves | ✅ |

## Why it matters

The same $\tau = RC$ reappears as debounce delays, low-pass filter cutoffs, and pairs of timing rules in every later domain. Read τ as the time to reach ~63% — the most common mistake is reading it as "full charge" time.

## Where to go from here

- [Domain 02 -- Analog Electronics](../../../02-analog-electronics/README.md) turns this curve into filters and amplifiers.
- Back to [Domain 01 overview](../../README.md).