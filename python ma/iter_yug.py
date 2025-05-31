# l=['w',4,7,'k','hi',True] #! iterable (collection of items)
# print(dir(l))
# it=iter(l) #! it is iterator obj
# print(dir(it))
# print(it) #! memory location
# # print(next(it))
# # print(next(it))
# # print(next(it))
# # print(next(it))
# # print(next(it))
# # print(next(it))
# for x in it:
#     print(x)

#~ method
# l1=[10,20,30,40,50] #! iterable
# # l1_obj=iter(l1) #! list as iter (exp-> l1.__iter__())
# l1_obj=l1.__iter__() #! iterator and iter()
# print(type(l1_obj)) #! o/p 'list_iterator'
# # print(next(l1_obj))
# print(l1_obj.__next__()) #! next()
# for x in l1_obj:
#     print(x)

#^
# l2=[21,22,23,24,25]
# l2_obj=iter(l2)
# print(id(l2))
# l3_obj=iter(l2_obj)
# print(id(l2_obj))

#& checking iterator or iterable
obj=iter(eval(input('Enter the Object:')))
obj_dir=dir(obj)
if '__int__' in obj_dir and '__next__' in obj_dir:
    print('Iterator')  
elif '__init__' in obj_dir:
    print('Iterable')
else:
    print('no Iteration')