"""Write a Python function student_data () that will print the ID of a student (student_id).
If the user passes an argument student_name or student_class the function will print the student name and class."""

'''def student_data(student_name='', student_class='', student_id=''):
    return f'Student ID: {student_id}\nStudent Name: {student_name}\nClass: {student_class}'
    
name , clas = input("Enter your name and your class: ").split() 
id = int(input("Enter your ID: "))
print(student_data(student_name = name, student_class = clas, student_id = id))'''

def student_data(student_id, **kwargs):
    print(f'\nStudent ID: {student_id}')
    if 'student_name' in kwargs:
        print(f"Student Name: $ {kwargs['student_name']}")
    
    if 'student_name' and 'student_class' in kwargs:
            print(f"\nStudent Name: $ {kwargs['student_name']}")
            print(f"Student Class: $ {kwargs['student_class']}")

 
student_data(student_id='SV12', student_name='Jean Garner')

student_data(student_id='SV12', student_name='Jean Garner', student_class ='V')
