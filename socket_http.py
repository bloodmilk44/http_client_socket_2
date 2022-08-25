import socket

from config import LOCALHOST, random_port

my_socket = socket.socket()

address_and_port = (LOCALHOST, random_port())
my_socket.bind(address_and_port)
print("Socket start: ", address_and_port)

my_socket.listen(20)

conn, addr = my_socket.accept()
print("Connection established", conn, addr)

data = conn.recv(1024)
print("Data accept:\n", data.decode("UTF-8"))

conn.send(b"HTTP/1.0 200 OK\n")
conn.send(b'Content-Type: text/html\n')
conn.send(b'\n')
conn.send(b'<html><body><h1>{:((f(}</body></html>')

my_socket.close()