# write a program using hybrid inheritance of classes that displays a student's inf.

class Uni:
    def __init__(self, uni_name):
        self.uni_name = uni_name

    def show_details(self):
        return self.uni_name


class Course(Uni):
    def __init__(self, uni_name, course_name):
        Uni.__init__(self, uni_name)
        self.course_name = course_name

    def show_details(self):
        super().show_details()
        return self.course_name


class Branch(Uni):
    def __init__(self, uni_name, branch_name):
        Uni.__init__(self, uni_name)
        self.branch_name = branch_name

    def show_details(self):
        super().show_details()
        return self.branch_name


class Faculty(Branch):
    def __init__(self, uni_name, branch_name, fac_name):
        Branch.__init__(self, uni_name, branch_name)
        self.fac_name = fac_name

    def show_details(self):
        return self.fac_name


class Student(Faculty, Course):
    def __init__(self, uni_name, branch_name, fac_name, course_name, stud_name):
        Faculty.__init__(self, uni_name, branch_name, fac_name)
        Course.__init__(self, uni_name, course_name)
        self.stud_name = stud_name

    def show_details(self):
        super().show_details()
        return self.stud_name


s = Student(input('Enter your university name : '), input('Enter the branch name : '),
            input('Enter the faculty name : '), input('Enter the course name : '), input('Enter the student name : '))
print(f'Student name : {s.stud_name}\nUniversity name : {s.uni_name}\nBranch name : {s.branch_name}\n'
      f'Faculty name :{s.fac_name}\nCourse name : {s.course_name}\n')

# MRO is used to solve this problem in this case
print(Student.mro())
# Student -> Faculty -> Branch -> Course -> Uni
