import os

MIME_TYPES = {
    '.mp3' : 'audio/mp3',
    '.ogg' : 'audio/ogg',
    '.wav' : 'audio/wav'
}

class Sound(object):
    def __init__(self, filename, dirname=None):
        self.dirname = dirname
        self.filename = filename

    @property
    def id(self):
        return self.filename

    @property
    def label(self):
        return self.filename

    @property
    def mime_type(self):
        _, ext = os.path.splitext(self.filename)
        return MIME_TYPES.get(ext)




