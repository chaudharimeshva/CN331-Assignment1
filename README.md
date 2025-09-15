# CN331 – Computer Networks (Assignment 1)

## Overview
This project implements two main tasks:

## **Task 1 – Custom DNS Resolver**
- The client reads DNS queries from a **PCAP file**.
- A **custom header** (format: `HHMMSSID`) is added to each query.
- The modified query is sent to the server.
- The server applies a **time-slot + modulo rule** to map the query to one of the IP addresses from a **15-IP pool**.
- The results are displayed and stored in a CSV file (`dns_results.csv`).


---

### File Structure

|-> client.py            # Client code

|-> server.py            # Server code 

|-> 9.pcap               # Sample PCAP file ((075+044=119)%10=9) 

|-> dns_results.csv      # DNS results output (Task-1) 

|-> report.pdf           # Final report 

|-> README.md            # Instructions

---

## Requirements
- **Python 3.x**
- Libraries:
  - `scapy`
  - `socket` (built-in)
  - `csv` (built-in)

To install scapy:
```bash
pip install scapy
```


## **Task 2 – Traceroute Protocol Behavior**

- Experiments are performed using:
  - **Windows** → `tracert` command
  - **Linux** → `traceroute` command
- Network traffic is captured with **Wireshark** (Windows) or **tcpdump** (Linux).
- Observations are made about:
  - Protocol differences (ICMP in Windows vs UDP in Linux by default).
  - Path variations and the effect of firewalls.

