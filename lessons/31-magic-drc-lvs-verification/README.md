# Lesson 31: Magic DRC and LVS Verification

## What you are building

A verified physical layout with design-rule and layout-versus-schematic checks.

## What you will learn

Magic layout inspection, DRC errors, extraction, Netgen LVS, device mismatches, and the limits of automated verification.

## Prerequisites

[OpenLane Sky130 Flow](../30-openlane-sky130-flow/README.md).

## Tools and software

- Magic VLSI
- Netgen
- SkyWater SKY130 technology files
- Generated layout, netlist, and schematic references

## Build and test

Run DRC, classify and fix violations, extract the layout, and run LVS against the intended netlist. Keep the reports, tool versions, and known waivers with the design. A clean check does not replace electrical review or foundry sign-off.

## What to build next

Continue to Level 11: [Semiconductor Devices](../../levels/11-semiconductor-devices/README.md), or contribute a tested extension to the open-silicon path.
