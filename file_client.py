import socket

def request_file(server_ip, server_port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server_ip, server_port))

    try:
        while True:
            filename = input("Enter the filename to request (or 'exit' to quit): ")
            if filename.lower() == 'exit':
                break

            # Send the filename to the server
            client.send(filename.encode('utf-8'))

            # Receive the file contents from the server
            file_contents = client.recv(4096).decode('utf-8')
            print(f"Received file contents:\n{file_contents}")
    finally:
        client.close()

if __name__ == "__main__":
    server_ip = "127.0.0.1"
    server_port = 9999
    request_file(server_ip, server_port)
