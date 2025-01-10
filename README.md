# Packet Sniffer

## **Overview**
This script is a basic packet sniffer that captures network packets and shows important details like the source IP, destination IP, protocol type (TCP, UDP, etc.), and source and destination ports (if available). It is made for educational purposes to help understand how packet sniffing and network protocols work.

## **Features**
- Captures all incoming and outgoing packets on the specified network interface.
- Extracts and displays:
  - Source and Destination IP addresses.
  - Protocol type (TCP, UDP, or Other).
  - Source and Destination ports (for TCP and UDP).
- Easy to understand and beginner-friendly.

## **Setup and Usage**
1. Clone this repository:
   ```bash
   git clone https://github.com/shootout19/packetsniffer.py.git
   cd packetsniffer
2. Open the script (`packetsniffer.py`) and replace "192.168.x.x" with your local IP address in the `sniffer.bind()` line.
3. Run the script:
   ```bash
   python packetsnniffer.py
4. The script will display captured packet details in the terminal.
   ```bash
   # output
   Source IP: 192.168.209.1, Destination IP: 192.168.209.170, Protocol: TCP
   Source Port: 443, Destination Port: 51623
   --------------------------------------------------
   Source IP: 8.8.8.8, Destination IP: 192.168.209.170, Protocol: UDP
   Source Port: 53, Destination Port: 62000
   --------------------------------------------------
