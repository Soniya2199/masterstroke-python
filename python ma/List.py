#list used to store multiple values and any type of datatypes, duplicate values are allowed and in []

car=['bmw','swift','ford','mahindra','renault','toyato']
# print(car[2]) #through index value
# car[2]='audi' #changing value by index
# print(car[2])
# print(len(car)) #length
# print(car[2:3]) #slicing 
# car[1:3]=["ferrar"] #changing value by positive value
#print(car)

# car[-5:-2]=['honda','skoda','hyundai'] #changing value by negative value
# print(car)
# car[2:4]=['tata','maruti','kia']
# print(car)
# car[2]=['a','b']
# print(car)

# car.append('audi') #elements will be added at the last
# print(car)
# car.insert(2,'c')
# print(car)
# a=[1,2,3]
# b=[4,5,6]
# a.extend(b)
#print(a)
# a.remove(3) #direct value
# print(a)
# car.remove('toyato') 
# print(car)

# car.pop(2) #removing element by position
# print(car)
# car.pop() #without index value removes last value
# print(car)
# del car[1]
# print(car)
# # del car
# car.clear()
# print(car)
#print(a)
# for b in reversed(car):
#     print(b)
# print(car)
# car.sort()
# print(car)
car.sort(reverse=True)
print(car)

# bike=car.copy()
# print(bike)
# c=a+b
# print(c)
