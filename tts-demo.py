import asyncio
import edge_tts

# ---------------------- 1. 配置参数 ----------------------
TEXT = "地球ON LINE欢迎您！"  # 要转语音的文本
VOICE = "zh-CN-XiaoyiNeural"  # 中文女声（可选：zh-CN-YunxiNeural 男声）
OUTPUT_FILE = "test_audio.mp3"  # 输出音频文件名
SRT_FILE = "test_subtitle.srt"  # 同时生成字幕文件（可选）

# ---------------------- 2. 保存文本（Day9 知识点复用） ----------------------
with open("audio_script.txt", "w", encoding="utf-8") as f:
    f.write(TEXT)
print("✅ 已保存文本到 audio_script.txt")

# ---------------------- 3. 生成语音并保存 ----------------------
async def tts_main():
    communicate = edge_tts.Communicate(TEXT, VOICE)
    submaker = edge_tts.SubMaker()
    
    with open(OUTPUT_FILE, "wb") as file:
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                file.write(chunk["data"])
            elif chunk["type"] == "WordBoundary":
                submaker.create_sub((chunk["offset"], chunk["duration"]), chunk["text"])
    
    # 保存字幕文件（可选）
    with open(SRT_FILE, "w", encoding="utf-8") as f:
        f.write(submaker.generate_srt())
    
    print(f"✅ 语音已生成：{OUTPUT_FILE}")
    print(f"✅ 字幕已生成：{SRT_FILE}")

if __name__ == "__main__":
    asyncio.run(tts_main())