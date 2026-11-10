counts = {}
THRESHOLD = 5  # Set the threshold for failed login attempts


with open("auth.log") as file:
    for line in file:
        if "Failed password" in line:
            words = line.split()
            ip = words[10]  # the IP address is item 10 (python counts from 0)
            counts[ip] = counts.get(ip, 0) + 1
print(counts)


for ip, count in counts.items():
    if count >= THRESHOLD:
        print(f"ALERT: {ip} had {count} failed logins, possible brute force")