#!/usr/bin/env python3
"""Add subjects from existing task script.json files to the Roll subject ledger."""

import argparse

from app.services import task


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--limit", type=int, default=10000, help="maximum task directories to scan"
    )
    args = parser.parse_args()

    _, subjects = task.collect_subject_history(limit=max(1, args.limit))
    added = sum(task.reserve_generated_subject(subject) for subject in subjects)
    print(f"Scanned {len(subjects)} known subjects; added {added} to the generated-subject ledger.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
