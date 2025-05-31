# def adds(a,b):
#     print('add:',a+b)
# # for i in range(100):
# #     a=int(input('a:'))
# #     b=int(input('b:'))
# adds(35,5)
# print('*'*50)

# def simple(p,n,r):
#     p=int(input('Principle:'))
#     n=int(input('No of years:'))
#     r=float(input('Rate of interest:'))
#     s=(p*n*r)/100
#     print('Simple Interest:',s)
#     print(locals())
# simple(0,0,0)

# ^ local variable (scope)
# def func(n):
#     name='swetha' #! local variable
#     print(name)
#     print(n)
#     print(locals()) #! returns in dict format
# func(3)

# & global variable (scope)
# a='hello' #! global
# def func():
#     b='Welcome' #! local
#     a='10' #! local
#     print(a)
#     print(b)
# func()
# print(a)
# print(globals()) #! identifier

# ? To access the global variables inside function
x = "Welcome"  #! global
a = 21

def func():
    y = "arav"
    global a
    a = a - 3
    print(a)  #! UnboundLocalError [use global keyword]
    print(y)
func()
