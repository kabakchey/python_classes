# import utils
# # from utils import print_table
# import student
#
# st1 = student.Student("Alice", 19)
# st2 = student.Student("Bob", 22, 3)
#
# # st1.name = "Alice"
# # st2.name = "Bob"
#
# print(st1.name, st1.year, st1.age)
# print(st2.name, st2.year, st2.age)
#
# #
# # Student.print_info(st1)
# # Student.print_info(st2)
#
# print("----")
# st1.print_info("UA")
# st2.print_info()
#
# st1.papers.append("Math")
# st2.papers.append("Literature")
#
# st1.papers_local.append("Physics")
# st2.papers_local.append("Astronomy")
#
# st1.print_papers()
# st2.print_papers()
#


import course
import professor
import student


if __name__ == "__main__":
    pr1 = professor.Professor("Dr. Adams")
    pr2 = professor.Professor("Dr. Smith")
    course1 = course.Course("ML")

    course1.add_lecturer(pr1)
    course1.add_lecturer(pr2)
    course1.print_info()

    pr1.add_course(course1)
    pr1.print_info()
    pr2.print_info()

    st1 = student.Student("Alice")
    st1.print_info(lang="UA")

    # print(pr1)



