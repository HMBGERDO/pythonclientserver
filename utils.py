import inspect
import json, traceback, inspect, logging
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

def log(func):
    # определяем нужный логгер по имени файла
    if inspect.getfile(func).endswith("server.py"):
        logger = logging.getLogger("server_logger")
    elif inspect.getfile(func).endswith("client.py"):
        logger = logging.getLogger("client_logger")
    else:
        # или указываем стандартный, если ничего не подошло
        logger = logging.Logger("default_logger")
        formatter = logging.Formatter(fmt="[%(levelname)s * %(asctime)s * %(module)s] %(message)s")
        handler = logging.FileHandler(filename="log.log", encoding="utf-8")
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    def catcher(*args, **kwargs):
        result = func(*args, **kwargs)
        traceback_result = reversed(traceback.format_stack()[:-1]) # последняя строка всегда будет traceback_result = traceback.format_stack(), нам она не нужна
        result_list = []
        for v in traceback_result:
            result_list.append(v.strip().split()[-1])
        logger.debug("Traceback result - " + " called from ".join(result_list))
        return result
    return catcher