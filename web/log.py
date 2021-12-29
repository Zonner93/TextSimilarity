import logging
from datetime import datetime
from functools import wraps


log_format = "%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s"

logging.basicConfig(
    filename=f"logs/{str(datetime.now()).split('.')[0].replace(':', '_')}.log",
    level=logging.NOTSET,
    format=log_format)

log_formatter = logging.Formatter(log_format)
root_logger = logging.getLogger()

console_handler = logging.StreamHandler()
console_handler.setFormatter(log_formatter)
root_logger.addHandler(console_handler)


class Log:

    def __init__(self, tag):
        self.tag = tag

    def info(self, msg):
        logging.info(f"{self.tag}: {msg}")

    def debug(self, msg):
        logging.debug(f"{self.tag}: {msg}")

    def error(self, msg):
        logging.error(f"{self.tag}: {msg}")

    def log_info_decorator(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            kwargs_list = [f"{key}={value}" for key, value in kwargs.items()]
            args_list = [arg for arg in args]

            logging.info(f"{self.tag}: {func.__name__}() {args_list} {','.join(kwargs_list)}")
            return func(*args, **kwargs)

        return wrapper
