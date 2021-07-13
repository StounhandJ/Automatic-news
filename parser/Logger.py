import logging


class Logger:
    _logger = None

    def __init__(self):
        logger = logging.getLogger()
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            '[%(asctime)s][%(name)s] %(message)s', "%Y.%m.%d %H:%M:%S")
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.DEBUG)
        self._logger = logger

    def log(self, text):
        logging.info(text)

    def error(self, text):
        logging.error(text)


logger = Logger()
