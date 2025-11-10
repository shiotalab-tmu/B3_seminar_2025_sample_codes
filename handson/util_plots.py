import scipy
import matplotlib.pyplot as plt
import numpy as np
import librosa
from pathlib import Path


def plot_filter(b, a, N, btype, sr, cutoff_freq):
    nyquist = sr / 2

    # 周波数応答を得る（点数を増やして滑らかに）
    w, h = scipy.signal.freqz(b, a, fs=sr)

    plt.figure(figsize=(10, 6))
    plt.semilogx(w, 20 * np.log10(abs(h)))
    plt.title(f"{btype} filter frequency response (cutoff: {cutoff_freq}Hz, N={N})")
    plt.xlabel("Frequency [Hz]")
    plt.ylabel("Amplitude [dB]")
    plt.xlim(10, nyquist)
    plt.ylim(-80, 5)
    plt.grid(which="both", axis="both", alpha=0.5)
    # カットオフ周波数の垂直線
    plt.axvline(
        cutoff_freq,
        color="green",
        linestyle="--",
        linewidth=1.5,
        label=f"Cutoff frequency ({cutoff_freq} Hz)",
    )
    # -3dBの水平線
    plt.axhline(-3, color="red", linestyle="--", linewidth=1.5, label="-3 dB point")
    plt.legend(loc="lower left")

    # 余白調整
    plt.tight_layout()
    plt.show()


def plot_spectrogram_compare(
    data_raw,
    data_filtered,
    sr,
    hop_length,
    win_length,
    win,
    n_fft,
    y_axis,
    filter_cutoff,
    filter_N,
    filter_type,
):
    """2つのplotをまとめる"""
    D_orig = librosa.stft(
        data_raw,
        n_fft=n_fft,
        hop_length=hop_length,
        win_length=win_length,
        window=win,
    )
    D_filt = librosa.stft(
        data_filtered,
        n_fft=n_fft,
        hop_length=hop_length,
        win_length=win_length,
        window=win,
    )

    # 共通の基準値を使用してdB変換
    ref_value = np.max(np.abs(D_orig))  # 元の音声の最大値を基準値とする
    D_mag_orig = librosa.amplitude_to_db(np.abs(D_orig), ref=ref_value)
    D_mag_filt = librosa.amplitude_to_db(np.abs(D_filt), ref=ref_value)

    v_min = min(np.min(D_mag_orig), np.min(D_mag_filt))
    v_max = max(np.max(D_mag_orig), np.max(D_mag_filt))

    # plot
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # original (左側のプロット)
    librosa.display.specshow(
        D_mag_orig,
        sr=sr,
        hop_length=hop_length,
        win_length=win_length,
        n_fft=n_fft,
        y_axis=y_axis,
        x_axis="time",
        vmin=v_min,
        vmax=v_max,
        ax=axes[0],  # 左側のaxesに描画
    )
    axes[0].set_title("Original (w/o filter)")
    axes[0].set_xlabel("Time [s]")
    axes[0].set_ylabel("Frequency [Hz]")

    # filtered (右側のプロット)
    librosa.display.specshow(
        D_mag_filt,
        sr=sr,
        hop_length=hop_length,
        win_length=win_length,
        n_fft=n_fft,
        y_axis=y_axis,
        x_axis="time",
        vmin=v_min,
        vmax=v_max,
        ax=axes[1],  # 右側のaxesに描画
    )
    axes[1].set_title(
        f"Filtered ({filter_type}, cutoff={filter_cutoff}Hz, N={filter_N})"
    )
    axes[1].set_xlabel("Time [s]")
    axes[1].set_ylabel("Frequency [Hz]")

    plt.tight_layout()
    plt.show()

    print(f"Color scale range: {v_min:.1f} dB to {v_max:.1f} dB")
