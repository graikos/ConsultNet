from enum import Enum

class MediaTypes(Enum):
    Image = 1
    Video = 2
    Audio = 3
    HTML = 4

class Media:
    def __init__(self, type):
        self.type = self.get_media_type(type)

    def get_media_type(self, type):
        for media_type in MediaTypes:
            if media_type.value == type:
                return media_type.name


