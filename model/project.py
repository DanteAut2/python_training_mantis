from sys import maxsize

class Project:

    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name


    def __repr__(self):
        return "%s:%s" % (self.id, self.name)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name

    def sorted_name(self):
        if self.name:
            return self.name