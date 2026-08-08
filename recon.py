#!/usr/bin/env python3
"""
Port Recon — A fast TCP connect scanner for discovering open doors.
Usage: python3 recon.py <target_ip> [start_port] [end_port]
"""

import socket
import sys
from concurrent.futures import ThreadPoolExecutor

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"[+] Port {port} OPEN")
        sock.close()
    except Exception:
        pass

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 recon.py <target_ip> [start_port] [end_port]")
        sys.exit(1)
    target = sys.argv[1]
    start_port = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    end_port = int(sys.argv[3]) if len(sys.argv) > 3 else 1024

    print(f"[*] Scanning {target} from {start_port} to {end_port}...")
    with ThreadPoolExecutor(max_workers=100) as executor:
        for port in range(start_port, end_port+1):
            executor.submit(scan_port, target, port)
    print("[*] Recon complete.")
