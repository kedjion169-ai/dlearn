# 导入Python自带的json模块，专门处理JSON数据
import json

# 定义一个Python字典，对应你截图里的角色语音数据
data = {"voice": "女", "text": "你好"}

# 用json.dumps()把Python字典转换成JSON格式的字符串
# ensure_ascii=False 可以保留中文不转义，方便查看
json_str = json.dumps(data, ensure_ascii=False)

# 打印结果
print("转换后的JSON字符串：")
print(json_str)
print("数据类型：", type(json_str))