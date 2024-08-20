import socket
import threading

# Function to receive messages from the server
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                print("Disconnected from server.")
                break
            print(f"Server: {message}")
        except:
            print("Connection error.")
            break

# Main function to start the client
def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 5555))

    # Start a thread to receive messages from the server
    threading.Thread(target=receive_messages, args=(client_socket,)).start()

    while True:
        message = input("Client: ")
        client_socket.send(message.encode('utf-8'))

if __name__ == "__main__":
    start_client()


