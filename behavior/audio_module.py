from pydub import AudioSegment
import threading
import time
from pydub.playback import play
from tkinter import filedialog

class AudioManager:
    def __init__(self):
        self.audio_track = None
        self.playing_thread = None
        self.paused = threading.Event()  # Мьютекс для синхронизации паузы

    def load_audio(self):
        file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav *.mp3")])
        if file_path:
            try:
                self.audio_track = AudioSegment.from_file(file_path)
                print("Audio loaded successfully.")
            except Exception as e:
                print(f"Error loading audio: {e}")

    def play_audio(self):
        if self.audio_track:
            if self.playing_thread and self.playing_thread.is_alive():
                # Если уже есть активный поток воспроизведения, измените состояние паузы
                if self.paused.is_set():
                    self.paused.clear()  # Снимите паузу, чтобы продолжить воспроизведение
                else:
                    self.paused.set()  # Установите паузу, чтобы приостановить воспроизведение
            else:
                # Если нет активного потока воспроизведения, создайте новый
                self.playing_thread = threading.Thread(target=self._play_audio_thread)
                self.playing_thread.start()

    def _play_audio_thread(self):
        audio = self.audio_track
        while True:
            if self.paused.is_set():
                time.sleep(0.1)  # Приостановка воспроизведения
            else:
                play(audio)  # Воспроизведение аудио
