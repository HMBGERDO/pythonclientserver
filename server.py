from socket import *
import time
from config import ACTION, TIME, USER, ACCOUNT_NAME, PRECENSE, RESPONSE, DEFAULT_PORT, MAX_CONNECTIONS
from utils import send_message, receive_message
import sys

def create_response_message(code):
    message = {
        RESPONSE: code,
        TIME: time.time(),
    }
    return message

def process_client_message(message):
    if ACTION in message and message[ACTION] == PRECENSE:
        print(f'Client {message[USER][ACCOUNT_NAME]} precensed!')
        return create_response_message(200)

def main():
    try:
        if '-p' in sys.argv:
            listen_port = int(sys.argv[sys.argv.index('-p') + 1])
        else:
            listen_port = DEFAULT_PORT
    except IndexError:
        print('После параметра -\'p\' необходимо указать номер порта.')
        sys.exit(1)

    try:
        if '-a' in sys.argv:
            listen_address = int(sys.argv[sys.argv.index('-a') + 1])
        else:
            listen_address = ''
    except IndexError:
        print('После параметра -\'a\' необходимо указать IP адрес для прослушивания.')
        sys.exit(1)

    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind((listen_address, listen_port))
    server_socket.listen(MAX_CONNECTIONS)
    while True:
        client, client_adress = server_socket.accept()
        client_message = receive_message(client)
        response = process_client_message(client_message)
        send_message(client, response)
        client.close()

if __name__ == "__main__":
    main()
