# Opportunities

Opportunities is a student-focused index inside Hardware Atlas for jobs, internships, hackathons, scholarships, research programs, fellowships, and open source programs that sit at the intersection of hardware and software.

Hardware Atlas teaches you how to build. Opportunities is where some of that building can turn into grants, internships, and careers. The two directories share the same vocabulary. The areas in the roadmap, from basic circuits up through embedded, FPGA, RTL, ASIC, VLSI, semiconductor fabrication, and computer architecture, are the same areas used to tag every opportunity here.

## What is included

The index covers these categories:

| Category | Examples |
|---|---|
| 💼 Jobs and internships | Embedded, firmware, hardware, FPGA, and RTL roles |
| 🏆 Hackathons and competitions | Build contests, robotics challenges |
| 🎓 Scholarships | Degree funding for engineering study |
| 🔬 Research programs | Labs, REUs, and research internships |
| 🧑‍💻 Fellowships | Structured programs for contributors and students |
| 🌐 Open source programs | GSoC, Outreachy, and similar |
| 📚 Other recurring opportunities | Anything recurring that does not fit above |

Opportunities are tagged with the Hardware Atlas areas they relate to:

Embedded, Firmware, Electronics, Hardware, PCB, FPGA, RTL, ASIC, VLSI, Semiconductor, EDA, DSP, Edge AI, Robotics, Automotive, Computer Architecture, and Low-level Systems.

## India vs international

Each opportunity has a `region` field with one of three values:

- **India**: located in India, or explicitly open to Indian applicants
- **International**: located outside India
- **Global**: remote, or open to applicants anywhere

Region is inferred from the location text, and an Indian location wins even when the role is also remote (so "India (Remote)" is India); a remote role without an Indian location is Global; everything else is International. Treat it as an inference, not a legal guarantee, and check the original page for actual eligibility.

By default the published index keeps only India and Global (remote) roles, so it reads as an India + remote quick-apply list. Run the scraper with `--all-regions` to include International roles as well.

## The classroom is not this page

Hardware Atlas is an index. It lists opportunities and links to the official page. It is not the application platform, and it does not apply on your behalf.

Always verify the original organization page before applying:

1. Open `official_url` on the opportunity.
2. Check eligibility, deadlines, and requirements on the page itself.
3. Apply through the organization's own application flow.

Deadlines and eligibility in this index come from what the source reported at `last_verified`. They can change without warning. Trust the organization, not the index.

## How the data is collected

The scraper runs in two parts:

- **ATS feeds**. Companies publish open roles through Greenhouse, Lever, and Ashby. These ATS vendors expose documented, public, read-only JSON endpoints. The scraper fetches those endpoints directly. No scraping of HTML, no logins, no CAPTCHAs, no rate-limit evasion.
- **Curated records**. Scholarships, fellowships, hackathons, and open source programs rarely have public JSON feeds. Those live as curated entries that maintainers verify by hand. Curated entries are marked with `"source": "curated"`.

Every record keeps its original `official_url` untouched. The scraper does not fabricate deadlines, eligibility, salaries, or recurrence. Fields it cannot confirm are left `null` or absent, and `last_verified` records when a source was checked.

## Recurring opportunities

Recurring programs are stored as a series, not a pile of lookalike rows:

```json
{
  "series": "Google Summer of Code",
  "edition": 2026,
  "recurring": true
}
```

Different editions of the same series are kept as separate records if they can be distinguished. If a program's recurrence cannot be confirmed, it is not marked `recurring`.

## How automatic updates work

A GitHub Actions workflow runs the scraper on a schedule. It:

1. Fetches ATS feeds
2. Normalizes and classifies the data
3. Deduplicates records
4. Validates the JSON
5. Runs the test suite
6. Commits and pushes only when the generated file actually changed

See [the scraper README](scraper/README.md) for the pipeline and [the workflow](../.github/workflows/update-opportunities.yml) for the schedule.

## How to verify an opportunity

Every record has a `source` and a `last_verified`. You can check whether a listing is still live by opening `official_url`. If the role has closed or the details changed, update or remove the entry.

Retention rule: ATS-derived roles are replaced wholesale on every run. A job that is no longer published simply disappears, which is correct. Curated records that are past their deadline and not recurring are dropped. Closed editions of recurring programs are kept for up to one year, so the series history survives for tracking. Anything older is removed.

## How to add or correct an opportunity

Two ways:

1. **Curated records**. For fellowships, scholarships, hackathons, and open source programs, add an entry to [`scraper/curated.json`](scraper/curated.json) in the same schema, with `"source": "curated"` and a stable `source_id`. The next scheduled run picks it up.
2. **ATS companies**. For a company whose open roles should be tracked, add its ATS slug to the bootstrap lists in [`scraper/config.py`](scraper/config.py). You need to know which ATS the company uses and its public board slug. The careers site URL reveals this. Example: `boards.greenhouse.io/shieldai` means Greenhouse slug `shieldai`.

Contributors should follow the usual [contribution guidelines](../CONTRIBUTING.md), and quality matters here as much as it does in lessons: correct sourcing, structural legitimacy, useful classification, and a valid official URL that actually points at the opportunity.

## Scope

The current sources cover a bounded, hand-verified set of companies and programs. That is deliberate. The architecture is built to grow a few entries at a time without a redesign, and quality is preferred over volume.