# 概要
discordのVCチャンネルに人が入室したとき、その通知をLINEグループに送信するシステム。  
このシステムにより、LINEグループのメンバーでゲームをしたいとき、いちいち「discordにいるよ」などと知らせる必要が無くなり、事前に予定を合わせずともLINE通知を確認してdiscordに参集することが可能となる。

## 仕様
- VCチャンネルに1人目が入室したとき、LINEに「discordに○○が入室しました。」と通知される。誰もいなくなったとき、「通話が終了しました。」と通知される。
- LINEnotifyとdiscord.pyを使用している。（どちらもAPIのようなやつ）
- 当スクリプトのAPIトークン部分を書き換えるだけで使用できる。
- 常時コードを実行状態にしておくため、レンタルサーバーやクラウドサーバーなどを利用する必要がある。

## 環境
awsEC2のt4g.nanoで十分動作する

# 実行手順
1. apt update, apt upgradeの実行
1. このgitをclone
1. pip, libffi-dev, libnacl-dev, python3-devのインストール
    ```
    $ sudo apt install pip libffi-dev libnacl-dev python3-dev 
    ```
1. discord.pyのインストール
    ```
    $ python3 -m pip install -U discord.py
    ```
1. discord_channels_sample.pyをコピーしdiscord_channels.pyとし、discoedトークンを入力
1. discord_channels.pyを実行しdiscordVCチャンネルIDを取得
    ```
    $ python3 discord_channels.py
    ```
1. discord_bot_sample.pyをコピーしdiscord_bot.pyとし、discordトークン, LINEトークン(LINE notify), discordVCチャンネルIDを変更
1. discord_bot.pyを実行(nohupでSSH切断後もプロセスを動かし続ける)
    ```
    $ nohup python3 discord_bot.py &
    ```

# 参考文献
- [Discord APIを利用して入室通知Botをつくってみた](https://techblog.cartaholdings.co.jp/entry/archives/6412)
- [discordpy-japan メンバーがボイスチャンネルorステージチャンネルに参加した時](https://scrapbox.io/discordpy-japan/%E3%83%A1%E3%83%B3%E3%83%90%E3%83%BC%E3%81%8C%E3%83%9C%E3%82%A4%E3%82%B9%E3%83%81%E3%83%A3%E3%83%B3%E3%83%8D%E3%83%ABor%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8%E3%83%81%E3%83%A3%E3%83%B3%E3%83%8D%E3%83%AB%E3%81%AB%E5%8F%82%E5%8A%A0%E3%81%97%E3%81%9F%E6%99%82)
