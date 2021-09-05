import socket

c = True 

#AF_INET refers to IPV4, SOCK_STREAM refers to TCP-type connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Binding our socket to a particular port on our machine
server_ip = ('localhost', 4444)
print("Server listening on port", server_ip)
s.bind(server_ip)

#Socket begins listeining on port 4444 for any incoming connections
s.listen(1)

#If connection is detected, accept, and print the origin of the connection
while c == True:
    print("Waiting for a connection...")
    connection, server_ip = s.accept()

    try: 
        print("Connection from:", server_ip)
    finally: 
        connection.close()
        c = False