import socket
import threading

# Setting the username
username = input("Choose your username: ")

# Connecting to the server
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(('127.0.0.1', 4444))

def receive():
    while True:
        try: 
            # Receive messages from the server, if the message is "USER" send username
            message = c.recv(1024).decode('ascii')
            if message == "USER":
                c.send(username.encode('ascii'))
            else:
                print(message)
        except:
            # If exception close server
            print("Error, Connection closed.")
            c.close()
            break

def send():
    while True:
        message = '{}: {}'.format(username, input(''))
        c.send(message.encode('ascii'))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

send_thread = threading.Thread(target=send)
send_thread.start()
