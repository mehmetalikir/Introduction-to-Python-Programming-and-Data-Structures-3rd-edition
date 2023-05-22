# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Custom Exception) In Programing Exercise 13.10 you were asked to create an
Exam class that raises an exception. Extend this exercise by creating your own
custom exceptions. Create a ExamException base class and two additional custom
exception classes which inherit from it --NegativeResultException and
ExcessiveResultException (these classes can be stubs with no other attributes
and methods). These should be raised in the Exam clas when an invalid score is
set. The first should be raised when a negative exam score is assigned and the
 second when an exam score is higher than 100.
    Write a test program that uses try and except statements to create an exam and
    prints an error message when the score result is illegal.'''


class NegativeResultException(Exception):
    pass


class ExcessiveResultException(Exception):
    pass


class ExamException:
    def __init__(self, name, score):
        self.name = name
        if score < 0:
            raise NegativeResultException("Invalid score")
        if score > 100:
            raise ExcessiveResultException("Invalid score")
        self.score = score


def main():
    exam1 = ExamException("Maths", -1)
    print(exam1.score)

    exam2 = ExamException("Maths", 101)
    print(exam2.score)


main()
