# Hardware Atlas Audit Report

Scope: `levels/` (00–13), `resources/`, `opportunities/`, `projects/`.
Reference: AICTE ECE Model Curriculum ([PDF](https://www.aicte.gov.in/sites/default/files/Final_ECE.pdf)).
Date: 2026-09-17.

Legend: ✅ fixed · 🔶 partial · ❌ outstanding.

## Summary

| Area | Files | Status |
|---|---|---|
| Levels 00–10 | 11 READMEs | ✅ rewritten to template, active voice, links |
| Level 11 | README | ✅ rewritten; ECE-01 gaps closed |
| Level 12 | README | ✅ rewritten; ECE-01 fab unit + electives mapped |
| Level 13 | README | ✅ rewritten; EC28/EC-P3/electives mapped |
| resources/ | 7 files | ✅ punctuation/run-on and stale-folder fixes |
| opportunities/ | README | ✅ voice cleanups |
| projects/ | README | ✅ garbled PR section + links fixed |
| AUDIT_REPORT.md | root | ✅ this file |

## Cross-check: AICTE course map

| Level | Course(s) | Coverage gap before | Now |
|---|---|---|---|
| 00 Getting started | Sem I/II basic EE | No prerequisites, no syllabus ties | ✅ Prerequisites + resources added |
| 01 Basic circuits | EC06 Network Theory | KVL/KCL underweighted in-circuit | ✅ KCL/KVL + Thevenin/superposition bullets |
| 02 Analog electronics | EC08/EC10 Analog Circuits | Multistage/feedback/CMRR/op-amp apps absent | ✅ "rest of the family" note + AICTE link |
| 03 Digital electronics | EC03 Digital System Design | Boolean algebra/K-maps missing | ✅ Added; links to Level 08 lesson 23 |
| 04 Microcontrollers | EC12 Microcontrollers | Timers + interrupts missing | ✅ Added |
| 05 Embedded systems | EC20 + EC22 | No product-side framing | ✅ EC20 product note + EC22 node |
| 06 PCB design | EC-P1/P2 (no direct course) | Unlabelled as applied | ✅ Mapped to project courses |
| 07 Hardware interfaces | EC12 serial I/O, EC20 interfacing | Unmapped | ✅ Mapping note added |
| 08 FPGA & RTL | EC03 HDL + EC24 | Unmapped | ✅ HDL + EC24 framing, HDLBits/ChipVerify links |
| 09 Computer architecture | EC18 Computer Architecture | Unmapped | ✅ EC18 "keeps going" note + Ripes link |
| 10 ASIC design | EC24 VLSI Design | Transistor/delay half unclear | ✅ Split-note vs layout half added |
| 11 Semiconductor devices | EC01 Electronic Devices | Schottky, MOS C–V, optoelectronics, sheet resistance, generation–recombination missing | ✅ Added |
| 12 Semiconductor fabrication | EC01 fab unit + ECEL5/ECEL16 | Twin-tub process, sputtering absent | ✅ Added; elective pointers |
| 13 Advanced hardware | EC28 seminar + EC-P3 + electives | No syllabus tie | ✅ Mapped; research/fellowship link |

## Per-level findings (before → after)

### 00-getting-started
- Structure: was a bare links list. → ✅ full template (prerequisites, core concepts, lessons table, diagram, common mistakes, resources, next).
- Links: had none to resources. → ✅ wiring included.

### 01-basic-circuits
- Style: dense, em-dash heavy, first-person tossaway ("I have a list of…"). → ✅ active, single-voice.
- Headings: used `:` like segments. → ✅ `--` standard.
- Terms: KCL/KVL/reciprocity squeezed under concept list. → ✅ expanded (EC06).

### 02-analog-electronics
- Coverage: op-amp only; multistage/feedback/oscillators missing. → ✅ EC08/EC10 family note.
- Links: no back-link to level 01. → ✅ added.

### 03-digital-electronics
- Coverage: Boolean algebra, K-maps, building blocks missing. → ✅ added.
- Links: no back-link. → ✅ added.

### 04-microcontrollers
- Coverage: EC12 timers/interrupts missing. → ✅ added.
- Links: no back-link. → ✅ added.

### 05-embedded-systems
- Coverage: EC20/EC22 self-learning unit missing. → ✅ added.
- Links: external docs added (Zephyr native_sim). Other doc links that crawl as 403 are bot-blocking, not dead.

### 06-pcb-design
- Syllabus: no direct AICTE course. → ✅ special case; EC-P1/P2 mapping.
- Links: Phil's Lab, Robert Feranec added.

### 07-hardware-interfaces
- Syllabus: unmapped. → ✅ EC12/EC20/EC22 note.
- Links: no back-link. → ✅ added.
- Structure: unlabelled "moving parts". → ✅ folded into core concepts.

### 08-fpga-and-rtl
- Coverage: HDL part of EC03 + EC24 unmapped. → ✅ framing note.
- Links: HDLBits, ChipVerify added (verified live).

### 09-computer-architecture
- Coverage: EC18 extension note missing. → ✅ added (pipelining/caches/IEEE 754 → Level 13).
- Links: Ripes added.

### 10-asic-design
- Coverage: transistor/delay half vs layout half unclear. → ✅ note added.
- Links: no back-link. → ✅ added.

### 11-semiconductor-devices
- Headings: `—`/`:` mixed. → ✅ `--`.
- Style: em-dash heavy preambles, hedging. → ✅ tightened.
- Coverage (ECE-01): Schottky, MOS C–V, optoelectronics (LED/photodiode/solar cell), sheet resistance, generation–recombination, reverse recovery. → ✅ added.
- Structure: TOC conversationally phrased. → ✅ clean TOC.
- Diagram: present (`measure → model → compare`). → ✅.

### 12-semiconductor-fabrication
- Structure: no Prerequisites; lessons table absent; coursework unlinked to level 11. → ✅ Prerequisites, Lessons (lesson 30), prev/next links.
- Coverage (ECE-01 fab unit): twin-tub CMOS + sputtering. → ✅ added.
- Electives: MEMS (ECEL5), Nanoelectronics (ECEL16). → ✅ pointed out.
- Typo/filler cleared ("off-the-shelf parts"). Diagram: two mermaid flows. → ✅.

### 13-advanced-hardware
- Typos: "checklist expect to bounce backward" (missing comma), em-dash chains. → ✅.
- Structure: no Prerequisites, no Lessons. → ✅ added.
- Syllabus: EC28/EC-P3/electives. → ✅ mapped.
- Links: Project/Contributing/Opportunities. → ✅ added. Diagram loop retained.

## resources/

### tools.md, components.md, india.md, power-and-batteries.md
- Run-ons / missing terminal punctuation ("…right supply chains in India match the purchase…", "≠ simpler it's a system…", "don't skip this especially…"). → ✅ all re-punctuated.
- components.md: stale `13-advanced-research` folder name (2 links + TOC + section title). → ✅ `13-advanced-hardware`.

### simulation.md, help.md, gate.md
- Minor touch-ups; no structural defects. → ✅ passed.

## opportunities/

- Passive "Region is inferred", dangling "It is an inference". → ✅ tightened to active voice, kept the hedging sentence because it is load-bearing (skew warning).

## projects/

- Garbled text: "Open a pull request, you can watch refer to the docs : [`[Opening a PR]`]…". → ✅ rewritten, clean links.
- Hard-coded GitHub blob link to CONTRIBUTING.md → ✅ relative `../CONTRIBUTING.md`.

## Links

- **Internal (165 md links):** all paths and anchors resolve; verified programmatically (link + slugged-anchor crawler on every file above).
- **Internal (35 lessons):** every level's lesson-table target exists in `lessons/`.
- **External (~100 URLs crawled):** 90 healthy; the rest are bot-blocked (403) or timeouts on known-live sites (forums.raspberrypi.com, gateoverflow.in, Digi-Key, st.com, analog.com, vlabs). No dead links found. This repo is private, so GitHub-API/raw anonymous checks 404 by design.

## Residual items (outside this pass)

- Root `README.md` not reclassed (out of scope as agreed).
- `lessons/31` and `levels` doc parity: lesson READMEs untouched (were not in scope).
- resources H1 emojis (🧰🔬⚡🎯📐) intentionally preserved.