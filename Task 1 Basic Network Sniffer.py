from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP, ICMP
from scapy.layers.l2 import Ether

# Packet handler function
def packet_handler(packet):
    print("\n=== New Packet Captured ===")

    # Ethernet Layer
    if Ether in packet:
        eth = packet[Ether]
        print(f"Ethernet -> Source: {eth.src}, Destination: {eth.dst}, Type: {hex(eth.type)}")

    # IP Layer
    if IP in packet:
        ip = packet[IP]
        print(f"IP -> Source: {ip.src}, Destination: {ip.dst}, Protocol: {ip.proto}")

        # TCP
        if TCP in packet:
            tcp = packet[TCP]
            print(f"TCP -> Source Port: {tcp.sport}, Destination Port: {tcp.dport}, Flags: {tcp.flags}")

        # UDP
        elif UDP in packet:
            udp = packet[UDP]
            print(f"UDP -> Source Port: {udp.sport}, Destination Port: {udp.dport}")

        # ICMP
        elif ICMP in packet:
            icmp = packet[ICMP]
            print(f"ICMP -> Type: {icmp.type}, Code: {icmp.code}")

# Main sniffer function
def start_sniffing(interface=None):
    print("Starting network sniffer...")
    sniff(prn=packet_handler, iface=interface, store=False)

# Entry point
if __name__ == "__main__":
    import os
    import platform

    # Check for admin/root
    if os.name != "nt" and os.geteuid() != 0:
        print("❌ Please run as root (e.g., sudo python network_sniffer.py)")
    else:
        # You can specify interface='eth0' or leave as None for default
        interface = None
        if platform.system() == "Windows":
            print("⚠️ On Windows, only supported interfaces will work (try using Wireshark for better support).")
        start_sniffing(interface)
