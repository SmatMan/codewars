import re

def increment_string(strng):
    if re.findall("(\d+)$", strng) == []:
        return strng + "1"
    match = re.findall(r"(.*?)(\d+)$", strng)[0]
    base = match[0]
    match = match[1]
    zeros = len(match)
    print(zeros)
    if match:
        match=int(match)
        match += 1
        match = f"{base}{str(match).zfill(zeros)}"
        return match