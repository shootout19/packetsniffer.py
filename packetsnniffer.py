import socket
import struct

sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
sniffer.bind(("192.168.209.170", 0)) # enter IP address here
sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

while True:
    packet, addr = sniffer.recvfrom(65565)
    ip_header = packet[:20]
    unpacked_header = struct.unpack("!BBHHHBBH4s4s", ip_header)
    source_ip = socket.inet_ntoa(unpacked_header[8])
    dest_ip = socket.inet_ntoa(unpacked_header[9])
    
    protocol = unpacked_header[6]
    if protocol == 6:
        protocol_name = "TCP"
    elif protocol == 17:
        protocol_name = "UDP"
    else:
        protocol_name = "Other"

    print(f"Source IP: {source_ip}, Destination IP: {dest_ip}, Protocol: {protocol_name}")
    if protocol == 6 or protocol == 17:
        transport_header = packet[20:40]
        source_port, dest_port = struct.unpack("!HH", transport_header[:4])
        print(f"Source Port: {source_port}, Destination Port: {dest_port}")
    
    print("-" * 50)