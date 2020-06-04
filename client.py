import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# making this socket conect
s.connect((socket.gethostname(), 1234))


# 1024 is the buffer size of the data we want to recieve in bytes.

full_msg = ""
while True:
    msg = s.recv(8)
    if len(msg) <= 0:
        break
    full_msg += msg.decode("utf-8")


print(full_msg)
