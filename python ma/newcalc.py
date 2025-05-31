a=int(input('Enter the value:'))
op=input('Enter the sign +,-,*,/:')
# if op!='+' or '-' or '*' or '/':
#     raise ArithmeticError ('Enter a valid operator')
b=int(input('Enter the value:'))

class calculator:
   
    def add(a,b):
        if op=='+':
            res = a+b
            return res
    
    def sub(a,b):
        if op=='-':
            res =a-b
            return res
        
    def mul(a,b):
        if op=='*':
            res=a*b
            return res

    def div(a,b):
        if op=='/':
            res=a/b
            return res
 
calc=calculator()
ad=calculator.add(a,b)
su=calculator.sub(a,b)
mu=calculator.mul(a,b)
di=calculator.div(a,b)

result=ad or su or mu or di

while True:
    print(result)
    op=input('Enter the sign +,-,*,/:')
    # if op!='+' or '-' or '*' or '/':
    #     raise ArithmeticError ('Enter a valid operator')
    nx=int(input('Enter the value:'))
    if op=='+':
        result=result+nx
    elif op=='-':
        result=result-nx
    elif op=='*':
        result=result*nx
    elif op=='/':
        result=result/nx
    else:
        print(result)
