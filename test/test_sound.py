from lib.app.sound import Sound

class TestGetters:
    def setUp(self):
        self.sound = Sound('foo.wav', 'bar/baz')

    def test_id_is_same_as_filename(self):
        assert 'foo.wav' == self.sound.id

    def test_label_is_same_as_filename(self):
        assert 'foo.wav' == self.sound.label

class TestMimeTypes:
    def test_mp3_is_mp3(self):
        assert 'audio/mp3' == Sound('gloopie.mp3').mime_type

    def test_ogg_is_ogg(self):
        assert 'audio/ogg' == Sound('bloopie.ogg').mime_type

    def test_wav_is_wav(self):
        assert 'audio/wav' == Sound('floopie.wav').mime_type

    def test_other_is_none(self):
        assert None == Sound('whatever.other').mime_type

