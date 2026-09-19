# FPGA and RTL Level 02 -- Verification

Making the check automatic. A cocotb testbench drives the RTL, asserts on it, and runs every time — so "verified" means the testbench agreed, not that you looked at one waveform once.

## Lessons

| # | Lesson | What it builds | Status |
|---|---|---|---|
| 25 | [cocotb Python testbench](../../../../lessons/25-cocotb-python-testbench/README.md) | Automate RTL verification | ✅ |

## Why verification is its own level

Running a testbench once, seeing green, and calling it verified is the failure mode this entire domain exists to prevent. The discipline transfers straight into the Computer Architecture and ASIC domains: the datapath and the GDSII both need the same skeptical checking.

## Where to go from here

- [Domain 09 -- Computer Architecture](../../../09-computer-architecture/README.md) builds a RISC-V core on these same RTL habits.
- Back to [Domain 08 overview](../../README.md).