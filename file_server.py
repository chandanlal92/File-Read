import socket
import threading
import os

# Semaphore for file access, allowing only one thread at a time
file_semaphore = threading.Semaphore(1)

def handle_client(client_socket):
    try:
        while True:
            # Receive the filename from the client
            requested_file = client_socket.recv(1024).decode('utf-8')
            if not requested_file:
                break

            # Acquire the semaphore
            file_semaphore.acquire()

            try:
                # Read the file contents
                if os.path.isfile(requested_file):
                    with open(requested_file, 'r') as f:
                        file_contents = f.read()
                else:
                    file_contents = "File not found."

                # Send the file contents back to the client
                client_socket.send(file_contents.encode('utf-8'))
            finally:
                # Release the semaphore
                file_semaphore.release()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close the client connection
        client_socket.close()

def start_server(server_ip, server_port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((server_ip, server_port))
    server.listen(5)
    print(f"[*] Listening on {server_ip}:{server_port}")

    while True:
        client_socket, addr = server.accept()
        print(f"[*] Accepted connection from {addr}")

        # Handle the client in a new thread
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    start_server("0.0.0.0", 9999)
