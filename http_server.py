import socket
import os

def create_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server is listening on {host}:{port}")

    while True:
        conn, addr = server_socket.accept()
        request = conn.recv(1024).decode('utf-8')
        method, path, *_ = request.split('\n')[0].split()

        if method == "GET":
            try:
                with open(path[1:], 'r') as file:
                    content = file.read()
                    response = "HTTP/1.1 200 OK\n\n" + content
            except FileNotFoundError:
                response = "HTTP/1.1 404 Not Found\n\nResource not found on the server"
        elif method == "POST":
            data = request.split('\n')[-1]
            with open(path[1:], 'w') as file:
                file.write(data)
            response = "HTTP/1.1 200 OK\n\nResource created on the server"
        elif method == "PUT":
            resource_name = path[1:]
            data = request.split('\n')[-1]
            if os.path.exists(resource_name):
                with open(resource_name, 'w') as file:
                    file.write(data)
                response = "HTTP/1.1 200 OK\n\nResource updated on the server"
            else:
                with open(resource_name, 'w') as file:
                    file.write(data)
                response = "HTTP/1.1 201 Created\n\nResource created on the server"
        elif method == "DELETE":
            resource_name = path[1:]
            if os.path.exists(resource_name):
                os.remove(resource_name)
                response = "HTTP/1.1 200 OK\n\nResource deleted on the server"
            else:
                response = "HTTP/1.1 404 Not Found\n\nResource not found on the server"

        conn.sendall(response.encode('utf-8'))
        conn.close()

if __name__ == '__main__':
    HOST = 'localhost' 
    PORT = 5005
    create_server(HOST, PORT)
