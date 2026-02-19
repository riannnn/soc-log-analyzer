from collections import defaultdict

log_file = "logs/access.log"

ip_count = defaultdict(int)
status_count = defaultdict(int)

with open(log_file, "r") as file:
    for line in file:
        parts = line.split()
        ip = parts[0]
        status = parts[-1]

        ip_count[ip] += 1
        status_count[status] += 1

print("=== Log Analysis Report ===\n")

print("Top IP Activity:")
for ip, count in sorted(ip_count.items(), key=lambda x: x[1], reverse=True):
    print(f"{ip} → {count} requests")

print("\nHTTP Status Summary:")
for status, count in status_count.items():
    print(f"Status {status} → {count} times")

print("\nSuspicious Activity Detection:")
for ip, count in ip_count.items():
    if count > 4:
        print(f"⚠ Possible brute force or abuse detected from IP: {ip}")
