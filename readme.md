# B3_seminar_2025
塩田研 2025年度 B3ゼミナール

ここでは，プログラムを実行するための環境を構築します．
- 各自のPCで実行することを想定しています．
  - WSLを使っている人はすぐ環境構築できると思います．
  - よくわからない人は山口に聞くか，GoogleColabを使ってください．

## コードをGitHubから取得する
リポジトリからコードを取得します．
![コード取得方法](<clone_instruction.png>)
### Gitが使える場合
1. Codeボタンをクリック
2. HTTPSを選択
3. アイコンをクリックしてURLをコピー
4. 自分のマシンにClone
  ```shell
  git clone https://github.com/***.git
  ```
### Gitがよくわからない場合
1. Codeボタンをクリック
2. `Download ZIP`を選択してZIPでダウンロード
3. ZIPを展開

以降はClone/展開したディレクトリをVSCodeで開いて作業してください．

## uvのインストール
パッケージ管理には[uv](https://docs.astral.sh/uv/)を使用します．
[公式インストールガイド](https://docs.astral.sh/uv/getting-started/installation/)に従ってインストールコマンドを実行してください．

## 実行環境の準備
以下のコマンドを実行してください．
> `.venv`, `pyproject.toml`, `uv.lock`がある場合は，これらを削除してからコマンドを実行してください．
1. 環境の初期化
    ```shell
    uv init --name b3-seminar-2025 --python 3.11 --bare
    ```
2. 必要なパッケージを追加
    ```shell
    uv add librosa scipy matplotlib ipykernel speechbrain "torchaudio<2.9.0" "huggingface-hub<0.17.0"
    ```

## プログラムの動かし方
- はじめに: 環境のアクティベート
    ```shell
    source .venv/bin/activate
    ```
  - VSCodeのターミナルを開き直しても可
- `.ipynb`の実行
  - 画面右上の`カーネルの選択`から，`Python環境`→`★ b3-seminar-2025`を選択
- `.py`の実行
  - `uv run python **.py`で実行してください．
