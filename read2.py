# 读取并处理台词
with open("word.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()  # 按行读取，返回一个列表

# 按角色分类台词
role_lines = {}
for line in lines:
    line = line.strip()  # 去掉行首尾空白字符
    if not line:
        continue  # 跳过空行
    # 按冒号分割角色和台词
    if "：" in line:
        role, content = line.split("：", 1)
        if role not in role_lines:
            role_lines[role] = []
        role_lines[role].append(content)

# 打印每个角色的台词
for role, lines in role_lines.items():
    print(f"【{role}】共有 {len(lines)} 句台词：")
    for line in lines:
        print(f"  - {line}")