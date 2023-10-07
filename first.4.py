##当列表字符不以空格分开时
lst = input("请输入列表：")  # 获取用户输入的列表
lst = [x for x in lst if x.isdigit()]  # 删除列表中的字符串元素
lst = [int(x) for x in lst]  # 把剩下的元素转换为整数类型
lst.sort() # 对列表进行升序排序
print(lst)