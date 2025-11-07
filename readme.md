# はじめに（環境構築）
プログラムを実行するための環境を構築します．
- 各自のPCで実行することを想定しています．
  - WSLを使っている人はすぐ環境構築できると思います．
  - よくわからない人は山口に聞くか，GoogleColabを使ってください．

## コードをGitHubから取得する
TODO

## uvのインストール
パッケージ管理には[uv](https://docs.astral.sh/uv/)を使用します．
[公式インストールガイド](https://docs.astral.sh/uv/getting-started/installation/)に従ってインストールコマンドを実行してください．

## 実行環境の準備
以下のコマンドを実行してください．

1. 環境の初期化
```shell
uv init . --python 3.11 --bare
```
2. pythonのバージョンを指定
```shell
uv python pin 3.11
```
3. 必要なパッケージを追加
```shell
uv add librosa scipy matplotlib ipykernel
```

## プログラムの動かし方
`.ipynb`に参考コードがまとめてあります．VSCodeか何かでファイルを開き，セルの実行時に`b3-seminar`みたいな環境名を選択して実行してください．
