# # x=lambda a,b,c:a+b+c
# # print(x(5,2,6)) 

# def func(b):
#     return lambda a:a*b
# b=func(3)
# print(b(5))
# # print(func(3))


# def add(x,y):
#     return x+y
# print(add(2,8))

# add=lambda x,y:x+y
# a=lambda x:3*x
# # print(add(2,8))

# def multiple(n):
#     return lambda x:n*x
# a=multiple(3)
# print(a(5))


students=[("ram",23),("priya",28),("sam",25)]
print(sorted(students))
students.sort(key=lambda x:x[1],reverse=True)
print(students)