import json
from config import ENCODING, MAX_PACKAGE_LENGTH

def send_message(socket, message):
    '''
    Утилита отправки сообщения
    Принимает словарь, преобразует его в JSON и кодирует, после чего отправляет в сокет
    '''
    json_message = json.dumps(message)
    encoded_message = json_message.encode(ENCODING)
    socket.send(encoded_message)

def receive_message(socket):
    '''
    Утилита получения сообщения
    Принимает байты, декодирует и преобразует из JSON в словарь
    Возвращает полученный словарь
    '''
    message = socket.recv(MAX_PACKAGE_LENGTH)
    decoded_message = message.decode(ENCODING)
    unparsed_message = json.loads(decoded_message)
    return unparsed_message
