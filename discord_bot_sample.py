import discord
import requests

TOKEN = '*************************'
api_url = 'https://notify-api.line.me/api/notify'
 
client = discord.Client(intents=discord.Intents.default())
 
# チャンネル入退室時の通知処理
@client.event
async def on_voice_state_update(member, before, after):

    # チャンネルへの入室ステータスが変更されたとき（ミュートON、OFFに反応しないように分岐）
    if before.channel != after.channel:
        # 通知メッセージを書き込むテキストチャンネル（チャンネルIDを指定）
        # botRoom = client.get_channel(**************)
 
        # 入退室を監視する対象のボイスチャンネル（チャンネルIDを指定）
        announceChannelIds = [****************]
 
        # 退室通知
        # if before.channel is not None and before.channel.id in announceChannelIds:
        # 1→0人を判定
        if before.channel and not after.channel and len(before.channel.members) == 0:
            # await botRoom.send("**" + before.channel.name + "** から、__" + member.display_name + "__  が抜けました！")

            send_contents = '通話が終了しました。'
            TOKEN_dic = {'Authorization': 'Bearer' + ' ' + TOKEN}
            send_dic = {'message': send_contents}
            requests.post(api_url, headers=TOKEN_dic, data=send_dic)
        # 入室通知
        # if after.channel is not None  and after.channel.id in announceChannelIds:
        # 0→1人を判定
        if not before.channel and after.channel and len(after.channel.members) == 1:
            # await botRoom.send("**" + after.channel.name + "** に、__" + member.display_name + "__  が参加しました！")

            send_contents = member.name + 'が通話を開始しました。'
            TOKEN_dic = {'Authorization': 'Bearer' + ' ' + TOKEN}
            send_dic = {'message': send_contents}
            requests.post(api_url, headers=TOKEN_dic, data=send_dic)
 
# Botのトークンを指定（デベロッパーサイトで確認可能）
client.run("*****************************")
