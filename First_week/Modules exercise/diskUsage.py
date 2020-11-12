#! /usr/bin/env python3

import shutil
import psutil
from connection import *

def check_disk_usage(disk):
    """verifies that there's enough free space on disk"""
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20

def check_cpu_usage():
    """Verigies that there's enough unused CPU"""
    usage = psutil.cpu_percent(1)
    return usage < 75

if not check_disk_usage('/') or not check_cpu_usage():
    print("ERROR!")
elif check_localhost() and check_connectivity():
    print("Everything is OK!")
else:
    print("Network checks failed")