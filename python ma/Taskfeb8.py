# def is_leap():
#     year=int(input('enter the year:'))
#     if year%4==0 and year%400==0:
#             print('leap year')
#     else:
#             print('not a leap year') 
# is_leap()

# def is_leap(year):
#     if year%4==0 and year%400==0:
#        leap=True
#     else:
#       leap=False
#       print(year,'is a not multiple of 4 and 400 hence its not a leap year') 
# if True:
#    print(year ,'is a multiple of 4 and 400 hence its a leap year')

# is_leap(1800)

#^^^^^^^^^^
# def is_leap(year):
#     if year%4==0 and year%400==0:
#         print('leap year')
#         return True
#     elif year/100!=0:
#         print('not a leap year')
#         return False
# print(is_leap(1800))

# def is_leap(year):
#     leap=True
#     if year%4==0:
#         if year%100==0:
#             if year%400==0:
#                 return True
#                 lp=leap
#             else:
#                 lp=not leap
#             if lp==leap:
#                     print(year,'is a multiple of 4 and 400 hence its a leap year')
#             else:
#                     print(year,'is not a multiple of 4 and 400 hence its not a leap year')
# is_leap(2200)       
#     elif year%100==0:
#         leap=False
   
#     print(year,'is a multiple of 4 and 400 hence its a leap year')
# else:
#     print(year,'is a multiple of 4 and 400 hence its a leap year')

#~~~
def is_leap(year):
    if (year % 400 == 0) and (year % 100 != 0) and (year % 4 ==0) :
        leap = True
        return leap
    else:
        leap = False
        return leap

    if leap==True:
        print("leap year")
    else:
        print("not a leap year")
print(is_leap(2000))


    
# def is_leap(year):
    
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 leap = True
#             else:
#                 leap = False
#         else:
#             leap = True
#     else:
#         leap = False
    
#     if leap==True:
#         print(year,'is a multiple of 4 and 400 hence its a leap year')
#     else:
#         print(year,'is not a multiple of 4 and 400 hence its not a leap year')
# is_leap(2000)

