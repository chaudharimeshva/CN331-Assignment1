import socket

# IP pool of 15 addresses
ip_pool = [
    "192.168.1.1", "192.168.1.2", "192.168.1.3", "192.168.1.4", "192.168.1.5",
    "192.168.1.6", "192.168.1.7", "192.168.1.8", "192.168.1.9", "192.168.1.10",
    "192.168.1.11", "192.168.1.12", "192.168.1.13", "192.168.1.14", "192.168.1.15"
]

def resolve_dns(header, query_packet):
    """
    Resolve DNS query using custom header (HHMMSSID) and rule set
    """
    try:
        # Extract hour and ID from header
        hour = int(header[:2])   # HH
        query_id = int(header[-2:])  # ID (last 2 digits)

        # Decide time slot
        if 4 <= hour <= 11:   # Morning
            pool_start = 0
        elif 12 <= hour <= 19:  # Afternoon
            pool_start = 5
        else:   # Night (20–23 or 00–03)
            pool_start = 10

        # Pick IP from correct pool
        index = pool_start + (query_id % 5)
        resolved_ip = ip_pool[index]

    except Exception as e:
        print("Error resolving:", e)
        resolved_ip = "0.0.0.0"

    return resolved_ip

# --- Server socket setup ---
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 9999))   # localhost, port 9999
server.listen(1)

print("Server running... waiting for client")
conn, addr = server.accept()
print(f"Client connected: {addr}")

while True:
    data = conn.recv(2048)
    if not data:
        break

    # First 8 bytes = custom header
    header = data[:8].decode(errors="ignore")
    query = data[8:]  # raw DNS query bytes (not used for resolution here)

    resolved_ip = resolve_dns(header, query)

    print(f"Received header: {header} -> Resolved: {resolved_ip}")

    # Response back to client
    response = f"{header} | Resolved: {resolved_ip}"
    conn.send(response.encode())

conn.close()
