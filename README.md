# CN331-Computer Networks Assignment1
## Overview
this Project implemens:
1. Custom DNS Resolver (Task-1)
   - Client parses DNS queries from a PCAP file.
   - Adds a custom header (HHMMSSID).
   - Sends query + header to server.
   - Server applies time-slot + modulo rule to resolve into IP from a 15-IP pool.
   - Results are logged in CSV format (dns_results.csv).
2. Traceroute Protocol Behavior (Task-2)
   - Experiments with tracert (Windows) and traceroute (Linux).
   - Captured outputs using Wireshark/tcpdump.
   - Observed protocol differences and firewall effects.

## Project Structure
CN_Assignment1/
├── client.py          # Client code 

├── server.py          # Server code

├── 1.pcap             # Sample PCAP file (chosen based on roll no rule)

├── dns_results.csv    # DNS results output (Task-1)

├── report.pdf         # Final report

└── README.md          # Instructions

## Requirements
- Python 3.x
- Libraries:
    - scapy
    - socket(built-in)
    - csv(built-in)
We can install scapy by,
          pip install scapy

## Task-1:
### How to Run
- Strat the server
    In terminal(command prompt),
      python server.py
    You can see,server running... waiting for client
- Run the Client
    In terminal(command prompt),
      pythone client.py
    The client will:
    - read 1.pcap
    - Extract DNS queries
    - Add headers and send them to server
    - Print result and save them to dns_results.csv

### Sample Output

## Task-2:


  
