# try:
#     print(y)
# except SyntaxError:
#     print('z')
# except:
#     print('abc')
# finally:
#     print('xyz')

# x=-5
# if x<0:
#     raise Exception ('no number should be less than 5')

# a=25
# c="g"
# try:
#     b=a/c
# except ZeroDivisionError:
#     print("a cannot be divided by zero")
# else:
#     print("Error")
# finally:
#     print('Done...')

#~ EMA

# try:
#     a=input()
#     b=input()
#     print(a/b)
# except Exception as e:
#     print('Error',e) #! e-> wch print d error

try:
    a=int(input())
    b=int(input())
    print(d)
    c=input()
    print(c/b)
    
except ValueError as e:
    print("Error",e)
except TypeError as e:
    print("TypeError",e)
except Exception as e:
    print("Common Error",e)
finally:
    print('try block executed and finally printed.....')
