counts = {}

with open("auth.log") as file:
    for line in file:
        if "Failed password" in line:
            words = line.split()
            ip = words[10]  # the IP address is item 10 (python counts from 0)
            counts[ip] = counts.get(ip, 0) + 1
print(counts)