<p align="center">
  <img src="assets/readme-cover.svg" alt="Alert Rule Audit cover" width="100%" />
</p>

# Alert Rule Audit

![stack](https://img.shields.io/badge/stack-Python-0891b2?style=flat-square) ![python](https://img.shields.io/badge/python-3.11-b45309?style=flat-square) ![license](https://img.shields.io/badge/license-MIT-be185d?style=flat-square) ![ci](https://img.shields.io/badge/ci-GitHub%20Actions-4b5563?style=flat-square)

Audit alert rules for noise, missing runbooks, and weak severity.

## Why it exists

Small review tasks are easy to skip when the signal lives in notes, spreadsheets, or loosely formatted exports. `alert-rule-audit` turns those checks into a repeatable command with plain findings and CI-friendly exit codes.

## Quick run

```bash
python -m pip install -e ".[dev]"
alert-rule-audit examples/sample.txt
alert-rule-audit examples/sample.txt --json --fail-on medium
```

## Rule set

| Rule | Severity | What it catches |
| --- | --- | --- |
| `missing-runbook` | high | paging alert has no runbook |
| `short-window` | medium | alert window may be too short |
| `weak-severity` | low | alert severity may be too weak for paging |

## Input

The reader accepts plain text, JSON, JSONL, and CSV. That keeps it useful for hand-written notes, review exports, and small automation jobs.

## Sample risky input

```text
examples/sample.txt
```

## Development

```bash
python -m pip install -e ".[dev]"
ruff check .
pytest
python -m alert_rule_audit --help
```

`cli.py` handles arguments, `core.py` reads and evaluates records, and `rules.py` keeps the Alert Rule Audit policy easy to review.
