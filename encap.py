# # # # class father:
# # # #     def __init__(self,a):
# # # #         self.a=a
# # # #     def eat(self):
# # # #         print('eating {self.a}')
# # # # class mother:
# # # #     def __init__(self, b):
# # # #         self.b=b
# # # #     def read(self):
# # # #         print("reading book")
# # # # class child(father,mother):
# # # #     def __init__(self,a,b,c):
# # # #         father.__init__(self, a)
# # # #         mother.__init__(self, b)
# # # #         self.c=c
# # # #     def write(self):
# # # #         print(self.c)
# # # # obj=child('eat, read, write')
# # # class elementary:
# # #     #def __init__(self, sname,Slocation):
# # #         #self.sname=sname
# # #         #self.Slocation=Slocation
# # #     def study(self):
# # #         print(f'studying 1st class')
# # #         #print('studying at {self.Slocation}')
# # # class university(elementary):
# # #     def study(self):
# # #         print('im studying Btech')
# # #         x=[elementary,university]
# # class vehicle:
# #     def __init__(self,brand,model):
# #         self.brand =brand
# #         self.model =model
# #     def move(self):
# #         print('move')
# # class car(vehicle):
# #    pass
# # class boat(vehicle):
# #     def move(self):
# #         print('sail')
# # class plane(vehicle):
# #     def move(self):
# #         print('fly')
# # car = car('BMW, Mahendra')
# # boat = boat('touring, cargo')
# # plane =plane('boeing, passenger')
# # for x in (car,boat,plane):
# #     print(x.brand)
    
# #     x.move()
# class Student:
#     def __init(self,name, grade):
#         self.name=name
#         self.grade=grade
#     def display_info(self):
#         print(f'Student1: {self.name}, grade:{self.grade}')
#     Student1 = Student("james", 'A')
#     Student1.display_info()
#     Student1.grade = 'A+'
#     print(Student1.grade)
class Student:
    def __init__(self, name, grade):
        self.name = name          # Public attribute
        self.grade = grade        # Public attribute

    def display_info(self):
        # Public method accessing encapsulated data
        print(f"Student: {self.name}, Grade: {self.grade}")

# Creating an instance
student1 = Student("Alice", "A")

# Accessing and modifying public attributes directly
student1.display_info()           # Output: Student: Alice, Grade: A
student1.grade = "A+"             # Modified directly
print(student1.grade)             # Output: A+