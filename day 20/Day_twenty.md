# DAY 20
## Objective
Today, we're learning about Interfaces. Check out the 
[Tutorial](https://www.hackerrank.com/challenges/30-interfaces/tutorial) tab for learning materials and an instructional
video!

## Task
The ``AdvancedArithmetic`` interface and the method declaration for the abstract ``divisorSum(n)`` method are provided 
for you in the editor below.

Complete the implementation of ``Calculator`` class, which implements the ``AdvancedArithmetic`` interface. The 
implementation for the ``divisorSum(n)`` method must return the sum of all divisors of _**n**_.

## Example
_**n = 25**_

The divisors of _**25**_ are _**1, 5, 25**_. Their sum is _**31**_.

----
The divisors of _**20**_ are _**1, 2, 4, 5, 10, 20**_ and their sum is _**42**_.

## Input Format

A single line with an integer, _**n**_.

## Constraints
- _**1 <= n <= 1000**_

## Output Format

You are not responsible for printing anything to stdout. The locked template code in the editor below will call your 
code and print the necessary output.

## Sample Input
````
6
````

## Sample Output
````
I implemented: AdvancedArithmetic
12
````
## Explanation

The integer _**6**_ is evenly divisible by _**1**_, _**2**_, _**3**_, and _**6**_. Our divisorSum method should return
the sum of these numbers, which is _**1 + 2 + 3 + 6 = 12**_. The Solution class then prints _**I implemented: 
AdvancedArithmetic**_ on the first line, followed by the sum returned by divisorSum (which is _**12**_) on the second
line.

[Day twenty](https://www.hackerrank.com/challenges/30-interfaces/problem?isFullScreen=true).
