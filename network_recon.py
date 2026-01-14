import socket
import argparse
import requests

def ip():
    def port():
        SERVER_HOST = "192.187.87.120"
        SERVER_PORT = 5003
        SERVER_LIST = (ip, port)

def network_recon(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setdefaulttimeout(5)
    s.connect_ex((ip, port))
    time_sleep(5) # Time in Seconds 
    s.close()
    return s
try:
    def start_network_reconnainsance(ip, port):
        p = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        p.settimeout(5)
        p.connect_ex((ip, port))
    def time_sleep():    
        time_sleep(10) # Time in Seconds
    def p():
        p.close()
        return p
except:
        print("[-] Failed to Start Up the Network Reconnainsance Tool")
else:
        print("[+] Starting Up Network Reconnainsance")
