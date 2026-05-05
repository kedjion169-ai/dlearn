import os

def read_and_print_lines(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        if not lines:
            print("文件是空的哦！")
            return

        print("===== 台词内容 =====")
        for i, line in enumerate(lines, start=1):
            clean_line = line.strip()
            if clean_line:
                print(f"[{i:02d}] {clean_line}")
        print("====================")

    except FileNotFoundError:
        print(f"❌ 错误：找不到文件 {file_path}")
    except Exception as e:
        print(f"❌ 读取文件出错: {e}")

if __name__ == "__main__":
    # 获取当前脚本所在的文件夹路径
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # 拼接 lines.txt 的完整路径
    txt_file = os.path.join(script_dir, "lines.txt")
    read_and_print_lines(txt_file)