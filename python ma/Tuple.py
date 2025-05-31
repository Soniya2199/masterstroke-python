# a=(1,'a',34,'red','black',899)
# print(a)
# print(type(a))
# print(len(a))
# b=("Soniya",) #assigning single value in variable
# print(type(b))
# print(len(b))

#accessing elements through index value
# print(a[0])
# print(a[1])
# print(a[2])
# print(a[3])
# print(a[4])
# print(a[5])

#updating through index values
a=(1,'a',34,'red','black',899)
# a[2]=65
# print(a) #error
c=list(a) #converting tuple to list
# print(type(c))
# c[2]=65
# print(c)
# a=tuple(c)
# print(a)
# print(type(a))
# c[1:3]=[5,'orange','pink',21] #changing values
# print(c)
# print(c[0])
# print(c[1])
# print(c[2])
# print(c[3])
# print(c[4])
# print(c[5])
# print(c[6])
# print(c[7])  #dd index position
# a=tuple(c) #converting list to tuple
# print(a)
# print(a[6])

# a=(1,'a',34,'red','black',899)
# c=list(a)
# print(c)
# c[-4:-2]=['hi',10,'bye']  #negative
# print(c)
# print(c[0])
# print(c[1])
# print(c[2])
# print(c[3])
# print(c[4])
# print(c[5])
# print(c[6])
# a=tuple(c)
# print(a)

# #append
# x=(1,2,3,'hello','welcome','bye')
# y=(99,'Good evening',23,'white')
# z=list(x)
# cp=z.copy()
# print(cp)
# print(z)z.insert(3,'color')
# print(z)
# x=tuple(z)
# print(x)
# a=list(y)
# print(a)
# # z.append(999)
# # print(z)
# a.append(z)
# print(a)
# # x=tuple(z)
# # print(x)
# y=tuple(a)
# print(y)
# a.extend(z)
# print(a)
# z.insert(3,'color')
# print(z)
# x=tuple(z)
# print(x)
# v=x.index('welcome')
# print(v)
# z.pop()
# print(z)
# z.sort()
# print(z)
# z.reverse()
# print(z)
# z.clear()
# print(z)
# a.remove(23)
# print(a)
# del x
# print(x)
# x=tuple(z)
# print(x)
# y=tuple(a)
# print(y)

#unpack
# car=('maruti','hyundai','tata','swift')
# (a,b,c,d)=car
# print(a)
# (a,*b,c)=car
# print(a)
# print(b)
# fruits=('apple','orange','pineapple','papaya','banana','kiwi')
# (a,b,*c,d)=fruits
# print(b)
# print(c)

#tuple to tuple (we can add)
# a=(1,2,3)
# b=('x','y','z')
# c=a+b
# print(c)
# d=b*2
# print(d)
# e=d.count('x')
# print(e)
# f=d.index('z')
# print(f)

