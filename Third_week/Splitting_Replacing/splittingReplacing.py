import re

print(re.split(r"[.?!]", "One sentence. Another sentence! The last sentence?"))
print(re.split(r"([.?!])", "One sentence. Another sentence! The last sentence?"))

print(re.sub(r"[\w.%+-]+@[\w.-]+", "[REDACTED]", "Received an email for go_nuts95@my.example.com"))
#Capturing groups used for changing the order of the words. The number indicates the number of matchreference at the expression.
print(re.sub(r"^([\w .-]*), ([\w .-]*)$", r"\2 \1", "Locelace, Ada"))

def transform_record(record):
    new_record = re.sub(r"([\d-]+)", r"+1-\1", record)
    return new_record

def multi_vowel_words(text):
    pattern = r"\w*[aeiou]{3,}\w*"
    result = re.findall(pattern, text)
    return result

def transform_comments(line_of_code):
    result = re.sub(r"([#]+) (\w+)", r"// \2", line_of_code)
    return result

def convert_phone_number(phone):
    result = re.sub(r"(\d{3,})-(\d{3,})-(\d{4,})", r"(\1) \2 \3", phone)
    return result