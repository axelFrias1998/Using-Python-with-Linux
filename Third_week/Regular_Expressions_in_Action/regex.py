#! /usr/bin/env python3

import re

#Getting all the countries.
#Starts with an A = ^A
#Followed by any characters = .+
#Ends with an a = a$
print(re.search(r"^A.+a$", "Alemania"))
print(re.search(r"^A.+a$", "Azerbaijan"))
print(re.search(r"^A.+a$", "Australia"))

pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"

print(re.search(pattern, "_this_is_a_valid_variable_name"))
print(re.search(pattern, "this isn't a valid variable name"))
print(re.search(pattern, "_my_variable1"))
print(re.search(pattern, "2my_variable"))