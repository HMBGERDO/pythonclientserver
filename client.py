from socket import *
from config import ACTION, TIME, USER, ACCOUNT_NAME, PRECENSE, RESPONSE, DEFAULT_IP, DEFAULT_PORT
from utils import send_message, receive_message
from time import time
import sys

def create_presence_message(username="guest"):
    message = {
        ACTION: PRECENSE,
        TIME: time(),
        USER: {
            ACCOUNT_NAME: username,
        },
    }
    return message

def process_server_message(message):
    if RESPONSE in message:
        print(f"Server responsed status {message[RESPONSE]}")

def main():
    try:
        server_adress = sys.argv[2]
        server_port = sys.argv[3]
    except IndexError:
        server_adress = DEFAULT_IP
        server_port = DEFAULT_PORT
    client_socket = socket(AF_INET,SOCK_STREAM)
    client_socket.connect((server_adress, server_port))
    message = create_presence_message()
    send_message(client_socket, message)
    response = receive_message(client_socket)
    process_server_message(response)

if __name__ == "__main__":
    main()
