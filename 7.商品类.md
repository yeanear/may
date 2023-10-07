class Commodity:#定义商品
    def __init__(self,id,name,price,total_quantity,remain_quantity):#参数选择
        self.__id = id
        self.__name = name
        self.__price = price
        self.__total_quantity = total_quantity
        self.__remain_quantity = remain_quantity
    def display(self):
        print("商品序号：", self.__id)
        print("商品名：", self.__name)
        print("单价：", self.__price)
        print("总数量：", self.__total_quantity)
        print("剩余数量：", self.__remain_quantity)
    def income(self):
        income=(self.__total_quantity-self.__remain_quantity)*self.__price
        return income
    def set_data(self,id,name,price,total_quantity,remain_quantity):
        self.__id = id
        self.__name = name
        self.__price = price
        self.__total_quantity = total_quantity
        self.__remain_quantity = remain_quantity
c=Commodity(2,"GGBond",5,100,50)
c.display()
print(c.income())
c.set_data(2,"GGBond",5,50,10)
c.display()
print("总收入为：",c.income())
