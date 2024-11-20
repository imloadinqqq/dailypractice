import socket
import sys

HOST, PORT = "localhost", 8080
data = " ".join(sys.argv[1:])

# create socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))
    sock.sendall(bytes(data + "\n", "utf-8"))

    recieved = str(sock.recv(1024), "utf-8")

print("Sent:\t{}".format(data))
print("Recieved:\t{}".format(recieved))
