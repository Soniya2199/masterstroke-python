
#~ simple even
# n=int(input('Enter a Number:'))
# if n%2==1:
#     print('Even Number')
# else:
#     print('Odd Number')

#! Simple odd with value
# n=int(input('Enter a number:'))
# if n%2==1:
#     print(f'{n} is Odd Number')
# else:
#     print(f'{n} is Even NUmber')

#^ function and value in args
# def EvenOdd(n):
#     return n%2==0
# print(EvenOdd(5))

#& function with user input
def EvenOdd(n):
    return n%2==0
n=int(input('Enter a value:'))
print(EvenOdd(n))
if EvenOdd(n)==True:
    print(f'{n} is a Even NUmber')
else:
    print(f'{n} is Odd NUmber')
    