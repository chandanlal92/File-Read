# File Request Networking Application

This is a simple networking application where a client requests the contents of a file from a server. The server uses semaphores to control access to the file, ensuring thread-safe operations.

## Features

- **Server**: Handles multiple client connections using threading.
- **Client**: Allows continuous file requests in a single session.
- **Semaphore**: Ensures only one thread can access the file at a time, preventing race conditions and ensuring data consistency.

## Prerequisites

- Python 3.x

# Usage

# Running the Server

 ```bash
    python file_server.py
```

# Run the client:

```bash
    python client.py
```
# Example Server
```bash
    [*] Listening on 0.0.0.0:9999
    [*] Accepted connection from ('127.0.0.1', 63415)   
```
# Example Client
```bash
    Enter the filename to request (or 'exit' to quit): test.txt
    Received file contents:
    Hello
    Testing file read

    Enter the filename to request (or 'exit' to quit):
```

# Author

Chandanlal