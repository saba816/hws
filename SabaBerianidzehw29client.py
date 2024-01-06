import socket

# შევქმნათ socket ობიექტი
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# დავაკავშიროთ სერვერთან
server_address = ('localhost', 12345)
client_socket.connect(server_address)

# გავაგზავნოთ data სერვერზე
message = "Hello, server! How are you doing?"
client_socket.send(message.encode())

# მივიღოთ პასუხი სერვერისგან
response = client_socket.recv(1024)
print(f"Received response: {response.decode()}")

# დავხუროთ socket
client_socket.close()
