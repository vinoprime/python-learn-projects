print("Welcome")
print(
    """Create an array with 5 students names, 
    after that create a function which takes 2 params
    (allStudents & studentName) iterate over all students and find that
    specific user "StudentName"
    """)

class Student:
    name:str
    def __init__(self, name) -> None:
        self.name = name
        pass
    

students_list_object =[
    Student("A1"),
    Student("A2"),
    Student("A3"),
    Student("A4"),
    Student("A5"),
]


students_list =[
"V1","V2","V3","V4","V5"
]




def find_student_by_name(student_List:list, student_name:str):
    for student in student_List:
        if student == student_name:
            print("Found")
            print(student)
            return
    
    print("Not Found")
    return

def find_student_by_name_from_object(student_List:list, student_name:str):
    for student in student_List:
        if student.name == student_name:
            print("Found")
            print(student.name)
            return
    
    print("Not Found")
    return

find_student_by_name(students_list,"V4")
find_student_by_name_from_object(students_list_object,"A4")

    
            
            
