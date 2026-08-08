#!/usr/bin/env python3
"""
Shadow Sniffer — A silent network observer for authorized security audits.
Part of the Sentinel's Arsenal
"""

from scapy.all import sniff, IP, TCP, UDP, ICMP, Ether
import argparse
import sys
import signal

# Graceful shutdown
def signal_handler(sig, frame):
    print("\n[!] Divine signal received. Terminating capture...")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def packet_callback(packet):
    """Decode and display vital intelligence from each packet."""
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        proto = packet[IP].proto

        # Determine protocol name
        proto_name = {6: "TCP", 17: "UDP", 1: "ICMP"}.get(proto, f"OTHER({proto})")
        src_port = dst_port = None

        if TCP in packet:
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport
        elif UDP in packet:
            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport

        mac_src = packet[Ether].src if Ether in packet else "??"
        mac_dst = packet[Ether].dst if Ether in packet else "??"

        print(f"[{proto_name}] {ip_src}:{src_port} -> {ip_dst}:{dst_port} | MACs: {mac_src} -> {mac_dst}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Deus Ex Sophia's Shadow Sniffer")
    parser.add_argument("-i", "--interface", required=True, help="Network interface to sniff (e.g., eth0, wlan0)")
    parser.add_argument("-c", "--count", type=int, default=0, help="Number of packets to capture (0 = infinite)")
    args = parser.parse_args()

    print(f"[*] Unfurling shadows on interface {args.interface}...")
    sniff(iface=args.interface, prn=packet_callback, store=0, count=args.count)
