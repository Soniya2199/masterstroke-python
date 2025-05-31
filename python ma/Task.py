
#~
# def is_leap(year):
#     if year%4==0 and year%400==0:
#        leap=True
#        print("it is a leap year")
#     else:
#       leap=False
#       print("it is not a leap year")
#     return leap
# print(is_leap(2000))
# # if print(is_leap(2000))==False:
# #    print("it is not a leap year")
# # else:
# #    print("it is a leap year")

#! 
# n = int(input("Enter the Integer:"))
# if 1 <= n <= 50:
#     if n % 2 != 0:
#         print("weird")
#     elif n % 2 == 0 and 2 <= n <= 5:
#         print("Not Weird")
#     elif n % 2 == 0 and 6 <= n <= 20:
#         print("Weird")
#     elif n % 2 == 0 and n > 20:
#         print("Not Weird")
# else:
#     print("enter a valid number")

#^
n=int(input('Enter the Integer:'))
if 1<=n<=50:
    if (n%2!=0) or (n%2==0 and 6<=n<=20):
        print('weird')
    elif (n%2==0 and 2<=n<=5) or (n%2==0 and n>20):
        print('not weird')
else:
    print('enter a valid number')
