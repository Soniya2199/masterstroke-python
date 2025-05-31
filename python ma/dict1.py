# #Nested dict -> inside dict
# family={
#     'child1':{
#         'Name':'Jeeva',
#         'Age':23
#     },
#     'child2':{
#         'Name':'Aravind',
#         'Age':20
#     },
#     'child3':{
#         'Name':'Harini',
#         'Age':15
#     },
# }
# # print(family)
# # print(len(family))
# print(family['child2']['Name'])
# print(family.get('child1'))
# print(family.keys())
# print(family.values())
# print(family.items())
# print(family)
# print(family.pop('child3'))
# print(family.popitem())
# family['child2']['Age']=21
# print(family)
# family.update({'child1':{'Name':'swetha'}})
# print(family) #dd


library={
    "dept1":{
        "book1":{
            "name":"Database Management",
            "copy":10,
        },
        "book2":{
            "name":"cloud computing",
            "copy":20,
        },
        "book3":{
            "name":"Operating system",
            "copy":13,
        }  
    },
    "dept2":{
         "book1":{
            "name":"Historical",
            "copy":8,
        },
          "book2":{
            "name":"Economics",
            "copy":11,
        }
    }
}

# print(library)
# print(library.get("dept2")) #specified key values
# print(library.values()) #only values
# print(library.keys()) #only keys
# print(library.pop("dept2")) #removed value
# print(library)
# library.popitem() #removes the last items
# print(library)
library.update({"dept1":{"book1":{"name":"sql","copy":9}}})
print(library)  #dd
# print(library["dept2"]["book2"])
# print(library["dept2"]["book2"]["copy"])
# college=library.copy()
# print(college)
# print(library["dept1"]["book3"]["name"])

# library["dept2"]=["book3":{"name":"Economics","copy":11}]
# print(library) #error add values

# library["dept2"]["book3"]=[{"name":"Economics","copy":11}]
# print(library) #adding elements 

# for asw in library:
#     print(asw)

# if "dept1" in library:
#     print("book1 is available in library")