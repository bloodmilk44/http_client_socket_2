import socket

from config import LOCALHOST, random_port

my_socket = socket.socket()

address_and_port = (LOCALHOST, random_port())
my_socket.bind(address_and_port)
print("Socket start: ", address_and_port)

my_socket.listen(20)

conn, addr = my_socket.accept()
print("Connection established", conn, addr)

data = conn.recv(10000)
data_2 = (data.decode('utf-8')).split("\r\n")
headers = []
for i in data_2:
    headers.append(i)
data_3 = str('<br>'.join(headers)).encode()


conn.send(b"HTTP/1.0 200 OK\r\nContent-Length: 100\r\nConnection: close\r\nContent-Type: text/html\r\n\r\n")
conn.send(b"<body>")
conn.send(data_3)
conn.send(b"</body>")

my_socket.close()