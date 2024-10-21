import requests
ip = '8.8.8.8'

try:
    response = requests.get("https://" + ip, timeout=5)
    print(f"{ip} is reachable")
except requests.exceptions:
    print(f"Failed to reach {ip}")

