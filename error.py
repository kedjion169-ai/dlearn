try:
    num = int(input("请输入一个数字："))
    result = 10 / num
    print(f"10 ÷ {num} = {result}")

except ZeroDivisionError:
    print("❌ 错误：不能除以 0")

except ValueError:
    print("❌ 错误：你输入的不是有效数字！")

except KeyboardInterrupt:
    print("\n⚠️  程序被用户手动中断")

except Exception as e:
    print(f"❌ 未知错误: {e}")

else:
    print("✅ 计算成功！")

finally:
    print("程序运行结束")