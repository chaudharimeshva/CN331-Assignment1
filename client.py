import socket
from scapy.all import rdpcap, DNS
import datetime
import csv

# Function for custom header
def make_header(seq_id):
    now = datetime.datetime.now()
    return now.strftime("%H%M%S") + f"{seq_id:02d}"

# Load PCAP
pcap_file = "C:/Users/chaud/OneDrive/Desktop/CN_Assignment1/1.pcap"
packets = rdpcap(pcap_file)

# Extract DNS queries only
dns_queries = [p for p in packets if p.haslayer(DNS) and p[DNS].qr == 0]

# Connect to server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 9999))

# Open CSV file to write results
with open("dns_results.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Custom Header", "Domain", "Resolved IP"])  # CSV header row

    # Loop through DNS queries
    for i, q in enumerate(dns_queries):
        header = make_header(i)                 # custom header
        packet_bytes = bytes(q)
        message = header.encode() + packet_bytes
        s.send(message)

        # Receive response
        response = s.recv(1024).decode()

        # Extract domain name for report
        domain = q[DNS].qd.qname.decode().strip(".")
        resolved_ip = response.split()[-1]  # last word after "Resolved:"

        # Print for verification
        print(f"{header} | {domain} | {resolved_ip}")

        # Save row in CSV file
        writer.writerow([header, domain, resolved_ip])

s.close()
