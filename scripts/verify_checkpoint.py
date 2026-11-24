"""Recompute the release's counts and within-frame weighted estimates."""
from collections import Counter, defaultdict
import csv
import json
from math import isclose
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VERDICTS = ("supported", "contradicted", "unresolved")
REASONS = {
    "definition": "Unclear definition or comparison",
    "partial_record": "Records cover only part",
    "missing_record": "No direct public record found",
    "transcript": "Spoken wording unverified",
    "causation": "Cause not established",
}
DIRECTIONS = {"positive", "negative", "mixed", "undetermined"}


def read_csv(name):
    with (ROOT / "data" / name).open(newline="", encoding="utf-8") as stream:
        return list(csv.DictReader(stream))


def require(condition, message):
    if not condition:
        raise ValueError(message)


def verify():
    report = json.loads((ROOT / "reports/findings.json").read_text(encoding="utf-8"))
    events = read_csv("events.csv")
    claims = read_csv("investigations.csv")
    combined = report["combined"]
    require(len(events) == len({row["event_id"] for row in events}) == combined["events"],
            "Event count or event IDs differ")
    require(len(claims) == len({row["claim_id"] for row in claims}) == combined["completed"],
            "Investigated count or claim IDs differ")

    by_event = defaultdict(Counter)
    reasons, directions = Counter(), Counter()
    scopes = {row["event_id"]: row["study_scope"] for row in events}
    for claim in claims:
        event, verdict = claim["event_id"], claim["verdict"]
        require(scopes.get(event) == claim["study_scope"] and verdict in VERDICTS, claim["claim_id"])
        by_event[event][verdict] += 1
        reason, direction = claim["unresolved_reason"], claim["rhetorical_direction"]
        if verdict == "unresolved":
            require(reason in REASONS and direction in DIRECTIONS, claim["claim_id"])
            reasons[REASONS[reason]] += 1
            directions[direction] += 1
        else:
            require(not reason and not direction, claim["claim_id"])

    inventory = pending = main_inventory = 0
    weighted_totals = Counter()
    main_events = [event for event in events if event["study_scope"] == "main"]
    require(len(main_events) == len(report["aggregate"]["events"]), "Main frame count differs")
    for event in events:
        counted = by_event[event["event_id"]]
        n, size = int(event["investigated"]), int(event["inventoried"])
        outside = int(event["outside_sample"])
        require(0 < n <= size and n == sum(counted.values()) and outside == size - n,
                event["event_id"])
        require(all(counted[key] == int(event[key]) for key in VERDICTS), event["event_id"])
        inventory += size
        pending += outside
        if event["study_scope"] == "main":
            main_inventory += size
            for key in VERDICTS:
                weighted_totals[key] += size * counted[key] / n

    require(inventory == combined["inventory"] and pending == inventory - len(claims),
            "Inventory or outside-sample count differs")
    require(dict(Counter(claim["verdict"] for claim in claims)) ==
            {key: combined[key] for key in VERDICTS}, "Combined verdict counts differ")
    require(dict(reasons) == report["unresolved_reasons"], "Unresolved reasons differ")
    require(dict(directions) == report["unresolved_direction"]["counts"], "Wording counts differ")
    require(main_inventory == report["aggregate"]["inventory"], "Main inventory differs")
    for key in VERDICTS:
        estimate = report["aggregate"]["rates"]["all"][key]["estimate"]
        require(isclose(weighted_totals[key] / main_inventory, estimate, abs_tol=1e-12), key)

    share = combined["unresolved"] / combined["completed"]
    require(isclose(share, report["unresolved_goal"]["unresolved_share"]), "Unresolved share differs")
    print(f"{combined['completed']:,} investigated across {combined['events']} events")
    print(f"{combined['unresolved']:,} unresolved ({share:.2%})")
    print(f"{pending:,} occurrences outside the investigated sample")
    print(f"{weighted_totals['unresolved'] / main_inventory:.1%} weighted unresolved share in the main frames")


if __name__ == "__main__":
    verify()
