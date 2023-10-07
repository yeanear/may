s = input("请输入字符串：")  # 获取用户输入的字符串
if "ol" in s:
    s = s.replace("ol", "fzu")  # 把所有的 "ol" 替换为 "fzu"
s = s[::-1]  # 把字符串倒序输出
print(s)#输出最后的结果