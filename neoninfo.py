import discord
import datetime
import random
import urllib
import urllib.request
from urllib.request import urlopen, Request
import bs4

client = discord.Client()

@client.event
async def on_ready():
    print("login")
    print(client.user.name)
    print(client.user.id)
    print("------------------")
    game = discord.Game("음메와")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message, value=None):
    if message.content.startswith("/날씨"):
        learn = message.content.split(" ")
        location = learn[1]
        enc_location = urllib.parse.quote(location + '날씨')
        hdr = {'User-Agent': 'Mozilla/5.0'}
        url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=' + enc_location
        print(url)
        req = Request(url, headers=hdr)
        html = urllib.request.urlopen(req)
        bsObj = bs4.BeautifulSoup(html, "html.parser")
        todayBase = bsObj.find('div', {'class': 'main_info'})

        todayTemp1 = todayBase.find('span', {'class': 'todaytemp'})
        todayTemp = todayTemp1.text.strip()  # 온도
        print(todayTemp)

        todayValueBase = todayBase.find('ul', {'class': 'info_list'})
        todayValue2 = todayValueBase.find('p', {'class': 'cast_txt'})
        todayValue = todayValue2.text.strip()  # 밝음,어제보다 ?도 높거나 낮음을 나타내줌
        print(todayValue)

        todayFeelingTemp1 = todayValueBase.find('span', {'class': 'sensible'})
        todayFeelingTemp = todayFeelingTemp1.text.strip()  # 체감온도
        print(todayFeelingTemp)

        todayMiseaMongi1 = bsObj.find('div', {'class': 'sub_info'})
        todayMiseaMongi2 = todayMiseaMongi1.find('div', {'class': 'detail_box'})
        todayMiseaMongi3 = todayMiseaMongi2.find('dd')
        todayMiseaMongi = todayMiseaMongi3.text  # 미세먼지
        print(todayMiseaMongi)

        tomorrowBase = bsObj.find('div', {'class': 'table_info weekly _weeklyWeather'})
        tomorrowTemp1 = tomorrowBase.find('li', {'class': 'date_info'})
        tomorrowTemp2 = tomorrowTemp1.find('dl')
        tomorrowTemp3 = tomorrowTemp2.find('dd')
        tomorrowTemp = tomorrowTemp3.text.strip()  # 오늘 오전,오후온도
        print(tomorrowTemp)

        tomorrowAreaBase = bsObj.find('div', {'class': 'tomorrow_area'})
        tomorrowMoring1 = tomorrowAreaBase.find('div', {'class': 'main_info morning_box'})
        tomorrowMoring2 = tomorrowMoring1.find('span', {'class': 'todaytemp'})
        tomorrowMoring = tomorrowMoring2.text.strip()  # 내일 오전 온도
        print(tomorrowMoring)

        tomorrowValue1 = tomorrowMoring1.find('div', {'class': 'info_data'})
        tomorrowValue = tomorrowValue1.text.strip()  # 내일 오전 날씨상태, 미세먼지 상태
        print(tomorrowValue)

        tomorrowAreaBase = bsObj.find('div', {'class': 'tomorrow_area'})
        tomorrowAllFind = tomorrowAreaBase.find_all('div', {'class': 'main_info morning_box'})
        tomorrowAfter1 = tomorrowAllFind[1]
        tomorrowAfter2 = tomorrowAfter1.find('p', {'class': 'info_temperature'})
        tomorrowAfter3 = tomorrowAfter2.find('span', {'class': 'todaytemp'})
        tomorrowAfterTemp = tomorrowAfter3.text.strip()  # 내일 오후 온도
        print(tomorrowAfterTemp)

        tomorrowAfterValue1 = tomorrowAfter1.find('div', {'class': 'info_data'})
        tomorrowAfterValue = tomorrowAfterValue1.text.strip()

        print(tomorrowAfterValue)  # 내일 오후 날씨상태,미세먼지

        embed = discord.Embed(
            title=learn[1] + ' 날씨 정보',
            description=learn[1] + '날씨 정보입니다.',
            colour=discord.Colour.gold()
        )
        embed.add_field(name='현재온도', value=todayTemp + '˚', inline=False)  # 현재온도
        embed.add_field(name='체감온도', value=todayFeelingTemp, inline=False)  # 체감온도
        embed.add_field(name='현재상태', value=todayValue, inline=False)  # 밝음,어제보다 ?도 높거나 낮음을 나타내줌
        embed.add_field(name='현재 미세먼지 상태', value=todayMiseaMongi, inline=False)  # 오늘 미세먼지
        embed.add_field(name='오늘 오전/오후 날씨', value=tomorrowTemp, inline=False)  # 오늘날씨 # color=discord.Color.blue()
        embed.add_field(name='**----------------------------------**', value='**----------------------------------**',
                        inline=False)  # 구분선
        embed.add_field(name='내일 오전온도', value=tomorrowMoring + '˚', inline=False)  # 내일오전날씨
        embed.add_field(name='내일 오전날씨상태, 미세먼지 상태', value=tomorrowValue, inline=False)  # 내일오전 날씨상태
        embed.add_field(name='내일 오후온도', value=tomorrowAfterTemp + '˚', inline=False)  # 내일오후날씨
        embed.add_field(name='내일 오후날씨상태, 미세먼지 상태', value=tomorrowAfterValue, inline=False)  # 내일오후 날씨상태
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
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
