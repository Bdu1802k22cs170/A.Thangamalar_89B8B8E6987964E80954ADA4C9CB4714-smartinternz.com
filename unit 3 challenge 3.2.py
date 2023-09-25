'''
implement a function called sort_students that takes a list of student objects as input and sorts the
list based on their CGPA(cumulative grade point average) in descending order.each student object
has the following attributes: name (string),roll_number(string),and chpa(float).test the function
with different input lists of students
'''

class student:


def__init__(self,name,roll_number,cgpa):
  self.name_name
  self.roll_number=roll_number
  self.cgpa


def sort_students(students _list):
  #sort the list of students in descending order of CGOA
  sorted_students=sorted (student_list,
                         ket=lambdastudent) studen.cgpa,
  return sorted sort_students
  #syntax-lambda arg.exp
  return sorted_students


#example.useage:
student=[
  student("hari","A123",7.8),
  student ("srikanth","A124",8.9),
  student ("saumaya","A125",9.1),
  student ("mahidhar","A126",9.9),
]

sorted_students=sort_students(students)

#print the sorted list of students
for students in sorted_students:
print("name;{}, roll number;{},CGPA{}". format(student.name,
                                               student roll_number
      student.cgpa