import logging
from random import randint
from typing import Literal
from .common import Level
try:
    from rich.logging import RichHandler
    from rich.console import Console
except ImportError:
    raise ImportError(
        "Rich is required for enviroments\nInstall it with 'pip install rich'") from None


class Enviroment(object):

    """
    Simple colorfull logging enviroment usable for debugging and 
    simple console applications
    """

    def __init__(self, name: str, color: int = randint(0, 256), logger_level: Literal[Level.NOTSET, Level.DEBUG, Level.INFO, Level.WARNING, Level.ERROR, Level.CRITICAL] = Level.NOTSET, record: bool = False):
        self.name = name
        self.logger_level = logger_level
        self.logger_handler = RichHandler(log_time_format="[%X]", markup=True)
        self.logger = logging.getLogger(self.name)
        self.logger.addHandler(self.logger_handler)
        self.console = Console(record=record)
        self.color = color
        self.logger_handler.setFormatter(logging.Formatter(
            f"[color({self.color})]{self.name}[/color({self.color})]\t%(message)s"))
        self.set_logger_level(logger_level)
        self.logger.debug("'%s' Enviroment created", self.name)

    def __del__(self):
        """
        Sends a debug message if the enviroment is deleted
        """
        try:
            self.logger.debug("'%s' Enviroment destroyed", self.name)
        except ImportError:
            pass

    #  Getters

    def get_name(self) -> str:
        """       
        Get the name of the enviroment       
        """
        return self.name

    def get_color(self) -> int:
        """       
        Get the color of the enviroment name       
        """
        return self.color

    def get_logger_level(self) -> Level:
        """       
        Get the logger level of the enviroment       
        """
        return Level(self.logger_level)

    def get_logger_handler(self) -> RichHandler:
        """       
        Get the logger handler of the enviroment       
        """
        return self.logger_handler

    def get_logger(self) -> logging.Logger:
        """       
        Get the logger of the enviroment       
        """
        return self.logger

    def get_console(self) -> Console:
        """       
        Get the console of the enviroment usefull for simple console applications       
        """
        return self.console

    def get_logger_level_name(self) -> str:
        """       
        Get the logger level name of the enviroment       
        """
        return Level(self.logger_level).name

    #  Setters

    def set_logger_level(self, logger_level: Literal[Level.NOTSET, Level.DEBUG, Level.INFO, Level.WARNING, Level.ERROR, Level.CRITICAL]):
        """
        Set the logger level of the enviroment
        """
        # Check if the level is valid and raise an error if not
        if isinstance(logger_level, Level):
            self.logger_level = logger_level.value
        else:
            self.logger_level = logger_level
        name = Level(self.logger_level).name

        self.logger.setLevel(self.logger_level)
        self.logger.debug("'%s' Enviroment level set to %s",
                          self.name, name)

    def set_color(self, color: int) -> None:
        """       
        Set the color of the enviroment name
        """
        self.color = color
        self.logger_handler.setFormatter(logging.Formatter(
            f"[color({self.color})]{self.name}[/color({self.color})]\t%(message)s"))

    def set_name(self, name: str) -> None:
        """       
        Set the name of the enviroment       
        """
        self.logger.debug("'%s' Enviroment name set to '%s'", self.name, name)
        self.logger.name = self.name
        self.name = name
        self.logger_handler.setFormatter(logging.Formatter(
            f"[color({self.color})]{self.name}[/color({self.color})]\t%(message)s"))
