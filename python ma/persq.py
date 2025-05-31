def persq(n):
    # if n<0:
    #     return False
    x=int(n**0.5)
    return x*x==n

num=int(input('Enter the Number:'))

if persq(num):
    print(num, 'is a perfect square')
else:
    print(num, 'is not a perfect square')