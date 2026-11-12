# Failed Login Detector

A Python script that reads a Linux SSH authentication log and flags possible brute force attacks.

I built this to understand how a security team spots someone trying to break in over SSH. In my university Network Security module I set up SSH keys on Cisco devices, and I wanted to see the other side: how failed logins look in a log, and how an analyst turns them into alerts.

## What it does

1. Reads `auth.log` line by line.
2. Finds every `Failed password` line and pulls out the source IP address.
3. Counts failed logins for each IP.
4. Raises an **ALERT** when an IP reaches 5 or more failures (possible brute force).
5. Raises a **CRITICAL** alert when an IP that has already failed 5 or more times then logs in successfully, because the account may be compromised.

The threshold is a setting at the top of the script (`THRESHOLD = 5`). A lower number catches more attacks but also flags more users who simply mistyped their password (false positives).

## How to run it

You need Python 3.

```
python detector.py
```

## Example output

```
CRITICAL: 198.51.100.7 logged in after 5 failed attempts, account may be compromised
{'203.0.113.45': 6, '192.168.1.35': 1, '198.51.100.7': 5, '192.0.2.88': 3}
ALERT: 203.0.113.45 had 6 failed logins, possible brute force
ALERT: 198.51.100.7 had 5 failed logins, possible brute force
```

The sample `auth.log` is made up for testing and uses private and documentation IP ranges, not real addresses.

## Why the alerts say "possible"

The script only sees numbers, not intent. Five failures could be an attacker or a user who forgot their password, so a real analyst would check before acting.

## Next steps

- Add a 10 minute time window, so 5 failures spread over a month are not treated the same as 5 failures in a minute
- Save alerts to a report file, tagged with MITRE ATT&CK technique T1110 (Brute Force)

## What I learned

- How an SSH log line is structured (time, server, service, result, username, IP)
- Python basics: reading files, loops, `split()`, dictionaries and f-strings
- Detection thinking: thresholds, false positives and why one signal is not proof
- Git basics: staging, committing and pushing changes
