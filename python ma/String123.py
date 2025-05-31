# a='hello'
# print(a)
# print(a[3]) #! index
# print(a[-4]) #! neg index
# print(a[1:4]) #! slicing
# print(a[-5:-3]) #! neg slicing
# print(a[:4]) #! no starting position
# print(a[2:]) #! no ending position

#~OPERATORS
#^ concat (+)
# b=3
# c=5
# print(b+c)

# b='hi'
# c='swe'
# d=b+' '+c
# print(d)

# b='hi'
# # c=5 #! instead
# c='5'
# d=b+c
# print(d) #!can only concatenate str (not "int") to str

# x=10
# y=20
# total =x+y
# print('Total:'+total) #!can only concatenate str (not "int") to str

# x=10
# y=20
# total =x+y
# print('Total:',total)

#&repetition (*)
# d='arav' *2 #! syntax: n*s or s*n
# print(d)
# d=2* 'arav'
# print(d)

#? comparison
# print('soni'=='Soni') #! == 
# print('soni'=='soni')
# print('soni'!='Soni') #! != 
# print('soni'!='soni')
# print('s'<'S') #! <
# print('S'<'s')
# print('s'<'s')
# print('s'<='S') #! <=
# print('S'<='s')
# print('s'<='s')
# print('S'>'s') #! >
# print('s'>'S')
# print('S'>='s') #! >=
# print('s'>='S')

#~ membership (in)
# x='soniya'
# print('soniya' in x)
# print('on' in 'soniya')
# print('soniya' not in x)
# print('on' not in 'soniya')

#^ escape***
# y="Black is a color that results from the \"absence or complete absorption\" of visible light."
# print(y) #! double quotes inside double quotes
# z="Black is a color that results from the \n absence or complete absorption\n of visible light."
# print(z) #! for new line
# f="Black is a color that results from the \tabsence or complete absorption\t of visible light."
# print(f) #! for a space 

#& slicing with third parameters
# a="Black is a color"
# print(a[3:17:3])
# print(a[16:2:-2])
# print(a[-15:-2:2])
# print(a[::-1]) #!reversing string using negative parameters

#? format string or interpolation(everything considered as string)
# x='arav'
# y=20
# print(f'Name is {x} and age is {y}')
# print(f'Name is {x.upper()} and age is {y}') 

#~ Methods
#^ strip()
# a=' hello '
# print(a.strip()) #! removes the whitespace before and after
# b='###Good###'
# print(b.strip('#')) #! removes characters

#& split() (return value in array format)
# a='Good Morning'
# print(a.split()) #! default by space
# b="Black is a color that results, from the absence or complete, absorption of visible light."
# print(b.split(',')) #! ,
# c="Black is a color that results, from the absence or complete, absorption of visible light."
# print(c.split(' ')) #! space
# d="Black is a color that results, from the absence or complete, absorption of visible light."
# print(d.split('l')) #! some value

#? join()
# x="Black is a color that results"
# y=x.split()
# print(y)
# print(' '.join(y))
# z=list(x)
# print(z)
