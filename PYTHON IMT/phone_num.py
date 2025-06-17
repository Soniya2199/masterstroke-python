import re
# def validate_phno(n):
#     # try:
#         pattern=re.compile(r"^[6-9]\d{9}$")
#         if pattern.match(n):
#             return True
#         else:
#             raise Exception ("Invalid number")
# n=input()
# validate_phno(n)

# import phonenumbers as pn
# from phonenumbers import geocoder as g

# ph_num=pn.parse("+91")


# def validate_phno(n):
#         try:
#             n=str(n).strip()
#             pattern=re.compile(r"^[6-9]\d{9}$")
#             return bool(pattern.match(n))
#         except Exception as e:
#             print('Invalid number',e)
#             return False
# while True:
#     try:
#         n=input()
#         if validate_phno(n):
#              print('valid')
#              break
#         else:
#              print('invalid')
#     except Exception as e:
#          print('Error',e)
#     break

def validate_phno(n):
    pattern=re.compile(r"^[6-9]\d{9}$")
    return pattern.match(n)

n=input('Enter The num:')
if validate_phno(n):
    print('success')
else:
    print('invalid')
