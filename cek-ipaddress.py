from ipaddress import ip_address
import socket

host = input("masukkan nama domain: ")
ip_address = socket.gethostbyname(host)

print(f"ma,a domain: {host}")
print(f"ip address :{ip_address}")