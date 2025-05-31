class calculator:
    a=int(input('Enter the value:'))
    b=int(input('Enter the value:'))

    def addition(add,a,b):
        add.res=add.a+add.b
        print(add.res)
    
    def subtraction(sub,a,b):
        sub.res=sub.a-sub.b
        print(sub.res)

    def multiplication(mul,a,b):
        mul.res=mul.a*mul.b
        print(mul.res)

    def division(div,a,b):
        div.res=div.a/div.b
        print(div.res)
    
calc=calculator()
calc.addition('a','b')
# calc.subtraction('a','b')
# calc.multiplication('a','b')
# calc.division('a','b')
result=calc.res

while True:
    operation=input('Enter The Operation:')
    n=int(input('Enter the value:'))
    if operation=='+':
        result=result+n
        print(result)
    elif operation=='-':
        result=result-n
        print(result)
    elif operation=='*':
        result=result*n
        print(result)
    elif operation=='/':
        result=result/n
        print(result)
    else:
        print('Exits')