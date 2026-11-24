# Presidential speech analysis

This study tracks evidence for factual claims in Donald Trump’s sampled presidential remarks. This repository contains the verified results at the research pause on **20 November 2026**, checkpoint **1228**. The evidence cutoff was **12 November 2026 at 19:44:39 UTC**.

## Findings

| Coverage | Claim occurrences |
| --- | ---: |
| Inventoried across 57 events | 21,164 |
| Investigated | 1,825 |
| Outside the investigated sample | 19,339 |

| Verdict | Count |
| --- | ---: |
| Supported | 732 |
| Contradicted | 257 |
| Unresolved | 836 (45.81%) |

The combined counts include 55 main speech frames and two comparison samples. The weighted unresolved estimate within the 55 main frames is **49.9%**, with a conservative 95% design interval of **23.8% to 75.9%**. These results reflect provisional machine review of the studied speeches.

Investigators revisited **518** distinct previously unresolved claims. Evidence changed **87** verdicts, with 43 becoming supported and 44 contradicted. Among the 836 still unresolved, 336 have a partial public record, 280 have an unclear definition or comparison, 153 lack a direct public record, 65 lack evidence for causation, and two have unverified spoken wording.

## Explore the results

- [Findings and charts](reports/findings.md) · [HTML report](reports/findings.html) · [Numerical data](reports/findings.json)
- [Methodology and limits](docs/methodology.md) · [Selected evidence notes](docs/evidence-notes.md)
- [Event-level counts](data/events.csv) · [Investigation outcomes](data/investigations.csv)
- [Project status and resumption](STATUS.md)

Verify the file checksums with `sha256sum -c SHA256SUMS` and reproduce the headline counts and weighted estimate with `python3 scripts/verify_checkpoint.py`. The CSVs contain occurrence IDs and outcomes. The research workspace holds the full case ledger, transcript and source snapshots, and in-progress review artifacts.
