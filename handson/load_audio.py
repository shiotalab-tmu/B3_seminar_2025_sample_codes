# 音声・音楽関連のライブラリです
# https://librosa.org/
# https://librosa.org/doc/latest/index.html
import librosa

def load_audio(filepath: Path, verbose: bool= False):
    
    data, sr = librosa.stft(
        audio,
        n_fft=2048,
        hop_length=None,
        win_length=None,
    )

if __name__ == "__main__":
    data = load_audio("./audiofile/J-SPaW_sample.wav")
    