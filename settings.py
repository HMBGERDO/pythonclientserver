import logging.config
import os


current_dir = os.path.dirname(__file__)
client_log_file = os.path.join(current_dir, "log", "client.log")
server_log_file = os.path.join(current_dir, "log", "server.log")


LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'default_formatter': {
            'format': '[%(levelname)s * %(asctime)s * %(module)s] %(message)s'
        },
    },

    'handlers': {
        'file_handler_client': {
            'class': 'logging.FileHandler',
            'formatter': 'default_formatter',
            'filename': client_log_file,
            'encoding': 'utf-8'
        },
        'file_handler_server': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'formatter': 'default_formatter',
            'filename': server_log_file,
            'encoding': 'utf-8',
            'when': 'D',
            'interval': 1,
        },
    },

    'loggers': {
        'server_logger': {
            'handlers': ['file_handler_server'],
            'level': 'DEBUG',
            'propagate': True
        },
        'client_logger': {
            'handlers': ['file_handler_client'],
            'level': 'DEBUG',
            'propagate': True
        },
    }
}

logging.config.dictConfig(LOGGING_CONFIG)