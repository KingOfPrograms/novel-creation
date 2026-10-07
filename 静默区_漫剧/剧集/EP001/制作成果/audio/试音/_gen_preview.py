# -*- coding: utf-8 -*-
"""EP001 TTS 配音选型试音：台词全部逐字取自 剧本.md，不改词。"""
import asyncio, os
import edge_tts

OUT = r"D:\小说创作\静默区_漫剧\剧集\EP001\制作成果\audio\试音"
os.makedirs(OUT, exist_ok=True)

CLIPS = [
    # (文件名, 音色, 语速, 音调Hz, 台词原文)
    ("01-陈默VO-A-云希（年轻自然·压嗓）.mp3",
     "zh-CN-YunxiNeural", "-8%", "-15Hz",
     "八年前我十六岁，发现这毛病的第一天，就买了副耳机，音量开到最大。这事我没跟任何人讲过——你是第一个。"),
    ("02-陈默VO-B-云健（浑厚低沉·磁性）.mp3",
     "zh-CN-YunjianNeural", "-8%", "-5Hz",
     "八年前我十六岁，发现这毛病的第一天，就买了副耳机，音量开到最大。这事我没跟任何人讲过——你是第一个。"),
    ("03-陈默VO-C-云扬（播音腔·对照组）.mp3",
     "zh-CN-YunyangNeural", "-4%", "-5Hz",
     "八年前我十六岁，发现这毛病的第一天，就买了副耳机，音量开到最大。这事我没跟任何人讲过——你是第一个。"),
    ("04-陈默对白-云希（现场说话）.mp3",
     "zh-CN-YunxiNeural", "-6%", "-10Hz",
     "周叔，我耳机里放的是英语。"),
    ("05-王姨-A-晓晓（暖宽·市井老板娘）.mp3",
     "zh-CN-XiaoxiaoNeural", "+5%", "+5Hz",
     "两百？！你一天挣几个两百！还有那老太太，六楼你爬的？米你扛的？顺路，你顺的是阎王路。面里给他多卧个蛋。"),
    ("06-王姨-B-晓伊（跳脱泼辣·偏年轻）.mp3",
     "zh-CN-XiaoyiNeural", "+8%", "+5Hz",
     "两百？！你一天挣几个两百！还有那老太太，六楼你爬的？米你扛的？顺路，你顺的是阎王路。面里给他多卧个蛋。"),
    ("07-老周-A-云健（老成浑厚）.mp3",
     "zh-CN-YunjianNeural", "-15%", "-10Hz",
     "喊他没用，他耳朵里塞着耳机呢。这小子，跟他妈一个闷法。"),
    ("08-老周-B-云希慢速（散漫松弛）.mp3",
     "zh-CN-YunxiNeural", "-18%", "-5Hz",
     "喊他没用，他耳朵里塞着耳机呢。这小子，跟他妈一个闷法。"),
    ("09-老太太-晓晓（慢速轻声）.mp3",
     "zh-CN-XiaoxiaoNeural", "-25%", "-8Hz",
     "小伙子，跟你说句话，别嫌我烦。我家老头子，撑不了几天了。你说，是我先瞒着他好，还是他先瞒着我好？"),
    ("10-母亲VO-晓伊（轻·回忆）.mp3",
     "zh-CN-XiaoyiNeural", "-18%", "-3Hz",
     "这座城市要塌下来之前，会先安静下来。"),
    ("11-三轮车主-云健（一嗓子）.mp3",
     "zh-CN-YunjianNeural", "+10%", "+5Hz",
     "看路啊小伙子！"),
    ("12-加班姑娘-晓伊（客气+心声）.mp3",
     "zh-CN-XiaoyiNeural", "-3%", "+0Hz",
     "麻烦你了，辛苦。这个点还有口热的，比人强。"),
]

async def main():
    for name, voice, rate, pitch, text in CLIPS:
        path = os.path.join(OUT, name)
        tts = edge_tts.Communicate(text, voice, rate=rate, pitch=pitch)
        await tts.save(path)
        print("OK", name)

asyncio.run(main())
print("done")
