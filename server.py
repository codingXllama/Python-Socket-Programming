import socket

# SOCK_STREAM is a TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

# listening for a connection, when anyone connects
# the address var => stores the ip address of where the users are joining from
# the clientsocket var => stores the clients socket object
while True:
    clientsocket, address = s.accept()
    print(f"connection from {address} has been established!")
    # sending information to the client socket
    clientsocket.send(bytes("Welcome to the server!", "utf-8"))
    clientsocket.close()
