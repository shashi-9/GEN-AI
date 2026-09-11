# # # # # # # # # # # # #
# # # # # # # # # # # # # a = '3'
# # # # # # # # # # # # # b = 5.9
# # # # # # # # # # # # # c = 9j 
# # # # # # # # # # # # # print(type(b))
# # # # # # # # # # # # # print(type(c))  


# # # # # # # # # # # # # d =10
# # # # # # # # # # # # # myvar = 40
# # # # # # # # # # # # # print(myvar)

# # # # # # # # # # # # # a='kandukur'
# # # # # # # # # # # # # b='T'
# # # # # # # # # # # # # print(b)

# # # # # # # # # # # # # a=['mango','banana','apple']
# # # # # # # # # # # # # b=[]
# # # # # # # # # # # # # b.append('vegetables')
# # # # # # # # # # # # # a[0]='orange'
# # # # # # # # # # # # # a.insert(1,'grapes')
# # # # # # # # # # # # # print(b)

# # # # # # # # # # # # # a=['man','women']
# # # # # # # # # # # # # b=['pen','pencil']
# # # # # # # # # # # # # print(a)

# # # # # # # # # # # # # print(2>5)
# # # # # # # # # # # # # print(5!=5)
# # # # # # # # # # # # # print(9==9)

# # # # # # # # # # # # # #arithematic
# # # # # # # # # # # # # a=5
# # # # # # # # # # # # # b=6
# # # # # # # # # # # # # print(a+b)
# # # # # # # # # # # # # print(a-b)
# # # # # # # # # # # # # print(a*b)
# # # # # # # # # # # # # print(a/b)
# # # # # # # # # # # # # print(a%b)
# # # # # # # # # # # # # print(a//b)

# # # # # # # # # # # # # #assignment operator
# # # # # # # # # # # # # a=10
# # # # # # # # # # # # # a/=2
# # # # # # # # # # # # # print(a)

# # # # # # # # # # # # # #comparision
# # # # # # # # # # # # # if 5>=6:
# # # # # # # # # # # # #     print('success')
# # # # # # # # # # # # # else:
# # # # # # # # # # # # #     print('not success')

# # # # # # # # # # # # # #logical
# # # # # # # # # # # # # a=int(input('enter your number'))
# # # # # # # # # # # # # if a>10 and a<100:
# # # # # # # # # # # # #     print('success')
# # # # # # # # # # # # # else:
# # # # # # # # # # # # #     print('not true')
    
# # # # # # # # # # # # # #identity
# # # # # # # # # # # # # x=['man','women']
# # # # # # # # # # # # # y=['man','women']
# # # # # # # # # # # # # z=x
# # # # # # # # # # # # # print(x is y)
# # # # # # # # # # # # # print(z is y)

# # # # # # # # # # # # # a=5
# # # # # # # # # # # # # b=6
# # # # # # # # # # # # # print(a|b)

# # # # # # # # # # # # # for i in range(1,5):
# # # # # # # # # # # # #     for j in range(1, i + 1):
# # # # # # # # # # # # #         print(j, end=" ")
# # # # # # # # # # # # #     print()
    
# # # # # # # # # # # # # for i in range(1, 4):
# # # # # # # # # # # # #     for j in range(1, 6):
# # # # # # # # # # # # #         print(i * j, end=" ")
# # # # # # # # # # # # #     print()
    
# # # # # # # # # # # # # fruits = ["apple", "banana", "cherry"]
# # # # # # # # # # # # # for x in fruits:
# # # # # # # # # # # # #   if x == "banana":
# # # # # # # # # # # # #     continue
# # # # # # # # # # # # #   print(x)
# # # # # # # # # # # # # """
# # # # # # # # # # # # # #listordered
# # # # # # # # # # # # # #set
# # # # # # # # # # # # # #a={'pen', 'pencil', 'mango', 'banana','pen', 'mango', 3, 3, 2.6}
# # # # # # # # # # # # # #print(a)

# # # # # # # # # # # # # #dictionary
# # # # # # # # # # # # # #a={'Name' :'kandukur', 'year' : 2026, 'estab' : 1950, 'famous' : 'vegetables', 'year' : 2022}
# # # # # # # # # # # # # #print(a.keys())
# # # # # # # # # # # # # #print(a.values())
# # # # # # # # # # # # # #for x,y in a.items():
# # # # # # # # # # # # # #print('keys are:', x)
# # # # # # # # # # # # # #print('values are:',y)
# # # # # # # # # # # # #
# # # # # # # # # # # # # a = [1, 2, 3]
# # # # # # # # # # # # # b = a
# # # # # # # # # # # # # b.append(4)
# # # # # # # # # # # # # print(a)
# # # # # # # # # # # # # a = {1, 2, 3, 4}
# # # # # # # # # # # # # b = {3, 4, 5, 6}
# # # # # # # # # # # # # print(a & b)
# # # # # # # # # # # # # print(a | b)

# # # # # # # # # # # # # #elseif
# # # # # # # # # # # # # a=int(input('enter your '))
# # # # # # # # # # # # # if a>=90:
# # # # # # # # # # # # #     print('Grade A')
# # # # # # # # # # # # # elif a>=80 or a<90:
# # # # # # # # # # # # #     print('Grade B')
# # # # # # # # # # # # # elif a>=70 or a<80:
# # # # # # # # # # # # #      print('Grade C')
# # # # # # # # # # # # # elif a>=60 or a<70:
# # # # # # # # # # # # #      print('Grade D')
# # # # # # # # # # # # # else:
# # # # # # # # # # # # #     print('not eligible')
    
# # # # # # # # # # # # a=input(('enter your serial/no'))
# # # # # # # # # # # # match a:
# # # # # # # # # # # #     case 'A':
# # # # # # # # # # # #         print('move towards East')
# # # # # # # # # # # #     case 'B':
# # # # # # # # # # # #         print('move towads south')
# # # # # # # # # # # age = int(input('enter our age'))
# # # # # # # # # # # a=input('enter your token')
# # # # # # # # # # # match a:
# # # # # # # # # # #     case 'red' if age>=18:
# # # # # # # # # # #         print('dosa')
# # # # # # # # # # #     case 'Green' if age>=16:
# # # # # # # # # # #         print('take dosa')
# # # # # # # # # # #     case 'blue' if age>=10:
# # # # # # # # # # #         print('no dosa')
# # # # # # # # # # #     case _:
# # # # # # # # # # #         print("No match")
# # # # # # # # # # def my_add(a,b):
# # # # # # # # # #     if a>20:
# # # # # # # # # #         c= a+b
# # # # # # # # # #     print(c)
# # # # # # # # # # else:
# # # # # # # # # #      print('try again')
# # # # # # # # # #    my_add(10,20)
# # # # # # # # # def kdkr(name = 'book'):
# # # # # # # # #     print('my name is:',name)
# # # # # # # # # kdkr('pencil')

# # # # # # # # import pandas
# # # # # # # # a=pandas.Series([1,2,3,4])
# # # # # # # # print(a)
# # # # # # # try:
# # # # # # #     a= 20
# # # # # # #     b= 100
# # # # # # #     print(b/a)
# # # # # # # except ZeroDivisionError:
# # # # # # #     print('Divisor number is zero so not valid')
# # # # # # # except:
# # # # # # #     print('something is missing')
# # # # # # # finally:
# # # # # # #     print('my task is completed')
# # # # # # x=('mango', 'banana', 'apple')
# # # # # # y=iter(x)
# # # # # # print(next(y))
# # # # # # print(next(y))
# # # # # class kdkr:
# # # # #     def __init__(self, x, y):
# # # # #         self.x=x
# # # # #         self.y=y
# # # # #     def my_add(self, z):
# # # # #         c=self.x + self.y + z
# # # # #         print(c)
# # # # #     def my_mul(self,w ,n):
# # # # #         d=self.x * self.y
# # # # #         print(d)
# # # # # obj = kdkr(50,40)
# # # # # print(obj.my_add(2000))
# # # # # print(obj.my_mul(30,40))
# # # # class father:
# # # #     def __init__(self,a,b):
# # # #         self.a =a
# # # #         self.b =b
# # # #     def land(self):
# # # #         print('have a land property')
# # # #     def building(self):
# # # #         print('i have a building')
# # # # class mother:
# # # #     def __init__(self,a,b):
# # # #         self.a =a
# # # #         self.b =b
# # # #     def Gold(self):
# # # #         print('mother have gold')
# # # #     def bike(self):
# # # #         print('i have a building')
# # # # class child(father, mother):
# # # #     def __init__(self,a,b,c):
# # # #         super().__init__ (a,b)
# # # #         self.c=c
# # # #     def car(self):
# # # #         print('i have a car')
# # # # obj = child(20,40,50)
# # # # obj.land()
# # # # obj.building()
# # # # obj.Gold()
# # # # obj.bike()
# # # # obj.car()
# # # class Grandfather:
# # #     def __init__(self,a):
# # #         self.a=a
# # #     def land(self):
# # #         print(f'i have a land in{self.a}')
# # # class father(Grandfather):
# # #     def __init__(self,a,b):
# # #         super().__init__(a)
# # #         self.b=b
# # #     def building(self):
# # #         print(f'i have a {self.b} house')
# # # class son(father):
# # #     def __init__(self,a,b,c):
# # #         super().__init_(c)
# # #         def bike(self):
# # #         print(f'i have a bike in{b}')
# # # class grandson(son):
# # #     def __init__(self,a,b,c,d):
# # #         super().__init__(d)
# # #         self.d=d
# # #         print(f'i have gold in{self.c}')
# # # obj.land()
# # # obj.building()
# # # obj.Gold()
# # # obj.bike()
# # class father:
# #     def __init__(self,a,b):
# #          self.a =a
# #          self.b =b
# #     def land(self):
# #          print('have a land property')
     
# # class mother:
# #     def __init__(self,c):
# #          self.c =c
# #     def read(self):
# #          print('mother reading book')
     
# # class child(father, mother):
# #     def __init__(self,a,b,c,d):
# #          super().__init__ (a,b,c)
# #          self.d=d
# #     def writing(self):
# #          print('writing letter')
# # obj1=child(1,2,3,4)
# # obj1.land()
# class kdkr:
#     def __init__(self,a,b):
#           self.a=a
#           self.b=b
#     def deposit(Self):
#         print('depositing the amount of{self.a}')
# class village(kdkr):
#     def __init__(self,a,b,c):
#          kdkr.__init__(a,b)
#          self.c=c
#     def withdraw(self):
#          print(f'withdraw amount is{self.c}')
# obj=village(1000,2000,3000)
# obj.withdraw()
class father:
    def __init__(self,a):
        self.a=a
    def eat(self):
        print('eating {self.a}')
class mother:
    def __init__(self, b):
        self.b=b
    def read(self):
        print("reading book")
class child(father,mother):
    def __init__(self,a,b,c):
        father.__init__(self, a)
        mother.__init__(self, b)
        self.c=c
    def write(self):
        print(self.c)
obj=child('eat, read, write')