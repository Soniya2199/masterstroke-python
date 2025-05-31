
#~ is and ==

# a=2
# b=4
# c=b
# print(id(a))
# print(id(b))
# print(id(c))

# x='hello'
# # y='hello'
# y='welcome'
# print(id(x),id(y))
# print(x==y)
# print(x is y)

# x=[1,2,3]
# y=[1,2,3] #! new memory space is created...
# print(id(x),id(y))
# print(x==y)
# print(x is y)

#^ empty array
# import numpy as np

# x=np.empty(0)
# print(x)

#& shallow copy and deep copy
# import copy as c

# a=[[1,2,3],['hi','hello'],['x','y','z']]
# b=c.copy(a)

# print(a)
# print(b)

# print(id(a))
# print(id(b)) #! diff memory address

# print(id(a[0][2])) #! same memory address of inner list
# print(id(b[0][2]))
# print('*'*25)
# b[0][2]=21
# print(b[0][2])
# print('*'*25)
# print(id(a[0][2])) 
# print(id(b[0][2]))

# x=[[1,2,3],['hi','hello'],['x','y','z']]
# y=c.deepcopy(x)

# print(x)
# print(y)

# print(id(x))
# print(id(y)) #! diff memory address

# print(id(x[1])) 
# print(id(y[1]))

# print(id(x[1][0]))
# y[1][0]='so'
# print(id(y[1][0]))

#? range and xrange

# for x in range(4):
#     print(x)


# for r in xrange(4):
    # print(r)

#~ generator

value = 0
def my_generator(n):
    global value
    while value < n:
        yield value
        value += 2
# print(my_generator(15))
for value in my_generator(15):
    print(value)