# DAY 5
## Objective
In this challenge, we're going to learn about the difference between a class and an instance; because this is an Object 
Oriented concept, it's only enabled in certain languages. Check out the 
[Tutorial](https://www.hackerrank.com/challenges/30-class-vs-instance/tutorial) tab for learning materials and an 
instructional video!

## Task
Write a Person class with an instance variable, _**age**_, and a constructor that takes an integer, _**initial_age**_, 
as a parameter. The constructor must assign _**initial_age**_ to _**age**_ after confirming the argument passed as 
_**initial_age**_ is not negative; if a negative argument is passed as _**initial_age**_, the constructor should set
_**age**_ to _**0**_ and print ``Age is not valid, setting age to 0.``. In addition, you must write the following 
instance methods:

1. yearPasses() should increase the  instance variable by .
2. amIOld() should perform the following conditional actions:
   - If , print ``You are young.``.
   - If  and , print ``You are a teenager.``.
   - Otherwise, print ``You are old.``.
   
To help you learn by example and complete this challenge, much of the code is provided for you, but you'll be writing  
everything in the future. The code that creates each instance of your Person class is in the main method. Don't worry 
if you don't understand it all quite yet!

**Note:** Do not remove or alter the stub code in the editor.

## Input Format

Input is handled for you by the stub code in the editor.

The first line contains an integer, _**T**_ (the number of test cases), and the _**T**_ subsequent lines each contain 
an integer denoting the _**age**_ of a Person instance.

## Constraints
- 1 <= T <= 4
- -5 <= age <= 30

## Output Format

Complete the method definitions provided in the editor so they meet the specifications outlined above; the code to test 
your work is already in the editor. If your methods are implemented correctly, each test case will print _**2**_ or 
_**3**_ lines (depending on whether or not a valid _**initial_age**_ was passed to the constructor).

## Sample Input
````
4
-1
10
16
18
````
## Sample Output
````
Age is not valid, setting age to 0.
You are young.
You are young.

You are young.
You are a teenager.

You are a teenager.
You are old.

You are old.
You are old.
````
## Explanation

Test Case 0: _**initiate_age = -1**_
Because _**initiate_age < 0**_, our code must set _**age**_ to _**0**_ and print the "Age is not valid..." message 
followed by the young message. Three years pass and _**age = 3**_, so we print the young message again.

Test Case 1: _**initiate_age = 10**_
Because _**initiate_age < 13**_, our code should print that the person is young. Three years pass and _**age = 13**_, so
we print that the personis now a teenager.

Test Case 2: _**initiate_age = 16**_
Because _**initiate_age <= 13 < 18**_, our code should print that the person is a teenager. Three years pass and 
_**age = 19**_, so we print that the 
person is old.

Test Case 3: _**initiate_age = 18**_
Because _**initiate_age >= 18**_, our code should print that the person is old. Three years pass and the person is still
old at _**age = 21**_, so we print the old message again.

**The extra line at the end of the output is supposed to be there and is trimmed before being compared against the test 
case's expected output. If you're failing this challenge, check your logic and review your print statements for spelling
errors.**

[Day five](https://www.hackerrank.com/challenges/30-class-vs-instance/problem?isFullScreen=true)