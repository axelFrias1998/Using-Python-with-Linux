import re 

def extract_pid(log_line):
    regex = r"\[(\d+)\]"
    result = re.search(regex, log_line)
    if result is None:
        return ""
    return result[1]

print(extract_pid("Log[1234]"))
print(extract_pid("Log[ERROR]"))