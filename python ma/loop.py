# WHILE LOOPS
# a=1
# while a<7:
#     print(a)
#     if a==5:
#         break
#     a=a+1

# i=10
# while i<=200:
#     # print(i)
#     print(i,end=',')
#     i=i+10

# reverse order
# i=100
# while i>=50:
#     print(i)
#     i=i-5

# i=6
# fact=1
# while i>0:
#     fact=fact*i
#     i=i-1
#     print(fact)

# flower=input('enter the value:')
# while flower=='jasmine':
#     print('jasmine is avaliable in basket')
#     break
# else:
#     print('jasmine is not avaliable in basket')

#! Reverse order (Tables)
# x=int(input('enter the number for x:'))
# while x>0:
#     y=12
#     while y>0:
#         z=x*y
#         print(f'{x}*{y}={z}')
#         y-=1
#     x-=1
#     print()

#~ Tables 1 to 12
a=int(input('enter the number a:'))
while a<=12:
    b=1
    while b<=10:
        c=a*b
        print(f'{a}*{b}={c}')
        # print(f'{a}*{b}={c}', end=' ')
        b+=1
    a+=1
    print()

#***salary increment using while loops
# Name=input('Enter the Name:')
# Salary=int(input('Enter the Salary:'))
# while True:
#     if Salary>=15000 and Salary<=24999:
#         Salary=Salary+15000
#         print(f'Salary increament for {Name} is {Salary:.2f}')
#         break
#     elif Salary>=25000 and Salary<=34999:
#         Salary=Salary+10000
#         print(f'Salary increament for {Name} is {Salary:.2f}')
#         break
#     elif Salary>=35000:
#         Salary=Salary+5000
#         print(f'Salary increament for {Name} is {Salary:.2f}')
#         break
#     else:
#         print('no increment')
#         break

#***5 subject mark using while and storing in list***
# Name = input("Enter the Name:")
# print("Mark of the student" + " " + Name)
# marks=[] #empty list
# subjects=5
# i=0
# while i<subjects:
#      mark=int(input(f'Enter the mark of subject:'))
#      if 0<=mark and mark<=100:
#         marks.append(mark)
#         i=i+1
#      else:
#         print("Enter a valid mark")
# print(f'Marks:{marks}')
# total=0
# j=0
# while j<subjects:
#     total=total+marks[j]
#     j=j+1
# print(f'Total mark of {Name} is {total}')
# average=total/subjects
# print(f'Average for {Name} is:{average}')
# k=0
# while k<len(marks):
#     if marks[k]>35:
#         print("passed")
#     else:
#         print("failed")

#********
# i=0
# total=0
# while i<len(l):
#     total=total+n[i]
#     i=i+1
# print(total)
# avg=total/len(l)
# print(avg)

# if (avg>80):
#     print("Distination Grade")
# elif (79>=avg>=60):
#     print("First Class Grade")
# elif (59>=avg>=35):
#     print("Second Class Grade")
# else:
#     print("Failed")

#*****
# Name=input('Enter the name:')
# for 
# mark=int(input('Enter the marks:'))
# l=[]
# l.append(mark)
# print(l)
    

