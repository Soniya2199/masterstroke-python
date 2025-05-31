import re

# a = "Regular functions in Python are the standard way of defining and using functions. They are defined using the def keyword, followed by the function name, a set of parentheses that can contain parameters, and a colon. The function body, which contains the code to be executed when the function is called, is indented."
# b = re.sub("\s", "z", a) #! subsitute
# c= re.search()
# print(b)
# if b:
#     print('It is a match')
# else:
#     print('no match')

a = "Regular functions in Python are the standard way of defining and using functions. They are defined using the def keyword, followed by the function name, a set of parentheses that can contain parameters, and a colon. The function body, which contains the code to be executed when the function is called, is indented."
b=re.findall('in',a) 
print(b)