import socket

while True:
    send_data = input("Enter: ")
    client_socket = socket.socket(socket.AF_INET,)