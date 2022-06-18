import socket
import time
from config import ACTION, TIME, USER, ACCOUNT_NAME, PRECENSE, RESPONSE, DEFAULT_PORT, MAX_CONNECTIONS
from utils import send_message, receive_message, log
import sys
import logging
import settings
import time


logger = logging.getLogger('server_logger')
def create_response_message(code):
    message = {
        RESPONSE: code,
        TIME: time.time(),
    }
    return message

@log
def process_client_message(message):
    if ACTION in message and message[ACTION] == PRECENSE:
        logger.info(f'Client {message[USER][ACCOUNT_NAME]} precensed!')
        return create_response_message(200)

def main():
    logger.info("Server started")
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
    logger.info(f"Server port: '{listen_port}' Server listen IP: '{listen_address}'")
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    logger.debug("Socket created")
    socket_binded = False
    attempts = 5
    while not(socket_binded) and attempts > 0:
        try:   
            server_socket.bind((listen_address, listen_port))
            socket_binded = True
        except socket.error as message:
            logger.warning(message)
        attempts = attempts - 1
        time.sleep(1)
    if not(socket_binded):
        logger.critical("Failed to bind socket")
        return
    logger.debug("Socket binded")
    server_socket.listen(MAX_CONNECTIONS)
    logger.debug("Socket started listening")
    while True:
        client, client_adress = server_socket.accept()
        logger.info(f"Client connected with IP {client_adress}")
        client_message = receive_message(client)
        logger.debug(f"Recieved message from client {client_adress}")
        response = process_client_message(client_message)
        logger.debug(f"Processed message from client {client_adress}")
        send_message(client, response)
        logger.info(f"Responced to client {client_adress} , closing connection")
        client.close()

if __name__ == "__main__":
    main()
