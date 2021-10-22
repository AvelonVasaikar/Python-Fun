import socket
chunk = 65536
port = 3000
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
hostname = '127.0.0.1'

s.bind((hostname, port))

print(f"Server is Free on {s.getsockname()}")

while True:
	data, client_add = s.recvfrom(chunk)
	message = data.decode('ascii')
	print(f"Avelon : {message} ")
	message_send = input("Reply : ")
	data = message_send.encode('ascii')
	s.sendto(data, client_add)