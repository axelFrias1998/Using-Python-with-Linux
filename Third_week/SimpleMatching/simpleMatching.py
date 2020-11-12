import re

#The r character before a string, indicates that it is a raw string
#Is a good idea to always use raw strings for regular expressions in Python
result = re.search(r"aza", "plaza")
print(result)
result = re.search(r"aza", "bazaar")
print(result)
result = re.search(r"aza", "maze")
print(result)

print(re.search(r"^x", "xenon"))
print(re.search(r"p.ng", "clapping"))

def check_aei(text):
    result = re.search(r"a.e.i", text)
    return result != None

print(check_aei("academia"))
print(check_aei("aerial"))
print(check_aei("paramedic"))

print(re.search(r"p.ng", "Pangaea", re.IGNORECASE))