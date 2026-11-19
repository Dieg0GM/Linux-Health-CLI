"""Read-only Linux health snapshot. No third-party dependencies."""
import argparse
import json
import os
from pathlib import Path
import shutil


def parse_meminfo(text: str) -> dict[str, int]:
    values = {}
    for line in text.splitlines():
        if ":" not in line:
            continue
        key, raw = line.split(":", 1)
        parts = raw.strip().split()
        if parts and parts[0].isdigit():
            values[key] = int(parts[0]) * (1024 if len(parts) > 1 and parts[1] == "kB" else 1)
    return values


def snapshot(root: str = "/") -> dict:
    memory = parse_meminfo(Path("/proc/meminfo").read_text())
    disk = shutil.disk_usage(root)
    uptime = float(Path("/proc/uptime").read_text().split()[0])
    total = memory.get("MemTotal", 0)
    available = memory.get("MemAvailable", 0)
    return {
        "hostname": os.uname().nodename,
        "load_average": list(os.getloadavg()),
        "uptime_seconds": round(uptime, 1),
        "memory_total_bytes": total,
        "memory_used_bytes": max(0, total - available),
        "disk_total_bytes": disk.total,
        "disk_used_bytes": disk.used,
        "disk_used_percent": round(disk.used / disk.total * 100, 1) if disk.total else 0,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Read-only Linux health snapshot")
    parser.add_argument("--json", action="store_true", help="Print formatted JSON")
    args = parser.parse_args()
    result = snapshot()
    print(json.dumps(result, indent=2) if args.json else "\n".join(f"{k}: {v}" for k, v in result.items()))
