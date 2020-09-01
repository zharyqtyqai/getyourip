#!/usr/bin/env python
import pymyip

print("-"*50)
print(f"{'-'*16}Get My IP Address{'-'*17}")
print("-"*50)

print(f"[+] Country: {pymyip.get_country()}")
print(f"[+] City: {pymyip.get_city()}")
print(f"[+] IP: {pymyip.get_ip()}")
