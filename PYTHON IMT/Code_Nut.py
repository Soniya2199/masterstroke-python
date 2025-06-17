
#~ Extract number from String
# import re
# print(re.findall(r'\d+',input("Strings values:"))) #! \d returns the number

#^ Find the 2nd largest number
# num =list(map(int,input('Numbers:').split()))
# num.remove(max(num))
# print(max(num))

#&
a=input('Enter a value:').split()
b=input('Enter a value:').split()
print(list(set(a) & set(b)))