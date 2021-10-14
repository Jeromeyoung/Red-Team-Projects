import socket
import threading

host = "127.0.0.1"
port = 4444
clients = []
usernames = []

# Establishing the socket and designating it as IPV4 and UDP
# Unlike TCP, UDP does not guarantee packet delivery. If a packet is lost it is lost forever. 
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# binds to the ip address and port
s.bind((host, port))

# Server broadcast function, sends message to all connected clients
def broadcast(message):
    for client in clients:
        client.sendto(message)

#Handling messages from the clients
def handle(client):
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            broadcast(message)
        except:
            break

data, addr = s.recvfrom(1024)
handle(data)