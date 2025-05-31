
a=int(input('Enter the value:'))
b=int(input('Enter the value:')) 
c=input('Enter the sign + or -:')
class calculator:
    if c == '+':
        def add(a,b):
            res = a + b
            return res
    # elif c == '-':
    #      def sub(a,b):
    #          res = a - b
    #          return res
print(type(c))
calc=calculator()
m=calculator.add(a,b)
# m=calculator.sub(a,b)
print(m)
result=m


# while True:
#     operation=input('Enter The Operation:')
#     n=int(input('Enter the value:'))
#     if operation=='+':
#         result=result+n
#         print(result)
#     elif operation=='-':
#         result=result-n
#         print(result)