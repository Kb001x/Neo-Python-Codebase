import socket
from threading import Thread

def handle_client(client_socket):
    while True:
        try:
            msg = client_socket.recv(1024)
            print(msg.decode("utf8"))
        except:
            break

def accept_incoming_connections():
    while True:
        client, client_address = SERVER.accept()
        print("%s:%s has connected." % client_address)
        Thread(target=handle_client, args=(client,)).start()

HOST = ''
PORT = 33000
SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER.bind((HOST, PORT))

SERVER.listen(5)
print("Waiting for connection...")
ACCEPT_THREAD = Thread(target=accept_incoming_connections)
ACCEPT_THREAD.start()
ACCEPT_THREAD.join()
SERVER.close()
