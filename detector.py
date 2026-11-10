with open("auth.log") as file:
    for line in file:
        if "Failed password" in line:
            words = line.split()
            ip = words[10]  # Assuming the IP address is the 12th word in the line
            print(ip) 