import random
import time
from enviroment import Enviroment

ENV = Enviroment("")


def random_color():
    return random.randint(0, 256)


while True:
    ENV.console.print(
        "[color({color})]COLOR SUPPORT[/color({color})]".format(color=random_color()))
    time.sleep(1)
