import discord
import datetime
import random
import urllib.request
from bs4 import BeautifulSoup
import os

client = discord.Client()

@client.event
async def on_ready():
    print("login")
    print(client.user.name)
    print(client.user.id)
    print("------------------")
    game = discord.Game("음메 대신")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message, value=None):
    if message.content.startswith("/코로나"):

        url = 'https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%EC%BD%94%EB%A1%9C%EB%82%98'
        html = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(html, 'html.parser')

        people = soup.findAll('strong', {'class': 'num'})
        data_list = []
        for i in people:
            data_list.append(i.get_text().replace('\n', '').replace(' ', ''))
        embed = discord.Embed(color=0xff0000)
        embed.add_field(name="코로나 실시간 현황", value="확진자 : " + data_list[0] + "\n격리해제 : " + data_list[1] + "\n검사 중 : " + data_list[2] + "\n사망자 : " + data_list[3], inline=True)
        embed.set_thumbnail(
            url="http://post.phinf.naver.net/MjAyMDAyMDNfMjIw/MDAxNTgwNjk0MzkwOTY2.pKNl4PbotKUn_vmYoHNTpKdsDx5HuuAvpA1p8NSQDaYg.1AYI3_Uf7Bk7ALP2lHevuR9ZThmuiHGi0fTNuMPPxnsg.PNG/IBuNUMjY84YotKgVXGthVvcdYVi4.jpg")
        await message.channel.send(embed=embed)  
    if message.content.startswith("/음메"):
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
        embed = discord.Embed(color=0xff0000)
        embed.add_field(name="서버", value="NEON", inline=True)
        embed.add_field(name="사용자", value=message.author.name, inline=True)
        embed.add_field(name="직군", value=message.author.top_role, inline=True)
        embed.add_field(name="사용자 정보", value=message.author.display_name, inline=True)
        embed.set_thumbnail(url=message.author.avatar_url)
        embed.add_field(name="제작자", value="음메#7491", inline=True)
        embed.set_image(url="https://o.remove.bg/uploads/a3011d27-6843-495a-85ad-fd723ef974f9/prop_ron_drop_sign_.png")
        await message.channel.send(embed=embed)
    if message.content.startswith("/제작자"):
        await message.channel.send("제작자 : 음메#7491")
    if message.content.startswith("/안녕"):
        await message.channel.send("안녕 나는 음메야 !")
    if message.content.startswith("/가위바위보 가위"):
        rsp = "123"
        rsp1 = random.choice(rsp)
        if rsp1 == "1":
            emb = discord.Embed(title='가위바위보', color=0xfff000)
            emb.add_field(name='승부결과!!', value='음메 :v: 당신 :v: 무승부!')
            await message.channel.send(content=None, embed=emb)
        if rsp1 == "2":
            emb = discord.Embed(title='가위바위보', color=0xff0000)
            emb.add_field(name='승부결과!!', value='음메 :fist: 당신 :v: 봇 승리!')
            await message.channel.send(content=None, embed=emb)
        if rsp1 == "3":
            emb = discord.Embed(title='가위바위보', color=0x0dff00)
            emb.add_field(name='승부결과!!', value='음메 :raised_hand: 당신 :v: 당신 승리!')
            await message.channel.send(content=None, embed=emb)

    if message.content.startswith("/가위바위보 바위"):
        rsp = "123"
        rsp1 = random.choice(rsp)
        if rsp1 == "1":
            emb = discord.Embed(title='가위바위보', color=0x0dff00)
            emb.add_field(name='승부결과!!', value='음메 :v: 당신 :fist: 당신 승리!')
            await message.channel.send(content=None, embed=emb)
        if rsp1 == "2":
            emb = discord.Embed(title='가위바위보', color=0xfff000)
            emb.add_field(name='승부결과!!', value='음메 :fist: 당신 :fist: 무승부!')
            await message.channel.send(content=None, embed=emb)
        if rsp1 == "3":
            emb = discord.Embed(title='가위바위보', color=0xff0000)
            emb.add_field(name='승부결과!!', value='음메 :raised_hand: 당신 :fist: 봇 승리!')
            await message.channel.send(content=None, embed=emb)
    if message.content.startswith("/가위바위보 보"):
        rsp = "123"
        rsp1 = random.choice(rsp)
        if rsp1 == "1":
            emb = discord.Embed(title='가위바위보', color=0xff0000)
            emb.add_field(name='승부결과!!', value='음메 :v: 당신 :raised_hand: 봇 승리!')
            await message.channel.send(content=None, embed=emb)
        if rsp1 == "2":
            emb = discord.Embed(title='가위바위보', color=0x0dff00)
            emb.add_field(name='승부결과!!', value='음메 :fist: 당신 :raised_hand: 당신 승리!')
            await message.channel.send(content=None, embed=emb)
        if rsp1 == "3":
            emb = discord.Embed(title='가위바위보', color=0xfff000)
            emb.add_field(name='승부결과!!', value='음메 :raised_hand: 당신 :raised_hand: 무승부!')
            await message.channel.send(content=None, embed=emb)
    if message.content.startswith('/명령어'):
        embed = discord.Embed(title="명령어", description="""\n\n
                /음메\n
                /가위바위보 가위\n
                /가위바위보 바위\n
                /가위바위보 보\n
                /출근\n
                /퇴근\n
                /clear\n
                /코로나\n""", color=0XFF0000)

        await message.channel.send(embed=embed)
   
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
