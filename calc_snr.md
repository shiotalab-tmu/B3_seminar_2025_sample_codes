# SNR（信号対雑音比）の計算

## SNRとは

信号対雑音比（Signal-to-Noise Ratio; SNR）は，信号とノイズの比のことです．SN比やS/Nと書くこともあります．

S/Nとあるように，SNRが大きければ雑音の影響は少なく，小さければ雑音の影響が大きいことを意味します．

## SNRの計算方法

具体的には，目的信号と雑音のパワー（$P$）の比によって求まります：

$$
\text{SNR} = \frac{P_{\text{target}}}{P_{\text{noise}}} \tag{1}
$$

音声信号 $x[n]$ のパワー $P$ は振幅の2乗の平均（1サンプルあたりの平均エネルギー）として定義されます：

$$
P = \frac{1}{N} \sum_{n=0}^{N-1} x^2[n] \tag{2}
$$

したがって，目的信号を $\text{target}[n]$，雑音を $\text{noise}[n]$ とすると，SNRは次のように書けます：

$$
\text{SNR} = \frac{P_{\text{target}}}{P_{\text{noise}}} = \frac{\frac{1}{N}\sum_{n=0}^{N-1} \text{target}^2[n]}{\frac{1}{N}\sum_{n=0}^{N-1} \text{noise}^2[n]} \tag{3}
$$

## 実際の音声録音におけるSNR計算

今回のシナリオでは，
- **目的信号 $\text{target}[n]$**: 発話単体
- **雑音 $\text{noise}[n]$**: 背景雑音

となります．

ここで，自分で録音した音声からは，
- **発話区間 (speaking_segment)**: 目的信号＋背景雑音
- **非発話区間 (silence_segment)**: 背景雑音

しか得られません．

すなわち，発話区間には目的信号以外に雑音が含まれており，目的信号だけを得ることはできません．
したがって，上記の式をそのまま適用してSNRを計算することができません．

ただ，純粋な雑音の情報は得られるので，発話区間に含まれる雑音の影響を除くことで目的信号のパワーを計算すればよいです。発話区間の信号を $\text{speaking}[n] = \text{target}[n] + \text{noise}[n]$ とすると，そのパワーは：

$$
P_{\text{speaking}} = P_{\text{target}} + P_{\text{noise}} \tag{4}
$$

と表せます（信号と雑音が独立と仮定）。したがって，目的信号のパワーは：

$$
P_{\text{target}} = P_{\text{speaking}} - P_{\text{noise}} \tag{5}
$$

となり，SNRは次のように計算できます：

$$
\text{SNR} = \frac{P_{\text{target}}}{P_{\text{noise}}} = \frac{P_{\text{speaking}} - P_{\text{noise}}}{P_{\text{noise}}} \tag{6}
$$

## SNRを求める
これらのことから，実際に手元の音声に対してSNRを求めるには：
1. 発話区間と非発話区間を切り出して保存する
2. 式(6)に基づいてSNRを求める

## 実装例
（動くかどうかは確認してないです）
```python
import librosa
import numpy as np

def calculate_snr(noise_path, speaking_path):
    """
    同一音声内の非発話区間と発話区間を切り出したwavからSNRを計算する．

    Parameters
    ----------
    noise_path : str
        非発話区間（雑音）を切り出した音声のパス
    speaking_path : str
        発話区間（目的信号＋雑音）を切り出した音声のパス

    Returns
    -------
    float
        SNR[dB]
    """
    # 音声をload
    noise, _ = librosa.load(noise_path, sr=16000)        # noise[n]: 雑音のみを含む
    speaking, _ = librosa.load(speaking_path, sr=16000)  # speaking[n]: 雑音+目的信号を含む

    # パワーを計算（式(2)）
    P_noise = np.mean(noise ** 2)        # 雑音のパワー
    P_speaking = np.mean(speaking ** 2)  # 発話区間のパワー

    # 目的信号のパワーを計算（式(5)）
    P_target = P_speaking - P_noise

    # SNRを計算（式(6)）
    if P_noise == 0:  # 雑音がないときはSNRが無限になる
        snr = np.inf
    else:
        snr = P_target / P_noise

    # dBに変換
    snr_db = 10 * np.log10(snr)

    return snr_db
```
