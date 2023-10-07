x = int(input("请输入x："))
y = int(input("请输入y："))
z = int(input("请输入z："))
#answer 1,逐个比较法
if y>x:
    x,y=y,x
if z>y:
    y,z=z,y
if y>x:
    x, y = y, x
print(x,y,z)
#answer 2，利用取大取小函数
max_num=max(x,y,z)
min_num=min(x,y,z)
mid_num=x+y+z-max(x,y,z)-min_num
print(max_num,mid_num,min_num)
#answer 3，利用列表中的函数
nums=[x,y,z]
nums.sort(reverse=True)#加上reverse=True条件使进行降序排序
print(nums)

