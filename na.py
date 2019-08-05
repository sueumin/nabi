import asyncio
import discord
import random

client = discord.Client()

token = 'NjAwODY2MzY1NzI0Njg4Mzg0.XS6K4w.1HZLTK9jLj96zxhWEvoLblb7ybU'

@client.event
async def on_ready():
    print('Logged in as') #화면에 봇의 아이디, 닉네임이 출력됩니다.
    print(client.user.name)
    print(client.user.id)
    print("===========")
    # 디스코드에는 현재 본인이 어떤 게임을 플레이하는지 보여주는 기능이 있습니다.
    # 이 기능을 사용하여 봇의 상태를 간단하게 출력해줄 수 있습니다.
    await client.change_presence(game=discord.Game(name="안녕?"))

@client.event
async def on_message(message):
    if message.content.startswith('혼내줘!'):
        await message.channel.send(random.choice(['때찌!']))

    if message.content.startswith('히스'):
        await message.channel.send(random.choice(['불렀어?', '응?','바쁜데 부르지마..','피곤해...','그만 불러!']))

    if message.content.startswith('!모험일지'):
        await message.channel.send('https://sites.google.com/view/adventurelog/%ED%99%88')

    if message.content.startswith('!룰북'):
        await message.channel.send('https://sites.google.com/site/dungeonworldkr/')

    if message.content.startswith('!시트'):
        await message.channel.send('https://docs.google.com/spreadsheets/d/1n6kLaGY7US3Bqxbxjs84iBtI9jp-3h4MZANERugg2IY/edit#gid=1372636276')

    if message.content.startswith('안녕'):
        await message.channel.send(random.choice(['안녕', '반가워', '흥...', '바보야','그래.. 안녕']))

    if message.content.startswith('!출석'):
        to_tomorrow = datetime.datetime.today()
        local_date2 = to_tomorrow.strftime("%Y.%m.%d")  # 위에서 구한 날짜를 년.월.일 형식으로 저장
        await message.channel.send('응 출석 확인했어', local_date2)

    if message.content.startswith('???'):
        await message.channel.send(random.choice(['ㅇㅈ','아니','으으 사람이세요?','특별히 허락할게','그래','싫어','바보','묵비권 사용하겠습니다.',
                                                  '거절할게','안돼' ,'글쎄?']))

    if message.content.startswith('플할까?'):
        await message.channel.send(random.choice(['그냥 자..','가자!!']))

    if message.content.startswith('!랜덤권사용'):
        await message.channel.send(random.choice(['[1] 낡은 활 / 중거리, 15닢, 무게 2',
                                                  '[2] 보통 활 / 중거리, 장거리, 60닢, 무게 2',
                                                  '[3] 사냥용 활 / 중거리, 장거리, 100닢, 무게 1 ',
                                                  '[4] 쇠뇌 / 중거리, 피해 +1, 재장전, 35닢, 무게 3 ',
                                                  '[5] 곤봉, 몽둥이, 혹몽둥이 / 한걸음, 1닢, 무게 2 ',
                                                  '[6] 지팡이  / 한걸음, 양손, 1닢, 무게 1 ',
                                                  '[7]  소검, 도끼, 전투망치, 철퇴 / 한걸음, 8닢, 무게 1 ',
                                                  '[8] 창 / 몇걸음, 투척, 중거리, 5닢, 무게 1 ',
                                                  '[9] 장검, 전투도끼, 도리깨  / 한걸음, 피해 +1, 15닢, 무게 2 ',
                                                  '[10] 할버드 / 몇걸음, 피해 +1, 양손, 9닢, 무게 2 ',
                                                  '[11] 레이피어 / 한걸음, 정밀, 25닢, 무게 1 ',
                                                  '[12] 결투용 레이피어 / 한걸음, 관통 1, 정밀, 50닢, 무게 2 ',
                                                  '[13] 가죽 갑옷, 사슬 갑옷  /  장갑 1, 착용, 10닢, 무게 1. ',
                                                  '[14] 미늘 갑옷 / 장갑 2, 착용, 불편, 50닢, 무게 3. ',
                                                  '[15] 판금 갑옷/장갑 3, 착용, 불편, 120닢, 무게 4. ',
                                                  '[16]  방패 /장갑 +1, 15닢, 무게 2. ']))

    elif message.content.startswith('!기록'):
        channel = 599613138828132362
        msg = message.content[4:]
        await client.get_channel(channel).send(msg)

    if message.content.startswith("!기억"):
            file = openpyxl.load_workbook('기억.cell')
            sheet = file.active
            learn = message.content.split(" ")
            for i in range(1, 201):
                if sheet["A" + str(i)].value == "-":
                    sheet["A" + str(i)].value = learn[1]
                    sheet["B" + str(i)].value = learn[2]
                    await client.send_message(message.channel, "응 외워둘게")
                    await client.send_message(message.channel, "★ 현재 사용중인 데이터 저장용량 : 200/" + str(i) + " ★")
                    break
            file.save("기억.cell")

    if message.content.startswith("!말해"):
            file = openpyxl.load_workbook("기억.cell")
            sheet = file.active
            memory = message.content.split(" ")
            for i in range(1, 201):
                if sheet["A" + str(i)].value == memory[1]:
                    await client.send_message(message.channel, sheet["B" + str(i)].value)
                    break

    if message.content.startswith("!기억 초기화") or message.content.startswith("!기억초기화"):
            file = openpyxl.load_workbook("기억.cell")
            sheet = file.active
            for i in range(1, 251):
                sheet["A" + str(i)].value = "-"
            await client.send_message(message.channel, "기억초기화 완료")
            file.save("기억.cell")

    if message.content.startswith("!데이터목록") or message.content.startswith("!데이터 목록"):
            file = openpyxl.load_workbook("기억.cell")
            sheet = file.active
            for i in range(1, 201):
                if sheet["A" + str(i)].value == "-" and i == 1:
                    await client.send_message(message.channel, "데이터 없음")
                if sheet["A" + str(i)].value == "-":
                    break
                await client.send_message(message.channel,
                                          "A : " + sheet["A" + str(i)].value + " B : " + sheet["B" + str(i)].value)

        #넣고 싶은 기능
        #1. 기록! 일반에서 기록을 외치면 기록에서 기록되는 시스템
        #2. 코인 mvp를 달성하면 코인을 줄 수 있고 받은 코인을 사용해 장비 뽑기를 할 수 있는 시스템
        #3. 플레이 중 / 지엠 중 플레이를 할 때 플레이 중을 달 수 있는 시스템

client.run(token)
