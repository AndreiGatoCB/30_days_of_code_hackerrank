class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    def __init__(self, first_name, last_name, id_number, scores_):
        super().__init__(firstName=first_name, lastName=last_name, idNumber=id_number)
        self.grade = str()
        self.scores_ = scores_

    def calculate(self):
        scores_ = self.scores_
        total = sum(scores_)
        cant = len(scores_)
        average = total / cant
        self.grade = str()
        if average < 40:
            self.grade = 'T'
        elif 40 <= average < 55:
            self.grade = 'D'
        elif 55 <= average < 70:
            self.grade = 'P'
        elif 70 <= average < 80:
            self.grade = 'A'
        elif 80 <= average < 90:
            self.grade = 'E'
        elif 90 <= average <= 100:
            self.grade = 'O'

        return self.grade

# Class Constructor
#
#   Parameters:
#   firstName - A string denoting the Person's first name.
#   lastName - A string denoting the Person's last name.
#   id - An integer denoting the Person's ID number.
#   scores - An array of integers denoting the Person's test scores.
#
# Write your constructor here


#   Function Name: calculate
#   Return: A character denoting the grade.
#
# Write your function here

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
# numScores = int(input())  # not needed for Python
scores = list(map(int, input().split()))
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())