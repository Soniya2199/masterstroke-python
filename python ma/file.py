# f=open("New.txt",'w')
# print(f.write('Hello'))
# f.close()

# # f=open('New.txt','r')
# # print(f.read())
# # f.close()

import os
# import shutil
# # os.remove('New.txt')
# # if os.path.exists('New.txt'):
# #     os.remove('New.txt')
# # else:
# #     print('file not exits')

# # shutil.rmtree('New')

# file_path="C:\Users\ogo\Desktop\python ma"

# with open(file_path,'w') as file:
#     file.write(file_path,"Hello")

# path of the current script
path = 'C:\Users\ogo\Desktop\Html\Microsoft VS Code\_\resources\app\extensions\python'
 
# Before creating
dir_list = os.listdir(path)
print("List of directories and files before creation:")
print(dir_list)
print()
 
# Creates a new file
with open('myfile.txt', 'w',encoding='utf-8') as fp:
    pass
 
# After creating
dir_list = os.listdir(path)
print("List of directories and files after creation:")
print(dir_list)