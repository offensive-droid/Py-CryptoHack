import socket

def handle_client(client_socket):
    # Receive data from the client
    data = client_socket.recv(1024).decode('utf-8').strip()

    # Check if the received data is the correct flag
    correct_flag = "crypto{150902150d113900021b3d2037352a363c212b062004}"
    if data == correct_flag:
        response = "Correct flag! You win!"
    else:
        response = "Incorrect flag. Try again."

    # Send the response back to the client
    client_socket.send(response.encode('utf-8'))

    # Close the connection
    client_socket.close()

def main():
    # Set up the server
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 5000))  # Use the desired port
    server.listen(5)

    print("[+] Listening for connections...")

    while True:
        # Accept a connection from a client
        client, addr = server.accept()
        print(f"[+] Connection from {addr[0]}:{addr[1]}")

        # Handle the client in a separate thread or process for concurrent connections
        handle_client(client)

if __name__ == "__main__":
    main()
