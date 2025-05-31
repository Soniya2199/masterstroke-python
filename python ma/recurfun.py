# def a(n):
#     if (n>0):
#         res=n+a(n-1)
#         print(res)
#         return res
#     else:
#         return 0
# print(a(5))

# def fact(n):
#     if n==1:
#         return n
#     else:
#         return n*fact(n-1)
# num=int(input('Number:'))
# if num<=0:
#     print('Negative numbers')
# elif num==1:
#     print("1")
# else:
#     print(fact(num))

def toh(n,start,end,aux):
  if(n==1):
    print(f"Move disk 1 from {start} to",end)
    return
  toh(n-1,start,aux,end)
  print(f"Move disk {n} from {start} to",end)
  toh(n-1,aux,end,start)

n = int(input("Enter the number of disks: "))
toh(n,'A','B','C')
