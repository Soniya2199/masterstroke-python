
#~ goa
# class Goa:
#     name='' #! variable
#     drinks=''
#     def Party(self): #! function/ self refers to instance of that cls
#         print('lets party in....')
#     def Beach(self):
#         print('Beach enjoying...')
# Ram=Goa() #! Ram is an object and Goa() main method
# Swe=Goa()
# # print(Ram) #!shows obj specified identifier where it is present
# Ram.name='Ram'
# Ram.drinks='yes'
# print(Ram.name)
# print(Ram.drinks)
# Ram.Party()
# Ram.Beach()
# Swe.name='Swetha'
# Swe.drinks='no'
# print('*'*50)
# print(Swe.name)
# print(Swe.drinks)
# Swe.Beach()

#^ Laptop 
# class Laptop:
#     price=''
#     processor=''
#     ram=''
# hp=Laptop()
# hp.price='52000'
# hp.processor='i5'
# hp.ram='8GB'
# print(hp.price)
# print(hp.processor)
# print(hp.ram)

#& user input laptop
# class Laptop:
#     def __init__(self):
#         self.price=float(input('Enter the price:'))
#         self.processor=input('Enter the processor:')
#         self.ram=input('Enter the ram:')
#     def display(self):
#         print('#'*50)
#         print('price:',self.price)
#         print('processor:',self.processor)
#         print('ram:',self.ram)
# hp=Laptop()
# # hp.price=float(input('Enter the price:'))
# # hp.processor=input('Enter the processor:')
# # hp.ram=input('Enter the ram:')
# hp.display()

#? student
# class student:
#     def __init__(self,name,registerno):
#         self.name=name
#         self.registerno=registerno
#     def display(self):
#         print('Name of the Student:',self.name)
#         print('Student RegisterNo:',self.registerno)
# print(student('Darshu','M21PIB13'))
# print(student.name)
# # y.display()

#~ fruit
# class fruit:
#     def __init__(self,color):
#         self.color=color
# apple=fruit('Red')
# print(apple.color)

#^ Calculator
# class calculator:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def add(self):
#         print('add:',self.a+self.b)
#     def sub(self):
#         print('sub:',self.a-self.b)
#     def multiply(self):
#         print('multiply:',self.a*self.b)
#     def division(self):
#         print('division:',self.a/self.b)
# x=calculator(20,5)
# x.add()
# x.sub()
# x.multiply()
# x.division()

#& Teacher
# class teacher:
#     def __init__(self,name,subject):
#         self.name=name
#         self.subject=subject
#     def display(self):
#         print('Name of the teacher:',self.name)
#         print('Subject:',self.subject)
# t1=teacher('Sugan','English')
# t2=teacher('David','Maths')
# t1.display()
# print('*'*50)
# t2.display()

# a="5"
# # b=str(a)
# c=int(a)
# # print(type(b))
# print(type(c))




# x = 41

# if x > 10:
#   print("Above ten,")
#   if x > 20:
#     print("and also above 20!")
#   else:
#     print("but not above 20.")


# a=[3,5,8,9]
# b=a.copy()
# print(b)
# b.append(12)
# print(b)
# print(a)