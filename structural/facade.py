from pathlib import Path

class MP3:
    def process(self):
        print('processing MP3')
        Path('filename.mp3').touch()


class WAV:
    def process(self):
        print('processing WAV')
        Path('filename.wav').touch()

class Data:
    def process(self):
        print('processing analysing')
        Path('filename.dbbbs').touch()

class Render:
    def __init__(self):
        self.mp3 = MP3()
        self.wav = WAV()
        self.data = Data()

    def startRendering(self):
        self.mp3.process()
        self.wav.process()
        self.data.process()
