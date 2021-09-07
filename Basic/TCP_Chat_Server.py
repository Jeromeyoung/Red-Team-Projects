import socket
import threading

#Defining our server host and port number
host = "127.0.0.1"
port = 4444

#These next steps are concerned with creating the server
#AF_INET refers to IPV4, SOCK_STREAM refers to TCP-type connection (AKA 3-way handshake)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen()

#Lists for the clients and usernames
clients = []
usernames = []

#Server broadcast function, sends messages to all connected clients
def broadcast(message):
    for client in clients:
        client.send(message)

# Handling messages from the clients

def handle(client):
    while True:
        try:
            # Broadcasting messages received from clients
            message = client.recv(1024)
            broadcast(message)
        except:
            # If an exception is raised during connection, remove and close client connections
            index = clients.index(client)
            clients.remove(client)
            client.close()
            username = usernames[index]
            broadcast('{} left the chatroom.'.format(username).encode('ascii'))
            usernames.remove(username)
            break

def receive():
    while True:
        # Accept connections
        client, address = s.accept()
        print("Connected with {}".format(str(address)))

        # Server requests username and appends it to usernames
        client.send('USER'.encode('ascii'))
        username = client.recv(1024).decode('ascii')
        usernames.append(username)
        clients.append(client)

        # Print and Broadcast Username
        print("Username is {}".format(username))
        broadcast("{} joined!".format(username).encode("ascii"))
        client.send('Connected to the server!'.encode('ascii'))

        # Start handling thread for client
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

receive()