import re

print(re.search(r".com", "welcome"))
print(re.search(r"\.com", "welcome"))
print(re.search(r"\.com", "mydomain.com"))

#When we see a pattern that includes a backslash, it coul be escaping a special regex character or a special string character

#\w matches any alphanumeric character
#\d matches digits
#\s matches whitespace characters like space
#\b matches word boundaries

# www.regex101.com
print(re.search(r"\w*", "This is an example"))
print(re.search(r"\w*", "And_this_is_another"))