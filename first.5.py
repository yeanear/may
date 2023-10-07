student_dict = {}  # 创建一个空字典
# 添加键值对到字典中，每个人对应的学号
student_dict["1"] = "张三"
student_dict["2"] = "李四"
student_dict["3"] = "王五"
student_dict["4"] = "赵六"
# 删除学号尾号为偶数的元素
keys_to_delete = []
for key in student_dict.keys():
    if int(key[-1]) % 2 == 0:#学号是偶数的储存在列表里
        keys_to_delete.append(key)
for key in keys_to_delete:
    del student_dict[key]
print(student_dict)
