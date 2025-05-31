# class a:
#     x=5
# # print(a)
# m=a()
# print(m.x)
# print(type(m))

# ~ init()
# class school:
#     def __init__(self,name,age): #! inbuilt function (create an obj inside a cls)
#         name=self.name
#         age=self.age
# a=school('swetha',21)
# print(a.name)
# print(a.age)

# ^ String function
# class school:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     # def __str__(self):
#     #     return f'{self.name}({self.age})'
# x=school('surya',27)
# print(type(x.name))
# print(type(x.age))
# print(type(x))
# n=123
# print(type(n))
# s=str(n)
# print(type(s))

# &
# class library:
#     def __init__(self, bookname, copy):
#         self.bookname = bookname
#         self.copy = copy
#     def __str__(a):
#         return f"{a.bookname} {a.copy}"
# x = library("python", 12)
# print(x.bookname)
# print(x.copy)
# x.bookname='oracle'
# print(x.bookname)
# del x.copy
# print(x.copy)
# del x

#? Sample example for execution process
a=3
b=8
class Demo:
    def __init__(d,a,b):
        d.a=a
        d.b=b
        print(f'init inside a:{d.a} b:{d.b} outside a:{a} b:',b)
    print(f'init outside a:{a} b:',b)
print(f'class outside a:{a} b:',b)
x=Demo(4,5)     

