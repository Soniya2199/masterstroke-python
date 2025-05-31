# STRING
# INDEXING
# a="25 35"
# b="Good evening"
# c=a+" "+b
# print(c)
# print(f"{a}{b}")
# print(f"{a} is number string and {b} is string")
# print(a)
# print(b)
# print(type(a)) #type of data
# print(type(b))
# print(len(a)) #length
# print(len(b))
# print(a[2]) #return space value
# print(b[8])

# c="Searches the string for a specified value and returns the position of where it was found"
# print(c[14:20])
# print(c[-70:-2])
# print(c[-5:-15]) #return no values n also show no error
# d="098754321 123457890"
# print(d[7:19])
# print(d[-18:-9])
# print(d[-3:-11])

# flower=["A rose is either a woody perennial flowering plant of the genus, Rosa in the family Rosaceae or the flower it bears",
#         "Lotus plants are adapted to grow in the flood plains of slow-moving rivers and delta areas",
#         "Lilies are a group of flowering plants which are important in culture and literature in much of the world"]
# x,y,z=flower
#print(type(flower))
#print(len(flower))
# print(x)
# print(x[30])
# print(x[12:30])
# print(type(x))
# print(x[:25])
# print(x[-45:])
#print(x[:-5])
#print(x[-12:25]) #returns no values
# print(x.split())
# print(x.split(" "))
# print(x.split(","))
# #print(flower[100:150]) #its a list
# print(y)
# print(y[10:25])
# print(y[-50:-12])
#print(flower)
#print(flower.split(" ")) #list has no split function

#concat
# s=    ["A rose is either a woody perennial flowering plant of the genus, Rosa in the family Rosaceae or the flower it bears",
#         "Lotus plants are adapted to grow in the flood plains of slow-moving rivers and delta areas",
#         "Lilies are a group of flowering plants which are important in culture and literature in much of the world"]
# a,b,c=s
# u=a+" "+b+" "+c
# print(u)

#format string or interpolation
# a=
#print(f"{a}{b}") #default args
#print(f"{s}") #error list
#print(f"{c}")
# print(f'{0}{2}')

#replace
#print(a.replace("rose","hibicus"))
#print(a.upper())
#print(c.lower())
# d=b.split(",")
# print(d)

# print(a.strip())
# print(a)
#print(b.strip())

#join
# z="Good Morning"
# print(z.split(" "))  #returns values in array format
# y=z.split(" ")
# print(y)
# x=' '.join(y) # joins 
# print(x)

# a="apple"
# b="pineapple"
# c="orange"
# #d=' '.join(a,b,c)
# # print(d) #error only one parameters accepted
# e=('red','orange','yellow','pink','blue')
# print(' '.join(e))
# print(type(e))
# print(' '.join(f'{a}{b}{c}')) 
# print(f"{a} {b} {c}")
# z="Lotus plants are adapted to grow in the flood plains of slow-moving rivers and delta areas"
# print(z.split(' '))/'"?????????: "
# x=5
# print(x)
# x='hi'
# print(x)
# print(id(x)) #memory loc id (in string memory loc changes every time)
# x='hello'
# print(x)
# print(id(x))

#Escape character (dou quotes inside dou quo can't be used [\" "\])
# a="Lotus plants are adapted to \"grow in the flood plains of slow-moving rivers\" and delta areas"
# print(a)

# LIST append
# c1=['red','orange','pink','blue','green']
# c2=['yellow','brown','voilet']
# c2.append(c1)
# print(c2)
# c=c2.append(c1)
# print(c)
# print(c1)
# print(c2)
# print(c1+c2) #o/p none    dd
# print(c2[3]) #index position
# n=[1,2,3,4]
# c=c1+n
# print(c)
# n.append(c2)
# print(n)
# print(n[0])
# print(n[1])
# print(n[2])
# print(n[3])
# print(n[4])      #dd

#index
# c=c2.index('voilet')
# print(c)

#insert
# c2.insert(2,'black') # by index positive and value
# print(c2)
# c1[1:3]=['white','grey','sky blue'] #changing element by index range
# print(c1)
# c1.append(c2)
# print(c1)

#extend
# c2.extend(c1)
# print(c2)

#count
# print(c1.count('red'))
# print(len(c2))

#copy
# n=c1.copy()
# print(n)
# c=c2[:] #slice operator to copy data
# print(c)
# z=c1+n+c2
# print(z)

#sort
# c2.sort()
# print(c2)
# n.append(c1)
# print(n)
# # n.sort()
# # print(n)  
# z=[20,1999,756,44] 
# z.sort()
# print(z) #dd
# c1.sort(reverse=True)
# print(c1)
# n.sort(reverse=True)
# print(n)

#reverse
# c1.reverse()
# c2.append(c1)
# print(c2)
# c2.reverse()
# print(c2)  #dd


#pop
# c2.pop()
# print(c2)
# c1.pop()
# print(c1)

#clear
# n.clear()
# print(n)

#remove
# c2.remove('brown')
# print(c2)
# c1.remove()
# print(c1)  #TypeError: list.remove() takes exactly one argument (0 given)
# n.remove(1)
# print(n)

#delete
# del n[2]
# print(n)
# del n
# print(n)

# #loop
# for m in n:
#     #print(m)
#     print(m,end=' ') #to print in straight line hori


