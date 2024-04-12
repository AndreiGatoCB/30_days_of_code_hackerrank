# DAY 26
## Objective
Today we will learn about running time, also known as time complexity. Check out the 
[Tutorial](https://www.hackerrank.com/challenges/30-running-time-and-complexity/tutorial) tab for learning materials and
an instructional video.

## Task
A prime is a natural number greater than _**1**_ that has no positive divisors other than _**1**_ and itself. Given a 
number, _**n**_, determine and print whether it is _**Prime**_ or _**Not prime**_.

**Note:** If possible, try to come up with a _**0(√n)**_ primality algorithm, or see what sort of optimizations you come
up with for an _**0(n)**_ algorithm. Be sure to check out the Editorial after submitting your code.

## Input Format

The first line contains an integer, _**T**_, the number of test cases.
Each of the _**T**_ subsequent lines contains an integer, _**n**_, to be tested for primality.

## Constraints
- _**1 <= T <= 30**_
- _**< <= n <= 2 x 10^9**_

## Output Format

For each test case, print whether _**n**_ is _**Prime**_ or _**Not prime**_ on a new line.

## Sample Input
````
3
12
5
7
````

## Sample Output
````
Not prime
Prime
Prime
````

## Explanation

Test Case 0: _**n = 12**_.
_**12**_ is divisible by numbers other than _**1**_ and itself (i.e.: _**2**_, _**3**_, _**4**_, _**6**_), so we print
_**Not prime**_ on a new line.

Test Case 1: _**n = 5**_.
_**5**_ is only divisible _**1**_ and itself, so we print _**Prime**_ on a new line.

Test Case 2: _**n = 5**_.
_**7**_ is only divisible _**1**_ and itself, so we print _**Prime**_ on a new line.

[Day twenty-six](https://www.hackerrank.com/challenges/30-running-time-and-complexity/problem?isFullScreen=true).
