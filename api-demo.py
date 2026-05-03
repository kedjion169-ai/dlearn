# Day10：最简单的 API 调用模板
import requests

# 发送 GET 请求
res = requests.get("https://www.baidu.com")

# 打印响应状态码（200 表示成功）
print("状态码：", res.status_code)

# 打印响应前 500 个字符（看看返回内容）
if res.status_code == 200:
    print("响应内容预览：")
    print(res.text[:500])
else:
    print("请求失败")