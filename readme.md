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
> 既に環境構築済みの人は，`pyproject.toml`を最新のものに置き換えてから以下のコマンドを実行してください．

使用するモデルに応じて環境をセットアップ：
- **デフォルト環境**（ECAPA-TDNNなど，CosyVoice以外）：
  ```shell
  uv sync --extra default
  ```
- **CosyVoiceを使用する場合：**
  ```shell
  uv sync --extra cosyvoice
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
