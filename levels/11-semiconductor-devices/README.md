# Level 11 — Semiconductor Devices

Diode, BJT, and MOSFET behaviour through controlled measurements, small-signal models, SPICE, and temperature variation. This is where the physics meets the circuits you have already built.

> [!NOTE]
> This level is theory and simulation-driven. There are no dedicated lesson files yet. See [Simulation](../../resources/simulation.md) for SPICE tools.

> [!TIP]
> If this is your first pass at device physics, read the sections in order. Each device section leans on the "Physics primer" below — the diode equation, the BJT model, and the MOSFET equations are all the same drift-diffusion story told from a different angle.

## Table of contents

- [What this level covers](#what-this-level-covers)
- [A five-minute physics primer](#a-five-minute-physics-primer)
- [The diode](#the-diode)
- [The BJT](#the-bjt)
- [The MOSFET](#the-mosfet)
- [Device by device (quick reference)](#device-by-device-quick-reference)
- [Measure, model, compare](#measure-model-compare)
- [Common mistakes](#common-mistakes)
- [Where to go from here](#where-to-go-from-here)
- [Resources](#resources)

## What this level covers

- Diode I–V behaviour and the Shockley relation behind it
- BJT regions of operation, small-signal models, and temperature drift
- MOSFET threshold, channel behaviour, and the SPICE models that approximate them
- Measurement discipline: record the uncertainty every time

---

## A five-minute physics primer

Every device in this level is built from the same raw material story, so it's worth having it straight before you touch a diode, a BJT, or a MOSFET.

**Bands and the gap.** In a crystal, electrons can only occupy certain energy ranges — *bands* — separated by forbidden *gaps*. The **valence band** is (mostly) full; the **conduction band** is (mostly) empty. The size of the gap between them, $E_g$, is what makes a material a conductor, an insulator, or a semiconductor. Silicon's $E_g \approx 1.12\ \text{eV}$ at room temperature — small enough that a modest amount of thermal energy or doping can push carriers across it, unlike an insulator's $E_g$ of several eV.

**Intrinsic carrier concentration.** Even undoped ("intrinsic") silicon has some free electrons and holes, created purely by thermal energy knocking electrons across the gap:

$$
n_i = \sqrt{N_c N_v}\; e^{-E_g / (2kT)}
$$

where $N_c$ and $N_v$ are the effective densities of states in the conduction and valence bands, $k$ is Boltzmann's constant, and $T$ is absolute temperature. Note the exponential: $n_i$ roughly doubles every 8–10 °C for silicon. This single fact is the reason diode leakage current, BJT $\beta$, and MOSFET subthreshold current all drift with temperature — it's not three separate quirks, it's one exponential showing up three times.

**Doping.** Add a controlled trace of impurity atoms and you can flood the crystal with one carrier type on purpose:
- **n-type**: donor atoms (e.g. phosphorus in silicon) contribute extra electrons. Electrons become the *majority carrier*.
- **p-type**: acceptor atoms (e.g. boron) create *holes* — missing electrons that behave like mobile positive charge. Holes become the majority carrier.

**Two transport mechanisms.** Once you have free carriers, they move in exactly two ways:

$$
J_{\text{drift}} = q\,(n\mu_n + p\mu_p)\,E
\qquad\qquad
J_{\text{diffusion}} = qD_n \frac{dn}{dx} - qD_p \frac{dp}{dx}
$$

*Drift* is carriers being pushed by an electric field (this dominates in a MOSFET's channel and a BJT's collector-base region). *Diffusion* is carriers spreading from where they're concentrated to where they're not (this dominates carrier transport across a BJT's base and across a forward-biased diode's junction). The two are linked by the **Einstein relation**, $D = \mu kT/q$, so mobility $\mu$ and diffusivity $D$ are really the same underlying number.

Keep those three ideas — exponential thermal sensitivity, doping asymmetry, and drift vs. diffusion — in your back pocket. Every equation below is a specific consequence of them.

---

## The diode

A diode is what you get when you push a p-type region up against an n-type region and let the carriers sort themselves out.

![PN junction band diagram showing depletion region and band bending](../../images/pnjunctionimage.png)

At the junction, electrons diffuse from the n-side into the p-side and holes diffuse the other way, until the resulting charge imbalance creates an internal electric field strong enough to stop further net diffusion. What's left behind is a **depletion region** — depleted of free carriers — and a **built-in potential**:

$$
V_0 = \frac{kT}{q}\ln\!\left(\frac{N_A N_D}{n_i^2}\right)
$$

which for a typical silicon diode is around 0.6–0.7 V.

### The Shockley equation

Apply an external voltage $V$ across the junction and the current that flows is:

$$
I = I_0\left(e^{\,V / (nV_T)} - 1\right)
$$

- $I_0$ is the **reverse saturation current** — tiny (pA–nA range), and exponentially temperature-dependent, since it inherits $n_i^2$'s temperature sensitivity.
- $V_T = kT/q$ is the **thermal voltage**, about 25.85 mV at 300 K (a good rule of thumb: 26 mV at room temperature).
- $n$ is the **ideality factor** — 1.0 for an "ideal" diode, closer to 1.5–2 for real silicon diodes where recombination inside the depletion region adds a second current component.

![Diode forward and reverse I-V curve](../../images/images.png)

A few consequences worth internalizing:

- **Forward region** ($V > 0$): current rises exponentially. Because it's an exponential, the forward voltage barely moves even as current changes by orders of magnitude — this is why "diode drop ≈ 0.6–0.7 V" is such a durable approximation, and also why it's an approximation, not a law.
- **Reverse region** ($V < 0$): current saturates at $-I_0$ — small and roughly constant, until you push far enough negative to hit breakdown.
- **Breakdown**: at a large enough reverse voltage, either **avalanche multiplication** (carriers gain enough energy to knock loose new carrier pairs) or, in heavily-doped junctions, **Zener tunnelling** causes current to rise sharply. Zener diodes are built to exploit this on purpose as a voltage reference.
- **Temperature coefficient**: $V_F$ for a silicon diode drops by roughly **−2 mV/°C** at constant current, because $I_0$ rises faster with temperature than the exponential term can compensate for at fixed $I$.
- **Small-signal resistance**: linearize the exponential around a bias point $I_D$ and you get a dynamic resistance $r_d = \dfrac{n V_T}{I_D}$ — useful the moment you want to treat a diode as a small AC element rather than a nonlinear one.

### What SPICE actually fits

A SPICE diode model (`.model D1 D(...)`) isn't solving Poisson's equation from scratch — it's fitting a handful of parameters to your measured curve: `IS` ($I_0$), `N` (ideality factor), `RS` (series resistance, which rounds off the exponential's sharp knee at high current), `TT` (transit time, relevant for switching speed), and `BV`/`IBV` (breakdown voltage and current). Measuring your own diode and fitting these parameters — rather than trusting the default `.model` values — is exactly the "measure vs. model" discipline this level is about.

---

## The BJT

A Bipolar Junction Transistor is two PN junctions back to back, sharing a thin middle region, arranged so that the middle region's thinness and doping asymmetry make it possible for a small current at one terminal to control a much larger current between the other two.

![NPN BJT structure and carrier flow](../../images/npntransistor.png)

### Regions of operation

| Region | Junction states | What it means physically |
|---|---|---|
| **Cutoff** | Both junctions reverse-biased | Essentially no carrier injection; transistor is "off" |
| **Active (forward)** | Base-Emitter forward, Base-Collector reverse | Carriers injected at the emitter diffuse across the thin base and get swept into the collector — this is the useful amplifying region |
| **Saturation** | Both junctions forward-biased | Collector can no longer pull carriers away fast enough; $V_{CE}$ collapses to a small value; transistor behaves like a closed switch |
| **Breakdown** | Excessive reverse bias at BC or BE junction | Avalanche multiplication takes over; usually a region to avoid, not use |

### Current gain and the Ebers–Moll picture

In the active region, most of the current injected at the emitter survives the trip across the thin base and is collected:

$$
\alpha = \frac{I_C}{I_E} \quad(\text{close to 1}), \qquad
\beta = \frac{I_C}{I_B} = \frac{\alpha}{1-\alpha} \quad(\text{often 50–300})
$$

The full **Ebers–Moll model** treats the BJT as two coupled diode equations (one per junction) plus the coupling terms that describe carriers making it across the base — worth reading once so that "$\beta$" doesn't feel like a magic constant, but the rest of this level mostly uses the simpler large-signal relation $I_C \approx \beta I_B$ plus the small-signal model below.

### The Early effect

In a real transistor, $I_C$ isn't perfectly independent of $V_{CE}$ — as $V_{CE}$ increases, the collector-base depletion region widens slightly and encroaches into the base, effectively narrowing it and letting a bit more current through:

$$
I_C = I_{C0}\left(1 + \frac{V_{CE}}{V_A}\right)
$$

$V_A$, the **Early voltage**, is typically tens to hundreds of volts. This is the BJT's version of a MOSFET's finite output resistance — extrapolate the $I_C$–$V_{CE}$ lines backwards and they all meet at $V_{CE} = -V_A$.

### Small-signal (hybrid-π) model

Once you bias a BJT into its active region and perturb it with a small AC signal, it linearizes into three key parameters:

$$
g_m = \frac{I_C}{V_T}, \qquad
r_\pi = \frac{\beta}{g_m}, \qquad
r_o = \frac{V_A}{I_C}
$$

$g_m$ (transconductance) tells you how much collector current you get per volt of base-emitter swing; $r_\pi$ is the small-signal input resistance looking into the base; $r_o$ is the output resistance set by the Early effect. Nearly every BJT amplifier gain formula you'll meet later is just Ohm's law applied to combinations of these three numbers.

### Temperature drift, concretely

- $V_{BE}$ at fixed $I_C$ drops by about **−2 mV/°C** — same mechanism as the diode's $V_F$ drift, because the base-emitter junction *is* a diode.
- Leakage and $I_{C0}$ roughly double every **10 °C**, tracking $n_i^2$.
- $\beta$ typically increases with temperature, which is part of why thermal runaway is a real failure mode in poorly-biased BJT circuits: hotter → more current → more self-heating → hotter.

---

## The MOSFET

A MOSFET controls current with an electric field across an insulating layer rather than by injecting carriers across a junction — which is why its gate draws (ideally) no DC current at all, unlike a BJT's base.

![NMOS transistor cross-section](../../images/nmoscrosssection.webp)

### Threshold and the inversion channel

Below a certain gate-source voltage, no conducting path exists between source and drain — the body underneath the gate is the "wrong" doping type. Above the **threshold voltage** $V_{TH}$, the gate's electric field pulls enough minority carriers to the surface to invert it into a thin conducting channel of the *opposite* type to the body. For an NMOS device, a p-type body inverts into an n-type surface channel once $V_{GS} > V_{TH}$.

### Regions of operation

| Region | Condition | Behaviour |
|---|---|---|
| **Cutoff** | $V_{GS} < V_{TH}$ | No channel; $I_D \approx 0$ (ignoring subthreshold leakage) |
| **Triode / linear** | $V_{GS} > V_{TH}$, $V_{DS} < V_{GS}-V_{TH}$ | Channel exists along the full length; behaves roughly like a voltage-controlled resistor |
| **Saturation** | $V_{GS} > V_{TH}$, $V_{DS} \geq V_{GS}-V_{TH}$ | Channel "pinches off" near the drain; current becomes (almost) independent of $V_{DS}$ |

The governing equations, with $\mu_n$ the channel mobility, $C_{ox}$ the oxide capacitance per unit area, and $W/L$ the transistor's width-to-length ratio:

$$
\text{Triode:}\quad I_D = \mu_n C_{ox}\frac{W}{L}\left[(V_{GS}-V_{TH})V_{DS} - \frac{V_{DS}^2}{2}\right]
$$

$$
\text{Saturation:}\quad I_D = \frac{1}{2}\mu_n C_{ox}\frac{W}{L}(V_{GS}-V_{TH})^2\,(1+\lambda V_{DS})
$$

The $(1+\lambda V_{DS})$ term is the MOSFET's analogue of the BJT's Early effect — real channels shorten slightly as $V_{DS}$ rises past pinch-off, letting a bit more current through than the idealized square law predicts.

### Small-signal parameters

$$
g_m = \sqrt{2\mu_n C_{ox}\frac{W}{L}I_D} = \frac{2I_D}{V_{GS}-V_{TH}}, \qquad
r_o = \frac{1}{\lambda I_D}
$$

Note the square-root dependence of $g_m$ on bias current — a MOSFET is intrinsically less transconductance-efficient per unit of bias current than a BJT (whose $g_m$ scales linearly with $I_C$), which is a large part of why analog designers reach for BJTs when they need gain from limited current, and MOSFETs when they need near-zero gate current and easy scaling.

### What "process corners" means in the SPICE table

MOSFET SPICE models (BSIM3, BSIM4, and their descendants for modern nodes) fit dozens of parameters — $V_{TH}$, mobility degradation, short-channel effects, velocity saturation — to real fabrication data. "Process corners" (`TT`, `FF`, `SS`, `FS`, `SF` — typical/fast/slow combinations of NMOS and PMOS speed) exist because no two fabricated chips are identical; a design has to work across the *range* SPICE predicts, not just at the nominal fit.

---

## Device by device (quick reference)

| Device | What you measure | What SPICE shows you |
|---|---|---|
| Diode | Forward voltage at several currents | Shockley model fit, temperature coefficient |
| BJT | Bias point and gain | Small-signal model, Early effect |
| MOSFET | Threshold and $I_D$ vs. $V_{GS}$ | Channel behaviour, process corners |

---

## Measure, model, compare

```mermaid
flowchart LR
    D[Device] --> M[Measure]
    D --> S[SPICE model]
    M --> C{Match?}
    S --> C
    C -->|No| R[Refine the model or the measurement]
    R --> S
```

A measurement without an uncertainty attached is a rumor, not data. When you record a diode's $V_F$ at a given $I_D$, or a MOSFET's $V_{TH}$ from an $I_D$–$V_{GS}$ sweep, propagate your instrument's error through whatever formula you used to extract the parameter:

$$
\delta f = \sqrt{\left(\frac{\partial f}{\partial x_1}\delta x_1\right)^2 + \left(\frac{\partial f}{\partial x_2}\delta x_2\right)^2 + \cdots}
$$

If your extracted $V_{TH}$ moves by more than its own uncertainty between two "identical" measurements, that's not noise to average away — that's a sign either your measurement setup or your model assumptions need attention before you trust the number.

## Common mistakes

- Reading one I–V point and calling it "the" characteristic
- Treating absolute maximum ratings as a suggested operating range
- Pushing a part far enough to self-heat during a sweep, then reading a drift as physics
- Trusting a simulator model over the datasheet you actually have
- Forgetting that $V_T$, $n_i$, and every leakage current in this level are all exponential in temperature — a "small" temperature change is rarely small in its effect
- Quoting a $\beta$ or $g_m$ without stating the bias point it was measured at — these parameters are functions of bias, not fixed constants
- Assuming a MOSFET's square-law equation holds exactly at short channel lengths, where velocity saturation and other short-channel effects bend the curve well before SPICE's simplest models would predict

## Where to go from here

- [Level 12](../12-semiconductor-fabrication/README.md) covers how the devices are actually made.
- [Level 10](../10-asic-design/README.md) connects device behaviour to standard-cell design.

---

## Resources

### Lab bench

- [Simulation](../../resources/simulation.md) — the SPICE tools referenced throughout this level.

### Foundational reading

- [Semiconductor device — Wikipedia](https://en.wikipedia.org/wiki/Semiconductor_device) — broad overview and a good jumping-off point into linked articles on specific devices.
- [MIT OpenCourseWare 6.002 (Circuits and Electronics)](https://ocw.mit.edu/courses/6-002-circuits-and-electronics-spring-2007/) — the full university treatment, from first principles to op-amps.

### Video courses & lectures

- **NPTEL / IIT Bombay — Semiconductor Device Modeling** (Prof. Yogesh Singh Chauhan): a comprehensive academic series covering carrier transport physics through advanced MOSFET electrostatics.
- **MIT 6.012 — Microelectronic Devices and Circuits** (Prof. Jesús del Alamo): an older archived course, still widely regarded for building carrier-level physical intuition about how transistors actually work.
- **All About Circuits / EE Video Library**: bite-sized, practical walkthroughs of diode, BJT, and MOSFET behaviour under different bias conditions.

### Interactive simulators & reference sites

- **[Falstad Circuit Simulator](https://www.falstad.com/circuit/)**: browser-based, interactive — build a circuit with diodes, BJTs, or MOSFETs and watch voltages and currents animate in real time.
- **PVEducation.org**: photovoltaics-focused, but its interactive modules on band gaps, recombination, and carrier generation are some of the clearest on the web.
- **HyperPhysics** (Georgia State University): concept-map style reference — fast lookup for drift, diffusion, and Fermi-level relationships when a formula slips your mind.

### Blogs & industry analysis

- **SemiAnalysis**: modern semiconductor industry and fab-economics analysis, with occasional deep dives into transistor scaling (FinFET vs. GAA nanosheet architectures).
- **Chipstrat** and **Less Than Dot**: independent technical blogs tracking microelectronics engineering and layout design concepts.
- **IEEE Solid-State Circuits Magazine / IEEE Spectrum**: accessible articles on device architectures and future-node physics.

### Open-source simulation & TCAD tools

| Tool | What it's for |
|---|---|
| [Ngspice](https://ngspice.sourceforge.io/) | The open-source descendant of Berkeley SPICE — the standard circuit-level simulator for taking device parameters into real circuits |
| [DEVSIM](https://devsim.org/) | TCAD in Python: define Poisson and drift-diffusion equations yourself and solve them over 1D/2D/3D meshes |
| Charon (Sandia National Labs) | Massively parallel, open-source finite-element device simulator, used for advanced carrier transport and radiation-effect studies |
| GSS (General-purpose Semiconductor Simulator) | Classic open-source 2D simulator with drift-diffusion and hydrodynamic models; can link to Ngspice for mixed device-circuit simulation |

### Commercial / industry-standard tools

| Tool | What it's for |
|---|---|
| Synopsys Sentaurus TCAD | The dominant foundry-grade suite for simulating fabrication processes and device physics at leading-edge nodes |
| Silvaco Victory / Atlas | Synopsys's primary competitor; heavily used for power electronics, optoelectronics, and CMOS scaling studies |
| Silvaco SmartSpice / Keysight ADS | High-end circuit simulators for extracting device models and simulating precision analog/RF behaviour |

> [!NOTE]
> The open-source tools above are genuinely capable but have a real learning curve — they're worth exploring once the equations in this README feel familiar, not as a replacement for working through the diode/BJT/MOSFET fundamentals first.