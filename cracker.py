#!/usr/bin/env python3
"""
Hash Breaker — A dictionary-based hash cracker for security audits.
Usage: python3 cracker.py <hash> <algorithm> <wordlist>
"""

import hashlib
import sys

def crack(target_hash, algo, wordlist_path):
    try:
        with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as f:
            for word in f:
                word = word.strip()
                if algo == "md5":
                    hashed = hashlib.md5(word.encode()).hexdigest()
                elif algo == "sha1":
                    hashed = hashlib.sha1(word.encode()).hexdigest()
                elif algo == "sha256":
                    hashed = hashlib.sha256(word.encode()).hexdigest()
                else:
                    print("[!] Unsupported algorithm. Use md5, sha1, or sha256.")
                    return
                if hashed == target_hash:
                    print(f"[+] CRACKED: {word}")
                    return
        print("[-] Password not found in wordlist.")
    except FileNotFoundError:
        print(f"[!] Wordlist file '{wordlist_path}' not found.")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 cracker.py <hash> <algorithm> <wordlist>")
        sys.exit(1)
    crack(sys.argv[1], sys.argv[2], sys.argv[3])
