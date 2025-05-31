# a=15
# b=12
# if a<b:
#     print('a<b')
# elif a==b:
#     print("a and b are equal")
# else :
#     print("a and b are not equal")

# print('a') if a>b else print('b')

# c=11
# if a>b and a<c:
#     print('x')
# if not a>b:
#     print('x')
# if not a<b and b>c:
#     print('And condition satisified')
# else:
#     print('not satisfied')

# if a<b or a>c:
#     print('hi')
# if not a<b or a>c:
#     print('hello')

# x=5
# y=3
# if x>3:
#     print('x is greater than 3')
#     if x>6:
#         print('x is greater than 4')
#     else :
#         print('y')

# if x>y:
#     pass

#***LOGICAL AND WITH CONDITIONALS***
#if

# age=15
# nationality='Indian'
# if age>18 and nationality=='Indian':
#     print("eligible for voting")

#if else and 
# age=25
# nationality='Indian'
# if age>18 and nationality=='Indian':
#     print("eligible for voting")
# else:
#     print("Not eligible for voting")

#if elif else 
# age=21
# nationality='other'
# if age>18 and nationality=='Indian':
#     print("eligible for exam and fees Rs.750.00")
# elif age>18 and nationality=='other':
#     print("eligible for exam and fees Rs.1000.00")
# else:
#     print("not eligible for exam")

#***LOGICAL OR WITH CONDITIONALS***
#if


#***salary increament using if else***
# salary=int(input('enter the salary:'))
# # print(salary)
# # print(type(salary))
# if salary>=10000 and salary<=14999:
#     salary=salary+5000
#     print(f'salary increased for 10000:{salary}')
# elif salary>=15000 and salary<=29999:
#     salary=salary+3000
#     print(f'salary increased for 15000:{salary}')
# elif salary>=30000:
#     salary=salary+2000
#     print(f'salary increased:{salary}')
# else:
#     print('no increment')

#****
# subjects=5
# marks=[79,86,97,35,92]
# j=0
# total=0
# while j<subjects:
#     total=total+marks[j]
#     j=j+1
# Average=total/len(marks)
# # print(Average)

#****
# k=0
# while k<len(marks):
#     if marks[k]>35:
#         print("passed")
#         k=k+1
#     else:
#         print("failed")
#         break
    

#***student mark and grades and range of marks btw 100***

# Name = input("Enter the Name:")
# print("Mark of the student" + " " + Name)
# Tamil = int(input("Enter the Tamil:"))
# if 0<=Tamil and Tamil<=100:
#     print
# else:
#     print("Enter a valid mark")
#     Tamil = int(input("Enter the Tamil:"))
# English = int(input("Enter the English:"))
# if 0<=English and English<=100:
#     print
# else:
#     print("Enter a valid mark")
#     English = int(input("Enter the English:"))
# Maths = int(input("Enter the Maths:"))
# if 0<=Maths and Maths<=100:
#     print
# else:
#     print("Enter a valid mark")
#     Maths = int(input("Enter the Maths:"))
# Science = int(input("Enter the Science:"))
# if 0<=Science and Science<=100:
#     print
# else:
#     print("Enter a valid mark")
#     Science = int(input("Enter the Science:"))
# Social = int(input("Enter the Social:"))
# if 0<=Social and Social<=100:
#     print
# else:
#     print("Enter a valid mark")
#     Social = int(input("Enter the Social:"))
# Total_Marks = Tamil + English + Maths + Science + Social
# print(f"Total Marks for Student {Name}:{Total_Marks}")
# avg = Total_Marks/5
# print(f"Average Mark of {Name} is {avg}")
# if ((avg>80) and (Tamil and English and Maths and Science and Social>35)):
#     print(Name + " " + "Distination Grade")
# elif ((79>=avg>=60) and (Tamil and English and Maths and Science and Social>35)):
#     print(Name + " " + "First Class Grade")
# elif ((59>=avg>=35) and (Tamil and English and Maths and Science and Social>35)):
#     print(Name + " " + "Second Class Grade")
# else:
#     print(Name + " " + "Failed")



