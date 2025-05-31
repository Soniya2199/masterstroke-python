import math 

def perfect_square(n):
      a=math.sqrt(n)
      b=a**2==n
      if a and b:
        print(n, 'is a perfect square')
      else:
          print(n, 'is not a perfect square')
perfect_square(121)


# def perSq(num):
#     num=int(input('Enter the Number:'))
#     x=math.sqrt(num)
#     print(x)
#     if x**2==num:
#         print(num, 'is a perfect square')
#     else:
#         print(num, 'is not a perfect square')
# perSq('num')
