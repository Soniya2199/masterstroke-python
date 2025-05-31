class calculator:
    a=int(input('Enter the value:'))
    b=int(input('Enter the value:'))

    def addition(add,a,b):
        res=add.a+add.b
        print(res)
        
        # while res>=0:
        #     n=int(input('Enter the value:'))
        #     if n>=0:
        #         res=res+n
        #         print(res)
        #         # break
        
    def subtraction(sub,a,b):
        res=sub.a-sub.b
        print(res)

        while res>=0:
            n=int(input('Enter the value:'))
            if n>=0:
                res=res-n
                print(res)
                # break
    
    def multiplication(mul,a,b):
        res=mul.a*mul.b
        print(res)

        while res>=0:
            n=int(input('Enter the value:'))
            if n>=0:
                res=res*n
                print(res)
                # break

    def division(div,a,b):
        res=div.a/div.b
        print(res)

        while res>=0:
            n=int(input('Enter the value:'))
            if n>=0:
                res=res/n
                print(res)
                # break
    
c=calculator()
add=c.addition('a','b')
# c.subtraction('a','b')
# c.multiplication('a','b')
# c.division('a','b')



    
    

