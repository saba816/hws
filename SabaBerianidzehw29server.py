import socket

# შევქმნათ socket-ის ობიექტი
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# დავაკავშიროთ socket-ი ადრესს და პორტს
server_address = ('localhost', 12345)
server_socket.bind(server_address)

# მოვუსმინოთ მომავალ დაკავშირებებს (max 1 დაკავშირება ამ მაგალითში)
server_socket.listen(1)
print(f"Server is listening on {server_address}")

# მივიღოთ დაკავშირება
client_socket, client_address = server_socket.accept()
print(f"Accepted connection from {client_address}")

# მივიღოთ data კლიენტისგან
data = client_socket.recv(1024)
print(f"Received data: {data.decode()}")

# პასუხი გავცეთ კლიენტს
response = "Hello, client! I received your message."
client_socket.send(response.encode())

# დავხუროთ socket
client_socket.close()
server_socket.close()
