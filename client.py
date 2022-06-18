from socket import *
from config import ACTION, TIME, USER, ACCOUNT_NAME, PRECENSE, RESPONSE, DEFAULT_IP, DEFAULT_PORT
from utils import send_message, receive_message
from time import time
import logging
import sys
import settings


logger = logging.getLogger('client_logger')
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
        logger.info(f"Server responsed with code {message[RESPONSE]}")

def main():
    logger.info("Client started")
    try:
        server_adress = sys.argv[2]
        server_port = sys.argv[3]
    except IndexError:
        server_adress = DEFAULT_IP
        server_port = DEFAULT_PORT
    logger.debug(f"Server adress: '{server_adress}' Server port:'{server_port}'")
    client_socket = socket(AF_INET,SOCK_STREAM)
    logger.debug("Socket created")
    client_socket.connect((server_adress, server_port))
    logger.info(f"Socket connected with arguments adress: '{server_adress}' port:'{server_port}'")
    message = create_presence_message()
    logger.debug("Precence message created")
    send_message(client_socket, message)
    logger.info("Precence message sended")
    response = receive_message(client_socket)
    logger.info("Server responced")
    process_server_message(response)
    logger.debug("Server message processed")

if __name__ == "__main__":
    main()
