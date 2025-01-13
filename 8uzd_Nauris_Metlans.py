import re

file = open("/var/log/messages" , "r")
content = file.readlines()
file.close

print("USB informācija no /var/log/messages faila:\n")
for line in content:
    if "usb" in line:
        print(line)
    else:
        continue

print("Filtrēta USB informācija no /var/log/messages faila:\n")
for line in content:
    if "usb" in line:
        match = re.search(r"(^\w+ \d+ \d+:\d+:\d+).*: (.*)", line)
        if match:
            print(match.group(1) + " " + match.group(2) + "\n")
    else:
        continue
