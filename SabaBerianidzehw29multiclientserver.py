import socket
import threading

def handle_client(client_socket):
    # მივიღოთ და გავუგზავნოთ data კლიენტს
    data = client_socket.recv(1024)
    print(f"Received data: {data.decode()}")

    response = "Hello, client! I received your message."
    client_socket.send(response.encode())

    # დავხუროთ კლიენტის socket-ი
    client_socket.close()

# შევქმნათ socket ობიექტი
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# დავაკავშიროთ socket-ი ადრესთან და პორტთან
server_address = ('localhost', 12345)
server_socket.bind(server_address)

# მოვუსმინოთ მომავალ კავშირებს
server_socket.listen(5)
print(f"Server is listening on {server_address}")

while True:
    # მივიღოთ კავშირი
    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address}")

    # დავიჭიროთ კლიენტი ახალ thread-ში
    client_handler = threading.Thread(target=handle_client, args=(client_socket,))
    client_handler.start()
