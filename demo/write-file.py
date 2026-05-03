# Day9：写入文件（文本/字幕/语音脚本都能用）
with open("audio.txt", "w", encoding="utf-8") as f:
    f.write("语音内容：你好，这是一段测试文本。")

print("✅ 文本已写入 audio.txt")