from Student_data import School as sch, Student as st

class StudentMarks:
    def __init__(self,English,Tamil,Maths,Science,Social):
        self.English=English
        self.Tamil=Tamil
        self.Maths=Maths
        self.Science=Science
        self.Social=Social
    
    def Subject_Mark(sub):
        All_sub=sub.English,sub.Tamil,sub.Maths,sub.Science,sub.Social
        print('Student Subject Marks:',All_sub)

    def Average(av):
        Total=av.English,av.Tamil,av.Maths,av.Science,av.Social
        avg=sum(Total)/len(Total)
        return avg
    
    def Grade(gra):
        if gra.Average()>=90:
            return 'A'
        elif 89>=gra.Average()>=70:
            return 'B'
        elif 69>=gra.Average()>=50:
            return 'C'
        elif 49>=gra.Average()>=36:
            return 'D'
        else:
            return 'F'
        
    def display(dis):
        dis.Subject_Mark() #! calling Subject_Mark() method
        print(f'Student Average Mark:{dis.Average()}')
        print(f'Student Grade:{dis.Grade()}') 

#& Created a lists for cls StudentMarks
student_list=[StudentMarks(78,80,67,88,84),StudentMarks(96,94,98,100,99)]

for xyz in student_list:
    xyz.display()

# x=sch('SDA','X','A').SDetail()
stud=st('SDA','X','A','Saravana','03/10/1994',30,'Chennai',7010138495)
stud.StudentDetails()
             
        
    