import socket
import sys

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as err:
    print("Failed to create a socket")
    print("Reason: %s" %str(err))
    sys.exit()

print("Socket Created")

target_port = 80
target_host = "www.python.org"

try:
    sock.connect((target_host, int(target_port)))
    print("Socket Connected to %s of port %s" %(target_host, target_port))
    sock.shutdown(2)
except socket.error as err:
    print("Failed to connect to the %s of port %s" %(target_host, target_port))
    print("Reason: %s" %str(err))
    sys.exit()
