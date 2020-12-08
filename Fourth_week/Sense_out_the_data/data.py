#! /usr/bin/env python3

import sys
import re

logFile = sys.argv[1]
pattern = r"USER \((\w+)\)$"
usernames = {}

with open(logFile) as f:
    for line in f:
        if "CRON" not in line:
            continue
        result = re.search(pattern, line)
        if result is None:
            continue
        name = result[1]
        usernames[name] = usernames.get(name, 0) + 1
print(usernames)