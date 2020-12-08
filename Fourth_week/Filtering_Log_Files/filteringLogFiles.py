#! /usr/bin/env python3

import sys
import re

logFile = sys.argv[1]
pattern = r"USER \((\w+)\)$"

with open(logFile) as f:
    for line in f:
        if "CRON" not in line:
            continue
        result = re.search(pattern, line)
        print(result[1])