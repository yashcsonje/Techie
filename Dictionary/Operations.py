
student = {'name' : 'Alice' , 'age' : 21 , 'grade' : 'A'} 
# Length
len(student)
3
# Key check
'grade' in student
True
'DOB' in student
False
# remove a key pair
grade_pop = student.pop("grade")
grade_pop 
'A'
student
{'name': 'Alice', 'age': 21}
