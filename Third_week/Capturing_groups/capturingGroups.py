#! /usr/bin/env python3

import re

#Capturing groups are portions of the pattern that are enclosed in parentheses
result = re.search(r"^(\w*), (\w*)$", "Lovelace, Ada")
print(result)
print(result.groups())

print(result[0])
print(result[1])
lastName, firstName = result.groups()
print("{}, {}".format(lastName, firstName))
print("{}, {}".format(result[1], result[2]))

def rearrange_name(name):
    r = re.search(r"^([\w \.-]), ([\w \.-]*)$", name)
    if r is None:
        return name
    return "{} {}".format(r[2], r[1])

rearrange_name("Frias Axel")