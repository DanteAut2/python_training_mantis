import string
import random

class GeneratorHelper:

    def __init__(self, app):
        self.app = app

    def random_name_of_project(self, start, maxlen):
        symbols = string.ascii_letters
        return start + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])