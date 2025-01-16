import logging
import sys
from logging import Logger


class MainLogger:
    def get_logger(
        self, name: str, file_name: str | None = None, level: str = "info"
    ) -> Logger:
        logger = logging.getLogger(name)
        logger.setLevel(level=level.upper())
        if file_name:
            handler = logging.FileHandler(file_name)
        else:
            handler = logging.StreamHandler(sys.stdout)
        formater = logging.Formatter("%(asctime)s - [%(levelname)s]: %(message)s")
        handler.setFormatter(formater)
        logger.addHandler(handler)
        return logger


logger = MainLogger().get_logger("MainLogger")
