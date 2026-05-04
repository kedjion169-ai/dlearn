# 生成角色语音的函数，接收voice（角色）和text（文本）参数，返回JSON格式的请求数据
import json

def generate_voice_request(voice: str, text: str) -> str:
    """
    生成角色语音合成请求的JSON字符串
    :param voice: 角色音色（如"女"、"男"）
    :param text: 要合成的文本内容
    :return: 标准JSON格式字符串
    """
    # 构建请求数据字典
    request_data = {
        "voice": voice,
        "text": text
    }
    # 转换为JSON字符串，保留中文
    return json.dumps(request_data, ensure_ascii=False)

# 测试函数
if __name__ == "__main__":
    # 测试：生成女性角色说"你好，我是AI助手"的请求数据
    test_json = generate_voice_request(voice="女", text="你好，我是AI助手")
    print("生成的语音请求JSON：")
    print(test_json)