#!/usr/bin/env python3
"""Simple system check tool using standard library only."""
import os
import shutil
import time
import subprocess

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

if __name__ == '__main__':
    check()
