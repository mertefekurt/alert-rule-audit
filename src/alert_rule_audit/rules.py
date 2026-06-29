from __future__ import annotations

from alert_rule_audit.models import Rule

PROJECT_NAME = 'alert-rule-audit'
DESCRIPTION = 'Audit alert rules for noise, missing runbooks, and weak severity.'
TEXT_FIELDS = ("text", "content", "description", "summary", "body", "notes", "message")
SUBJECT_FIELDS = ("id", "name", "service", "dataset", "route", "metric", "field", "path")
HIGH_SAMPLE = 'alert HighErrors severity warning for 1m runbook missing threshold any'
MEDIUM_SAMPLE = '\\b(for|window)\\s*[:=]?\\s*1m\\b'
CLEAN_SAMPLE = 'alert CheckoutErrors severity page for 10m runbook https://runbooks/checkout'

RULES = (
    Rule(
        code='missing-runbook',
        severity='high',
        pattern='\\b(runbook\\s*[:=]\\s*(missing|none|null)|runbook missing)\\b',
        message='paging alert has no runbook',
        recommendation='Attach a runbook with diagnosis and rollback steps.',
    ),
    Rule(
        code='short-window',
        severity='medium',
        pattern='\\b(for|window)\\s*[:=]?\\s*1m\\b',
        message='alert window may be too short',
        recommendation='Use a longer window or burn-rate style condition.',
    ),
    Rule(
        code='weak-severity',
        severity='low',
        pattern='\\bseverity\\s*[:=]\\s*(warn|warning|info)\\b',
        message='alert severity may be too weak for paging',
        recommendation='Check that severity matches user impact.',
    ),
)
