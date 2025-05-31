# a={1,2,3}
# b={'x','y','z'}
# c=a.union(b)
# print(c)
# d=a|b
# print(d)
# e={4,5,6}
# f=a.union(b,e)
# print(f)
# g=a|b|e
# print(g)
# h=(34,10,3,78)
# i=g.union(h)
# print(i)

# z={'a','b','c','m',True}
# y={'d','e','f','m',1}
# x=z.intersection(y)
# print(x)
# t=z&y
# print(t)
# s=[1,2,3,'m']
# u=z.intersection(s)
# print(u)

# ab=z.difference(y)
# print(ab)
# cd=z-y
# print(cd)

u={1,2,9}
v={1,2,3,4,5,6,7}
# t=u-v
# print(t)
# u.difference_update(v)
# print(u)
# s=u.symmetric_difference(v)
# print(s)
# u.symmetric_difference_update(v)
# print(u)
# s=u^v
# print(s)
# t=u.isdisjoint(v)
# print(t)
# t=u.issubset(v)
# print(t)
# t=u.issuperset(v)
# print(t)

# x={1,21,'ram','black','janani',945}
# y={'ram','white',3,'hello',765,10,True}
# print(y.union(x)) #combining all values togethers no repeated values
# print(x|y)
# z=('yellow',25)
# print(x.union(z)) #any datatypes can be used
# print(x|z) #set to set no other datatypes 

# print(x.intersection(y)) #common values from both variables
# x.intersection_update(y)
# print(x)

# print(x.difference(y)) #values present in x and not in y
# print(y-x)
# print(y.difference(z))
# print(x.difference_update(y))

# a=x.symmetric_difference(y) #omits the repeated values
# print(a)
# x.symmetric_difference_update(z) #combine both var n omits repeated value n change original var
# print(x)

# a=x.isdisjoint(z) #if intersetion returns f if not returns t
# print(a)
# a=x.isdisjoint(y) 
# print(a)

x={3,4}
y={3,4,5,6,7}
a=x.issubset(y)
print(a)

b=x.issuperset(y)
print(b)

# b=x.issubset(z)
# print(b)
# c=y.issubset(x)
# print(c)
