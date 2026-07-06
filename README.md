# Alert Rule Audit

Audit alert rules for noise, missing runbooks, and weak severity.

## First impression

![Alert Rule Audit cover](assets/readme-cover.svg)

When this tool reports something, I want the finding to be boringly explicit: what matched, how severe it is, and what a reviewer should clean up.

## Tripwires

- `missing-runbook` (high): paging alert has no runbook. Fix: Attach a runbook with diagnosis and rollback steps..
- `short-window` (medium): alert window may be too short. Fix: Use a longer window or burn-rate style condition..
- `weak-severity` (low): alert severity may be too weak for paging. Fix: Check that severity matches user impact..

## Runbook

```bash
git clone https://github.com/mertefekurt/alert-rule-audit.git
cd alert-rule-audit
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
```

Then:

```bash
alert-rule-audit examples/sample.txt
alert-rule-audit examples/sample.txt --json
```

## Development note

The policy lives in `rules.py`; parsing and rendering stay separate so the rule list is easy to audit.
