# DFS Autonomy Lab

A sandbox for proving an approval-gated, autonomous development loop with Claude Code routines.

## How it works

1. Andrew writes an issue (use the **Task for Claude** template) and adds the `approved-for-claude` label.
2. The **DFS Issue Runner (manual)** routine is started by hand.
3. Claude picks the oldest approved issue, works on a `claude/issue-<n>-…` branch, runs the tests, and opens a PR with a report.
4. Andrew reviews and merges. Claude never merges.

| Label | Meaning |
|---|---|
| `approved-for-claude` | Ready for Claude. Applied by Andrew only. |
| `claude-in-progress` | A run is working on it. |
| `claude-pr-ready` | Done; PR waiting for review. |
| `claude-blocked` | Claude stopped; see the issue comment for what's needed. |

Rules Claude follows: [CLAUDE.md](CLAUDE.md). The routine's exact prompt: [ROUTINE_PROMPT.md](ROUTINE_PROMPT.md).

## Tests

```bash
python3 -m unittest discover -s tests -t . -v
```
