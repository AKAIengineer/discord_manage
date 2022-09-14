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

# 環境
awsEC2のt4g.nanoで十分動作する