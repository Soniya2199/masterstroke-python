import numpy as np

# #~ 3d
# # x=np.array([[[1,2,3],[4,5,6]],
# #             [[7,8,9],[0,1,2]]])
# # print(x.ndim)
# # print(x[0,0])
# # print(x[0,1])
# # print(x[1,0])
# # print(x[1,1])
# # print(x[0,0,1])

# # print(x[1,1:2])
# # print(x[0,0:2])
# # print(x[0:1,0:1])

# #^ 4d
y=np.array([[[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]],
           [[[13,14,15],[16,17,18]],[[19,20,21],[22,23,24]]]])
print(y.ndim)
# # print(y[0,1])
# # print(y[0,0,1,1])
# # print(y[1,1,1,0])
# # print(y[1,0:2])
# # print(y[1,1,1])
# # print(y[1,1:2,0:1,2]) #! to access row starting position 
# # print(y[1:2,1:2,1])
# # print(y[::-1]) #! reverse order
# # print(y[::-1,::-1])
# # print(y[::-1,::-1,::-1])
# print(y[::-1,::-1,::-1,::-1])

# a=np.array([1,2,3,4,5,6,7])
# print(a[2:6])
# print(a[3:])
# print(a[:5])
# print(a[-5:-2])
# print(a[-6:])
# print(a[:-4])
# print(a[1:5:2])
# print(a[-6:-2:3])

# b=np.array([[1,2,3],[4,5,6]])
# print(b[0:1,1])

# b=np.array([[1,2,3,7,8],[4,5,6,12,15]])
# # print(b[1:2,1:4])
# print(type(b))
# print(b.dtype)

# c=np.array(['a','b','c','d'],dtype='S')
# print(c.dtype)