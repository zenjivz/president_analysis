# Methodology

## Speech and claim selection

The main sample covers public or credentialed-press presidential addresses with a verified opening monologue of at least 500 words. The event records preserve timing, public access, transcript completeness and remaining eligibility uncertainties. Lincoln Memorial and the CPAC dinner excerpt are comparison samples.

Reviewers independently extracted factual propositions from each scoped transcript and reconciled omissions and overlaps against the source before sampling. Each occurrence is a checkable assertion with a fixed meaning, time and scope. Deliberate repetitions remain separate occurrences. Questions, other speakers and nonfactual rhetoric are excluded from the extraction frame.

Within a speech frame, the study used seeded random draws without replacement. Smaller frames can be fully investigated, and later seeded draws sampled additional occurrences from previously audited frames. The two comparison samples contribute 25 investigations each. Occurrences outside the investigated sample remain pending.

## Evidence and judgments

Primary and blind skeptical reviewers searched independently for evidence supporting and challenging the same proposition. The research archive preserves retrieval logs, source URLs, publication dates, exact excerpts and locators. Evidence used in judgments was limited to material available by **12 November 2026 at 19:44:39 UTC**. Publication after a speech can establish an earlier fact and is recorded separately from evidence available at delivery.

- **Supported** means credible evidence supports the assertion within its recorded scope.
- **Contradicted** means credible evidence materially conflicts with that assertion.
- **Unresolved** means the completed investigation could not establish a verdict. This can arise from an undefined term or baseline, partial or missing public records, uncertain wording, or an unestablished causal link.

Targeted rechecks began with unresolved cases that had a specific documentary lead. A revision required agreement from two independent passes and decisive dated evidence addressing the fixed claim. The original random sample membership and reference time were preserved. The revision rate applies to the targeted cases.

## Estimation and limits

The combined raw share counts each investigated occurrence once, including the comparisons. For the 55 eligible main frames, the weighted estimate uses each speech's inventory size to weight its within-speech sample share. The conservative 95% design interval inverts an exact finite-population hypergeometric distribution within each speech and combines the endpoints with a Bonferroni adjustment for one status at a time.

These intervals describe sampling uncertainty conditional on the studied frames and machine judgments. Event discovery, transcript and extraction quality, and evidence interpretation can introduce additional uncertainty. The weighted results describe the studied speech frames.

The secondary chart codes the wording of unresolved claims as positive, negative, mixed, or undetermined. The labels describe the speaker’s framing. Audience attitudes and behavioral effects were not measured.

## Data files

[Event counts](../data/events.csv) give frame sizes and verdict totals for each speech or comparison. [Investigation outcomes](../data/investigations.csv) give one row per investigated occurrence. Reason and rhetorical direction are populated for unresolved rows. [Report data](../reports/findings.json) contains design intervals, recheck totals and chart inputs.
