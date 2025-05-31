
#***with range(start,stop,step)***
# for x in range(2,10,3):
#     print(x)

# for a in range(-2,-12,-2):
#     print(a)

# for a in range(-12,-2,2):
#     print(a)

# for a in reversed(range(-12,-2,2)):
#     print(a)

#***with range(stop)***
# for y in range(8):
#     print(y)

# for y in reversed(range(8)):
#     print(y)

# for y in range(-20):
#     print(y) #! stop we cannot give -ve value

#***with range(start,stop)***
# for z in range(1,6):
#     print(z)

# for z in range(-1,6):
#     print(z)

# for z in range(-8,-1):
#     print(z)

# for z in reversed(range(-8,-1)):
#     print(z)

#***else***
# color=['pink','black','red','blue','green']
# for x in color:
#     if color=='white':
#         print('no color')
#         break
# else:
#         print('add color')

#***string***
# x='apple'
# for i in x:
#     # print(i) #accessing string
#     print(i,end='')
# print(type(i))

# y='sweet'
# for j in y[::-1]:
#     print(j) #reverse order using slicing

# z='hello'
# for i in reversed(z):
#     print(i) #reverse order using reversed keywords

# c='White is the lightest color and is achromatic'
# for j in c.split():
#     print(j) #accessing words
#     print(len(j))

#***list***
# a=[1,21,'rose',True,'hi']
# for b in a:
#     print(b)

# for c in range(len(a)):
#     print(a[c]) #using loop and range

# [print(b) for b in a] #comprehension

# for b in reversed(a):
#     print(b) #reverse

#***Dictionary***
# d={
#     'child1':{
#         'name':'arav',
#         'age':'25',
#         'place':'blr'
#         },
#     'child2':{
#         'name':'abi',
#         'age':'25',
#         'place':'chn' 
# }}
# for x in d:
#     print(x) #only key values

# for y in d:
#     print(d[y]) #using [] accessing values

# for i in d.keys():
#     print(i)

# for j in d.values():
#     print(j)

# for i,j in d.items():
#     print(i,j)

