# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Raise an Exception) Create a class called Exam, which records the names of a
person who takes the exam and the score they obtained. The nae and score
should be assigned in the __init__() function. When an attempt is made to
allocate a negative score or a score which os iver 100,
a RuntimeError exception should be raised.'''


class Exam:
    def __init__(self, name, score):
        self.name = name
        if score < 0 or score > 100:
            raise RuntimeError("Invalid score")
        self.score = score


def main():
    exam1 = Exam("Maths", 99)
    print(exam1.score)

    exam2 = Exam("Maths", 101)
    print(exam2.score)


main()
