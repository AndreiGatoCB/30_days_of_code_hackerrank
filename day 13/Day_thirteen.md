# DAY 13
## Objective
Today, we're delving into Inheritance. Check out the attached 
[tutorial](https://www.hackerrank.com/challenges/30-inheritance/tutorial) for learning materials and an instructional 
video.

## Task
You are given two classes, Person and Student, where Person is the base class and Student is the derived class. 
Completed code for Person and a declaration for Student are provided for you in the editor. Observe that Student 
inherits all the properties of Person.

Complete the Student class by writing the following:

- A Student class constructor, which has  parameters:
  1. A string, _**firstName**_.
  2. A string, _**lastName**_.
  3. An integer, _**idNumber**_.
  4. An integer array (or vector) of test scores, _**scores**_.
- A char calculate() method that calculates a Student object's average and returns the grade character representative of their calculated average:

![Grading](../imgs/test_day_13_b.PNG)

## Input Format

The locked stub code in the editor reads the input and calls the Student class constructor with the necessary arguments.
It also calls the calculate method which takes no arguments.

The first line contains _**firstName**_, _**lastName**_, and _**idNumber**_, separated by a space. The second line 
contains the number of test scores. The third line of space-separated integers describes _**scores**_.

## Constraints
- _**1 <= length of firstName, length of lastName <= 10**_
- _**length of idNumber = 7**_
- _**0 <= score <= 100**_

## Output Format

Output is handled by the locked stub code. Your output will be correct if your Student class constructor and calculate()
method are properly implemented.

## Sample Input
````
Heraldo Memelli 8135627
2
100 80
````
## Sample Output
````
 Name: Memelli, Heraldo
 ID: 8135627
 Grade: O
````
## Explanation

This student had _**2**_ scores to average: _**100**_ and _**80**_. The student's average grade is 
_**(100 + 80) / 2 = 90**_. An average grade of _**90**_ corresponds to the letter grade _**O**_, so the calculate() 
method should return the character ``O``.

[Day thirteen](https://www.hackerrank.com/challenges/30-inheritance/problem?isFullScreen=true).