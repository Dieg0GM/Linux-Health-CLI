# Linux Health CLI

A lightweight, read-only Linux health snapshot tool built with Python's standard library.

## Run

```bash
python3 health.py --json
python3 -m unittest discover -s tests -v
```

Reports CPU load, memory usage, uptime and filesystem capacity. No sudo required. Linux `/proc` is required for memory and uptime.

## Learning challenges

1. Add a warning threshold for disk usage.
2. Add a `--output` option to save a JSON report.
3. Add tests for missing `/proc` files.

**Status:** Starter implementation. Extend and explain it yourself in Codespaces.
