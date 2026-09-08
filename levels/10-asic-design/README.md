# Level 10: ASIC Design

ASIC work moves from synthesizable RTL to gates, physical constraints, verification, and manufacturable outputs.

## Project sequence

1. [Yosys RTL synthesis](../../lessons/29-yosys-rtl-synthesis/README.md): map RTL to gates and inspect optimization and area reports.
2. [OpenLane Sky130 flow](../../lessons/30-openlane-sky130-flow/README.md): run an RTL-to-GDSII physical-design flow and review its reports.
3. [Magic DRC and LVS verification](../../lessons/31-magic-drc-lvs-verification/README.md): check layout rules and compare extracted layout against the intended netlist.
4. **Standard-cell layout:** place and route a small block with power and clock constraints.
5. **Verification flow:** combine simulation, lint, formal checks, and coverage.
6. **Open shuttle design:** prepare a small hardened block for an open silicon flow such as Tiny Tapeout.
7. **Post-silicon comparison:** compare measured silicon behaviour with pre-silicon assumptions.

## Verify

Track timing, area, power estimates, design-rule checks, coverage, and known limitations. Fabrication is a later step, not a substitute for verification.

**Next:** [Level 11: Semiconductor Devices](../11-semiconductor-devices/README.md).
