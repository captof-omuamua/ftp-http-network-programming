import socket

def send_request(method, filename='', data=''):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 5005))#this happens in same computer

    headers = f'Filename: {filename}\r\n'

    if method in ['POST', 'PUT']:
        headers += f'Content-Length: {len(data)}\r\n\r\n'
        request = f'{method} /{filename} HTTP/1.1\r\n{headers}{data}'
    else:
        request = f'{method} /{filename} HTTP/1.1\r\n{headers}\r\n'

    client_socket.send(request.encode())

    response = client_socket.recv(1024).decode()
    print(response)

    client_socket.close()

def main():
    while True:
        print("\nMenu:")
        print("TO PERFORM GET PRESS 1")
        print("TO PERFORM POST PRESS 2")
        print("TO PERFORM PUT PRESS 3")
        print("TO PERFORM DELETE PRESS 4")
        print("TO Exit PRESS 5")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            filename = input("Enter filename to GET: ")
            send_request('GET', filename)
        elif choice == '2':
            filename = input("Enter filename for POST: ")
            data = input("Enter data to be created: ")
            send_request('POST', filename, data)
        elif choice == '3':
            filename = input("Enter filename for PUT: ")
            data = input("Enter updated data: ")
            send_request('PUT', filename, data)
        elif choice == '4':
            filename = input("Enter filename to DELETE: ")
            send_request('DELETE', filename)
        elif choice == '5':
            break
        else:
            print("please enter a valid number between 1-5")

if __name__ == '__main__':
    main()
