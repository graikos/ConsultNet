from enum import Enum

class MediaTypes(Enum):
    IMAGE = 1
    VIDEO = 2
    AUDIO = 3
    HTML = 4


class Media:
    def __init__(self, type):
        self.type = type



