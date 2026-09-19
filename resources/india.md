# 🇮🇳 Hardware Sourcing & Electronics Lab Guide

Sourcing components, building a diagnostic workbench, and verifying hardware integrity in India. Whether you are building simple microelectronics or complex embedded hybrid systems, this reference covers where to buy, what to stock, and how to avoid counterfeits.

> **Related guides →** [Components](components.md) · [Tools](tools.md) · [Power & Batteries](power-and-batteries.md) · [Simulation](simulation.md) · [Help](help.md) · [GATE](gate.md)

## 📑 Table of Contents

1. [Component Categories & Sourcing Strategy](#1-component-categories--sourcing-strategy)
2. [Sourcing: Where to Buy](#2-sourcing-where-to-buy)
   - [Online E-Shopping](#online-e-shopping)
   - [Offline Markets & Salvage (NCR Focus)](#offline-markets--salvage-ncr-focus)
3. [The Essentials: What to Stock](#3-the-essentials-what-to-stock)
   - [Microcontrollers & Dev Boards](#microcontrollers--dev-boards)
   - [Component Inventory](#component-inventory)
   - [Power & Wiring](#power--wiring)
4. [Tools & Diagnostic Workbench](#4-tools--diagnostic-workbench)
   - [Measurement & Diagnostic Equipment](#41-measurement--diagnostic-equipment)
   - [Soldering & Rework Station](#42-soldering--rework-station)
   - [Hand Tools & Bench Accessories](#43-hand-tools--bench-accessories)
   - [Wiring](#44-wiring)
   - [Work Surfaces](#45-work-surfaces)
   - [Minimum Viable Bench Checklist](#46-minimum-viable-bench-checklist)
5. [Quality Control: Inspecting Parts](#5-quality-control-inspecting-parts)
   - [Inspection Workflow](#51-inspection-workflow)
   - [Physical & Chemical Tests](#52-physical--chemical-tests)
   - [Electrical Verification](#53-electrical-verification)
   - [Common Counterfeit/Recycled Red Flags](#54-common-counterfeitrecycled-red-flags)
6. [Communities & Simulation Tools](#6-communities--simulation-tools)
7. [Related guides & cross-references](#7-related-guides--cross-references)


## 1. Component Categories & Sourcing Strategy

Before purchasing, categorize your Bill of Materials (BOM) to determine the right supplier. Never blindly trust a single marketplace for every component type.

```mermaid
flowchart LR
    Start[BOM Item] --> Q{Critical or Complex?}

    Q -- Yes --> Q2{Exact ICs, DSPs, or Transceivers?}
    Q2 -- Yes --> Auth[Authorized Distributors]
    Auth -.-> Mouser[Mouser / DigiKey]
    Auth -.-> E14[Element14]

    Q -- No --> Q3{Dev Boards, Modules, Batteries?}
    Q3 -- Yes --> Maker[Indian E-Stores]
    Maker -.-> Robu[Robu / Robomart]
    Maker -.-> EComp[ElectronicsComp]

    Q3 -- No --> Q4{Bulk wires, Passives, Hardware?}
    Q4 -- Yes --> Local[Offline Markets]
    Local -.-> Lajpat[Lajpat Rai / SP Road]
    Local -.-> Nehru[Nehru Place / Salvage]
```

[⬆ Back to top](#-table-of-contents)


## 2. Sourcing: Where to Buy

### Online E-Shopping

| Store | Best for | Link |
|---|---|---|
| Mouser India | Authentic ICs, specific MCUs, precision components, safety-critical parts | [mouser.in](https://www.mouser.in/) |
| Element14 India | Same tier; strong same-day/next-day fulfillment in major metros | [in.element14.com](https://in.element14.com/) |
| DigiKey India | Same tier; the deepest shared inventory of the big three | [digikey.in](https://www.digikey.in/) |
| Robu.in | Dev boards, maker hardware, robotics, tools | [robu.in](https://robu.in/) |
| Robomart | Dev boards, maker hardware, robotics | [robomart.com](https://www.robomart.com/) |
| ElectronicsComp | Common components, modules, prototyping quantities | [electronicscomp.com](https://www.electronicscomp.com/) |
| Electronify India | Common components, modules, prototyping quantities | [electronifyindia.com](https://www.electronifyindia.com/) |
| Electroshield | Passives and common building blocks at low unit prices | [electroshield.com](https://www.electroshield.com/) |

**Element14 / Mouser / DigiKey** are the gold standard for authentic ICs, specific microcontrollers, and precision components — use them for complex development and safety-critical parts. Indian e-stores are excellent for dev boards, maker hardware, and prototyping quantities, but do not place 100% trust in them for highly sensitive silicon: cheap green PCBs or modules sometimes utilize rejected or recycled IC batches. Cross-check any part that matters against the [inspection workflow](#5-quality-control-inspecting-parts).

### Offline Markets & Salvage (NCR Focus)

Buying offline wins on price and on instant inspection, but you carry the risk: vendors rarely accept returns on false or broken parts. Run the [inspection workflow](#5-quality-control-inspecting-parts) before money changes hands, not back at the bench. The table below covers the major electronics streets nationwide; the NCR markets get the most detail.

| Market | City | Best for | JustDial | Google Maps |
|---|---|---|---|---|
| Lajpat Rai Market / Chandni Chowk | Delhi | Cheap bulk passives, connectors, hardware, hand tools | [component dealers](https://www.justdial.com/Delhi/Electronic-Component-Dealers-in-Lajpat-Rai-Market/nct-10184815) | [maps](https://www.google.com/maps/search/Lajpat+Rai+Market,+Delhi) |
| Nehru Place | Delhi | Salvage: stripped boards, motors, heatsinks, second-hand gear to reverse engineer | [computer dealers](https://www.justdial.com/Delhi/Computer-Dealers-in-Nehru-Place/nct-10110698) | [maps](https://www.google.com/maps/search/Nehru+Place,+Delhi) |
| Gaffar Market, Karol Bagh | Delhi | Surplus and refurbished electronics | [market listing](https://www.justdial.com/Delhi/Gaffar-Market-Block-51-Pt-Quarters-Karol-Bagh/011PXX11-XX11-220127151849-T1H9_BZDET) | [maps](https://www.google.com/maps/search/Gaffar+Market,+Karol+Bagh,+Delhi) |
| SP Road | Bangalore | The classic components street: passives, ICs, wire, tools | [component dealers](https://www.justdial.com/Bangalore/Electronic-Component-Dealers-in-Sp-Road/nct-10184815) | [maps](https://www.google.com/maps/search/SP+Road,+Bangalore) |
| Ritchie Street | Chennai | Bulk components, tools, repair parts | [component dealers](https://www.justdial.com/Chennai/Computer-Part-Dealers-in-Richie-Street-Mount-Road/nct-10115684) | [maps](https://www.google.com/maps/search/Ritchie+Street,+Chennai) |
| Lamington Road | Mumbai | Components, tools, audio and salvage gear | [component dealers](https://www.justdial.com/Mumbai/Electronic-Component-Dealers-in-Lamington-Road/nct-10184815) | [maps](https://www.google.com/maps/search/Lamington+Road,+Mumbai) |
| Kotwali electronics bazaar | Kolkata | Surplus bargains (pricing varies; ask the locals where the good bins are) | — | [maps](https://www.google.com/maps/search/Electronics+Market,+Kolkata) |

* **Local maker hubs (Delhi NCR):** [Maker Junction](https://www.google.com/maps/search/Maker+Junction,+Delhi) and [Robosaki](https://www.google.com/maps/search/Robosaki,+Delhi) for maker supplies and rapid prototyping.
* **PCB fabrication (Delhi NCR):** for local prototyping without waiting on international shipping, **Atronics (Mayur Vihar)** and **Megabyte** are solid job shops — [find PCB manufacturers in Delhi on JustDial](https://www.justdial.com/Delhi/PCB-Manufacturers/nct-10233654).

[⬆ Back to top](#-table-of-contents)


## 3. The Essentials: What to Stock

### Microcontrollers & Dev Boards

Skip the older Uno R3 if you are moving into modern embedded systems. Opt for boards that force you to read datasheets and understand modern architectures:

* **[Arduino UNO R4 WiFi](https://docs.arduino.cc/hardware/uno-r4-wifi/)** — modern AVR with WiFi; the board the roadmap's microcontroller level assumes.
* **[Arduino Nano ESP32](https://docs.arduino.cc/hardware/nano-esp32/)** — the ESP32-S3 in an Arduino footprint for connected builds.
* **[Raspberry Pi Pico W](https://www.raspberrypi.com/products/raspberry-pi-pico/)** — RP2040, C/C++ and MicroPython, the cheapest honest way to practice bare-metal.
* **[ESP32 family (Espressif)](https://www.espressif.com/en/products/socs/esp32)** — the SOC line that dominates Indian hobbyist IoT; check the Espressif pages for module variants and the official docs.

All of these are stocked on the [e-stores above](#online-e-shopping). The domain-by-domain buy list — what to own at each stage, and what to skip — lives in the [Components guide](components.md).

### Component Inventory

A well-stocked lab should have these on hand. The full taxonomy — which values to stock, when to prefer SMD vs THT, and where each category sits on the [levels map](../README.md#-find-something-quickly) — is in the [Components guide](components.md):

* **Logic & Timing:** Comparators, Timer/Oscillators, Logic Level Shifters, Shift Registers.
* **Conversion:** ADCs and DACs.
* **Power Management:** LDOs, Buck/Boost Converters (DC-DC), N-channel MOSFETs, BJTs, Diodes.
* **Passives:** Resistors, Capacitors (Keep a hybrid inventory: SMD for MCUs and sensors, THT for jacks, relays, and plug-and-play areas).
* **Modules & Comms:** USB-UART bridges, OLEDs, IMUs, EEPROM chips. *Optional but highly recommended for automotive/industrial:* MCP2515 + TJA1050 (CAN transceivers).

### Power & Wiring

Everything below goes deeper in the [Power & Batteries guide](power-and-batteries.md): wiring practice, charger boards, protection circuits, and the BMS/fuse stack every lithium build should carry.

* **Wiring:** Use **solid core wires** for clean breadboarding; rely less on messy jumper wires as you advance.
* **Batteries:** 18650 Li-Ion cells, 3.7V LiPo packs, and CR2032 coins for compact modeling.
* **CRITICAL SAFETY:** Always use a **BMS (Battery Management System)** with lithium batteries to prevent thermal runaway. Never puncture, throw, or use swollen LiPo pouches.

[⬆ Back to top](#-table-of-contents)


## 4. Tools & Diagnostic Workbench

Invest in your bench. Good tools prevent hours of debugging false hardware issues. The **[Tools guide](tools.md)** is the full tool-by-tool breakdown — every purchase, why it earns its place, and where in India to buy it. The tables below group tools by function with tiered recommendations (Budget / Hobbyist / Pro) so you can scale spend to how serious the lab is.

### 4.1 Measurement & Diagnostic Equipment

| Tool | Purpose | Budget Pick | Pro Pick | Notes |
|---|---|---|---|---|
| Digital Multimeter (DMM) | Voltage, current, continuity, resistance | Mastech MAS830L | Fluke 17B+ / 115 | Mandatory bench item buy first. |
| Bench Power Supply (variable, 0–30V) | Powering circuits under test, current-limiting to protect parts | Generic 30V/5A linear supply | Korad KA3005P | Look for a current-limit knob; this alone prevents most magic-smoke incidents. |
| Oscilloscope | Viewing signal timing, noise, PWM, comms bus traffic | DSO150 kit / Hantek 2C42 (USB) | Rigol DS1054Z | Only needed once you touch timing-sensitive or analog work. |
| Logic Analyzer | Decoding I2C/SPI/UART traffic | Saleae clone (8-channel) | Saleae Logic 8 (genuine) | Pairs well with PulseView/Sigrok software. |
| LCR Meter | Checking capacitor/inductor health, ESR | Basic handheld LCR | Component tester (DIY transistor tester) module | Useful for verifying salvaged passives before reuse. |
| Thermal Camera / IR Thermometer | Spotting hot components, shorts | IR thermometer gun | FLIR-based thermal camera | Great for catching a silently overheating regulator. |

### 4.2 Soldering & Rework Station

| Item | Budget/Hobbyist | Pro/Frequent Use | Why It Matters |
|---|---|---|---|
| Soldering Iron | TS100 / SID60A | Hakko FX-951 | Temperature-controlled tips give consistent, repeatable joints. |
| Hot Air Rework Station | Generic 858D | Quick 861DW / Hakko FR-810 | Needed for SMD rework and desoldering multi-pin ICs. |
| Solder Wire | 60/40 leaded, 0.8mm, 50g+ | Same, plus lead-free for compliance work | Leaded solder is easier for beginners; keep flux pen nearby. |
| Desoldering Tools | Manual pump | Desoldering gun / braid + pump combo | Braid (copper wick) is essential for fine SMD pads. |
| Flux | Basic rosin pen | No-clean liquid flux | Reduces bridging and improves wetting on tricky joints. |
| Fume Extractor | DIY fan + carbon filter | Dedicated benchtop extractor | Protects lungs during long sessions. Don't skip this. |

### 4.3 Hand Tools & Bench Accessories

* **Cutting/Stripping:** Wire strippers, flush cutters, precision side cutters.
* **Gripping:** Needle-nosed ESD-safe tweezers (straight + curved tip), hemostats.
* **Driving:** Precision screwdriver set, nut drivers, small adjustable wrench, pliers (needle-nose, flat).
* **Holding:** Weighted "helping hands" with alligator clips, PCB vise, third-hand magnifier with LED ring light.
* **Misc:** Crocodile/alligator test clips, standard electrical tape, copper shielding tape, heat-shrink tubing + heat gun, label maker or masking tape for bin labeling.

### 4.4 Wiring

* Use **solid core wire** for clean breadboarding; rely less on messy jumper wires as you advance to permanent builds.

### 4.5 Work Surfaces

| Mat Type | Best For | ESD Safe? | Notes |
|---|---|---|---|
| Silicone Mat | General Arduino/DIY soldering, heat resistance | No | Fine for hobbyist/maker work with no bare-die ICs. |
| Anti-Static (ESD) Rubber Mat | Motherboards, bare microchips, laptop repair | Yes (when grounded) | **Mandatory** for sensitive silicon must be wrist-strap grounded to actually work. |

### 4.6 Minimum Viable Bench Checklist

- [ ] Digital multimeter
- [ ] Temperature-controlled soldering iron + stand
- [ ] Solder, flux, desoldering braid
- [ ] Wire strippers, flush cutters, tweezers
- [ ] ESD wrist strap + grounded mat
- [ ] Helping hands / PCB vise
- [ ] Bench power supply (variable, current-limited)
- [ ] Storage bins for sorted passives/ICs

[⬆ Back to top](#-table-of-contents)

## 5. Quality Control: Inspecting Parts

When buying from informal markets or third-party sellers, inspect your silicon to avoid counterfeit, blacktopped, or recycled e-waste components. Treat every unbranded or loose-bin part as unverified until it passes the checks below.

### 5.1 Inspection Workflow

Run checks in this order cheapest/fastest first, so you reject bad parts before spending time on deeper testing.

```mermaid
flowchart TD
    A[Incoming Part] --> B[Visual Inspection]
    B -->|Fail: bad marking/indents| R1[Reject]
    B -->|Pass| C[Acetone Swab Test]
    C -->|Fail: ink wipes off| R2[Reject - Blacktopped]
    C -->|Pass| D[Pin/Lead Integrity Check]
    D -->|Fail: tarnish, re-tinned legs| R3[Reject - Recycled]
    D -->|Pass| E[Electrical Bench Test]
    E -->|Fail: wrong readings vs datasheet| R4[Reject]
    E -->|Pass| F[Accept into Inventory]
```

### 5.2 Physical & Chemical Tests

| Test | What You Need | How To Do It | Pass Criteria | Fail Signal |
|---|---|---|---|---|
| Visual Alignment | Loupe / macro phone lens | Inspect logo, text, and mold indents under magnification | Sharp, centered laser-etched marking; smooth mold indents | Blurry/offset print, rough or off-center indents |
| Acetone Swab Test | ≥99.5% lab-grade acetone, cotton swab | Gently rub markings for a few seconds | Marking stays intact (laser-etched) | Ink smears or wipes off (blacktopped remark) |
| Pin/Lead Inspection | Loupe or microscope | Check leg plating for uniformity | Uniform bright silver/tin plating | Tarnish, oxidation, uneven re-tinning, bent/re-straightened legs |
| Package Weight Check (optional) | Precision scale | Compare against known-good sample or datasheet spec | Matches expected weight within tolerance | Noticeably lighter/heavier (different die or filler) |
| Date/Lot Code Check | Loupe | Cross-check batch code format against manufacturer's coding scheme | Matches known format | Inconsistent/garbled lot code |

### 5.3 Electrical Verification

| Component Type | Bench Test | Tool Used | What To Check Against |
|---|---|---|---|
| Passives (R/C/L) | Measure value directly | Multimeter / LCR meter | Rated value ± tolerance printed on part |
| Diodes/LEDs | Diode-mode test | Multimeter diode function | Forward voltage drop in expected range, blocks reverse |
| Transistors/MOSFETs | Gain/threshold test | Multimeter transistor test or component tester | Datasheet hFE / Vgs(th) range |
| Digital ICs (logic, MCU, sensors) | Power up on bench supply, probe pins | Bench PSU + multimeter/oscilloscope + datasheet pinout | Correct idle voltages, expected signal activity on clock/reset pins |
| Comms modules (I2C/SPI/UART) | Bus probing | Logic analyzer | Device ACKs at correct address / responds to known commands |
| Batteries/Cells | Voltage + internal resistance | Multimeter, battery tester | Matches rated voltage; low internal resistance for age |

### 5.4 Common Counterfeit/Recycled Red Flags

- Mismatched font weight or spacing between the part number and date code on the same chip.
- Sanding or grinding marks on the package top (used to erase old markings before reprinting).
- Solder blobs or flux residue in pin gaps on a part sold as "new."
- Reels/tubes with resealed tape or non-factory packaging.
- Prices dramatically (>50%) below authorized-distributor pricing for an in-demand part.

> **Rule of thumb:** If a part fails *any* stage in the workflow above, reject it don't "test it in circuit anyway." A part that barely passes electrical test but failed visual/acetone checks is still likely to fail early in the field.

[⬆ Back to top](#-table-of-contents)


## 6. Communities & Simulation Tools

Before buying physical components for a complex layout, simulate it. The [Simulation guide](simulation.md) explains what simulation is good for (and what it cannot catch) before you pick a tool.

* **Simulators:** [Wokwi](https://wokwi.com/), [Tinkercad](https://www.tinkercad.com/), [EasyEDA](https://easyeda.com/), [Cirkit Designer](https://cirkitdesigner.com/).
* **Communities & Forums:** matching problem type to forum is a skill on its own — the [Help guide](help.md) maps communities to problems so you ask in the right place.
  * *Ideation:* Hackclub, Circuit Digest, Hackster.io, Instructables.
  * *Advanced Troubleshooting:* [Electrical Engineering Stack Exchange](https://electronics.stackexchange.com/), r/ElectricalEngineering, r/ECE.
  * *Specific Hardware:* Always refer to the respective official forums for Arduino, ESP32, or Raspberry Pi when working with those ecosystems.

> **Golden Rule:** Always verify a component's price across multiple sources, and heavily prioritize community reviews over marketing descriptions.

[⬆ Back to top](#-table-of-contents)


## 7. Related guides & cross-references

Sourcing is only one side of the workbench. Use this page together with the rest of the resources:

| Guide | Use it for | Link |
|---|---|---|
| Components | What to buy (and skip) at every level of the roadmap | [components.md](components.md) |
| Tools | The full tool-by-tool bench plan with Indian pricing and procurement routes | [tools.md](tools.md) |
| Power & Batteries | Wiring, charging, BMS and fuse protection before you plug lithium in | [power-and-batteries.md](power-and-batteries.md) |
| Simulation | Checking an idea before ordering hardware | [simulation.md](simulation.md) |
| Help | Picking the right community or forum for your problem | [help.md](help.md) |
| GATE | Running exam prep alongside project work | [gate.md](gate.md) |
| Levels | Where each skill this page buys parts for sits in the roadmap | [levels index](../README.md#-how-to-use-this-repository) |
| Projects | How to structure a build that outgrows the numbered lessons | [projects guide](../projects/README.md) |
| Opportunities | Jobs, hackathons, and programs that put this bench to work | [opportunities](../opportunities/README.md) |

The [Components guide](components.md) [Tools guide](tools.md) and [Power & Batteries guide](power-and-batteries.md) share this page's vocabulary: a component bought here is stocked per the components map, tested with the tools you bench here, and powered safely per the power guide.

[⬆ Back to top](#-table-of-contents)
