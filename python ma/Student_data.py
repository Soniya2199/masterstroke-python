class School: #! parent class
    def __init__(sc,schoolname,std,sec): 
        sc.schoolname=schoolname
        sc.std=std
        sc.sec=sec

    def SDetail(sd):
        if __name__=='__main__':
            print(sd.schoolname)
            print(sd.std)
            print(sd.sec)

class Student(School): #! child class
    def __init__(sc,schoolname,std,sec,name,dob,age,place,ph_number):
        super().__init__(schoolname,std,sec)
        sc.name=name
        sc.dob=dob
        sc.age=age
        sc.place=place
        sc.ph_number=ph_number

    def StudentDetails(se):
        if __name__=='__main__':
            print('School Name:',se.schoolname)
            print('Standard:',se.std)
            print('Section:',se.sec)
            print('Student Name:',se.name)
            print('Student DOB:',se.dob)
            print('Student Age:',se.age)
            print('Student Place:',se.place)
            print('Student Phone number:',se.ph_number)
            print('='*50)

# ss=School('SDA','X','A') #! obj of parent class
# s=Student('SDA','X','A','Swarna','21/11/1999',25,'Chennai',9894513702) #! obj of stu 1
# s1=Student('SDA','X','A','Saravana','03/10/1994',30,'Chennai',7010138495) #! obj of stu 2
# ss.SDetail()
# s.StudentDetails()
# s1.StudentDetails()


