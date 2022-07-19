import socket
from telnetlib import IP

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

print("El nombre de mi ordenador es: " + hostname)
print("Tu dirrecion IP es: " + ip)