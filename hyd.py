# # from kdkr import my_add
# # my_add
# class kdkr:
#     def __init__(self,a,b):
#         self.a = a
#         self._b = b
#     # def my_data(self):
#     #     return self._b
# obj1=kdkr(20,30)
# x=obj1._b
# # print(obj1.a)
# print(x)
# print(x*2)
# # print(obj1._b)
# # print(obj1.my_data())
def kdkr(func):
    def ong(a, b):
        if a > 100:
            print('start the process')
            x = func(a, b)
            print('process completed')
            return x
        else:
            print('please enter valid number')

    return ong


@kdkr
def my_add(a, b):
    return a + b


print(my_add(120, 30))