import re

#~ search(pattern,data)

# a='The MRO diamond problem occurs when a class inherits from two CLASSES that both inherit from a common superclass, forming a diamond-shaped inheritance diagram'
# b=re.search('classes',a,re.IGNORECASE)
# # print(b) #! shows where the given word present
# # if b:
# #     print('Match')
# # else:
# #     print('No Match')
# if b:
#     print('match word',b.group())
# else:
#     print('No Match')

#^ match(search,string,flags=0)
# a='The MRO diamond problem occurs when a class inherits from two CLASSES that both inherit from a common superclass, forming a diamond-shaped inheritance diagram'
# b=re.match('The',a) #! checks only 1st word
# # b=re.match('MRO',a) 
# print(b)

#& finditer()
# a='The MRO diamond problem occurs when a class inherits from two CLASSES that both inherit from a common superclass, forming a diamond-shaped inheritance diagram'


#? MetaCharacter
#* []
# a='The MRO diamond problem occurs when a class inherits from two CLASSES that both inherit from a common superclass, forming a diamond-shaped inheritance diagram'
# x=re.findall('[a-e]',a)
# print(x)

#* \
# a='The MRO diamond problem occurs when a 5677 class inherits from two CLASSES that both inherit from a common superclass, forming a diamond-shaped inheritance diagram'
# x=re.findall('\d',a)
# print(x)

#* .
# a='The MRO diamond problem occurs when a class inherits from two CLASSES that both inherit from a common superclass, forming a diamond-shaped inheritance diagram'
# x=re.findall('c....n',a)
# print(x)

#* ^
# a='The MRO diamond problem occurs when a class inherits from two CLASSES that both inherit from a common superclass, forming a diamond-shaped inheritance diagram'
# x=re.findall('^diamond',a)
# # print(x)
# if x:
#     print('Present')
# else:
#     print('Not present')

#* $
# a='The MRO diamond problem occurs when a class inherits from two CLASSES that both inherit from a common superclass, forming a diamond-shaped inheritance diagram'
# x=re.findall('diagram$',a)
# # print(x)
# if x:
#     print('Present')
# else:
#     print('Not present')

#* * + ?
# a='The MRO diamond problem occurs when a class inherits from two CLASSES that both inherit from a common superclass, forming a diamond-shaped inheritance diagram'
# x=re.findall('d.*d',a)
# y=re.findall('d.+a',a)
# z=re.findall('diam.?nd',a)
# print(x)
# print(y)
# print(z)

#* {} |
# a='The MRO diamond problem occurs when a class inherits from two CLASSES that both inherit from a common superclass, forming a diamond-shaped inheritance diagram'
# x=re.findall('pr.{4}m',a)
# y=re.findall('class | both',a)
# print(x)
# print(y)

#~ 
#* \A
a='The MRO diamond problem occurs when a class inherits from two CLASSES that both inherit from a common superclass, forming a diamond-shaped inheritance diagram'
# x=re.findall("\AThe",a)
# print(x)

#* \b
# x=re.findall(r"\bses",a) #! ending
# print(x)

# x=re.findall(r"dia\b",a) #! beginning
# print(x)

#* \B (middle)
# x=re.findall(r"\Bond",a) #! ending
# print(x)

# x=re.findall(r"cla\B",a) #! beginning
# print(x)

#* \s S
# x=re.findall("\S",a)
# print(x)

#* \w W
# x=re.findall("\W",a)
# print(x)