#!/usr/bin/env python3

import os
import datetime

#An Unix Timestamp represents the number of seconds since January 1st, 1970
print(os.path.getsize("spider.txt"))
print(os.path.getmtime("spider.txt"))
timestamp = os.path.getmtime("spider.txt")
print(datetime.datetime.fromtimestamp(timestamp))
print(datetime.datetime(2020, 1, 6, 7, 2, 3, 899999))

print(os.path.abspath("spider.txt"))
