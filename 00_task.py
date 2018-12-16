class student:

    Sum_grade=0
    Sum_age=0
    NumOfSudent=0
    
    def __init__(self, grade, age):
        self.grade=grade
        self.age=age
        student.Sum_grade+=grade
        student.Sum_age+=age
        student.NumOfSudent+=1

    @classmethod
    def avg_grade(G):
        return G.Sum_grade/G.NumOfSudent

    @classmethod
    def avg_age(A):
        return A.Sum_age/A.NumOfSudent

s1 = student(80,22)
s2 = student(93,24)
s3 = student(84,32)
s4 = student(75,28)
print('----------student No.1---------')
print("The age of student is:{}\nthe grade of student is:{}\nThe Average grade of students is:{}\nThe Average age of students: {}\n".format(s1.age,s1.grade,student.avg_grade(),student.avg_age()))
print('----------student No.2---------')
print("The age of student is:{}\nthe grade of student is:{}\nThe Average grade of students is:{}\nThe Average age of students: {}\n".format(s2.age,s2.grade,student.avg_grade(),student.avg_age()))
print('----------student No.3---------')
print("The age of student is:{}\nthe grade of student is:{}\nThe Average grade of students is:{}\nThe Average age of students: {}\n".format(s3.age,s3.grade,student.avg_grade(),student.avg_age()))
print('----------student No.4---------')
print("The age of student is:{}\nthe grade of student is:{}\nThe Average grade of students is:{}\nThe Average age of students: {}\n".format(s4.age,s4.grade,student.avg_grade(),student.avg_age()))


"""
_________________________OUTPUT_________________________


----------student No.1---------
The age of student is:22
the grade of student is:80
The Average grade of students is:83.0
The Average age of students: 26.5

----------student No.2---------
The age of student is:24
the grade of student is:93
The Average grade of students is:83.0
The Average age of students: 26.5

----------student No.3---------
The age of student is:32
the grade of student is:84
The Average grade of students is:83.0
The Average age of students: 26.5

----------student No.4---------
The age of student is:28
the grade of student is:75
The Average grade of students is:83.0
The Average age of students: 26.5
"""
