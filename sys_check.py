#!/usr/bin/env python3
"""Simple system check tool using standard library only."""
import os
import shutil
import time

def check():
    # Disk
    disk = shutil.disk_usage('/')
    disk_percent = (disk.total - disk.free) / disk.total * 100
    print(f"Disk: {disk_percent:.1f}%")

    # Time
    print(f"Time: {time.strftime('%Y-%m-%d %H:%M:%S')}")

    # Load average (Linux specific, but works on most Unix-like)
    try:
        load = os.getloadavg()
        print(f"Load avg: {load[0]:.2f}")
    except OSError:
        pass

    # Memory (Linux)
    try:
        with open('/proc/meminfo') as f:
            lines = f.readlines()
        mem_total = int(lines[0].split()[1])
        mem_free = int(lines[1].split()[1])
        mem_available = int(lines[2].split()[1]) if len(lines) > 2 else mem_free
        print(f"Mem: {mem_available // 1024} MB free / {mem_total // 1024} MB total")
    except OSError:
        pass

if __name__ == '__main__':
    check()
