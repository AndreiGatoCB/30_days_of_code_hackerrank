# DAY 18
## Objective
Yesterday's challenge taught you to manage exceptional situations by using try and catch blocks. In today's challenge, 
you will practice throwing and propagating an exception. Check out the 
[Tutorial](https://www.hackerrank.com/challenges/30-more-exceptions/tutorial) tab for learning
materials and an instructional video.

## Task
Write a Calculator class with a single method: int power(int,int). The power method takes two integers, _**n**_ and 
_**p**_, as parameters and returns the integer result of _**n^p**_. If either _**n**_ or _**p**_ is negative, then the
method must throw an exception with the message: ``n and p should be non-negative.``

**Note:** Do not use an access modifier (e.g.: public) in the declaration for your Calculator class.

## Input Format
Input from stdin is handled for you by the locked stub code in your editor. The first line contains an integer, _**T**_,
the number of test cases. Each of the _**T**_ subsequent lines describes a test case in _**2**_ space-separated integers
that denote _**n**_ and _**p**_, respectively.

## Constraints
- No Test Case will result in overflow for correctly written code.

## Output Format

Output to stdout is handled for you by the locked stub code in your editor. There are _**T**_ lines of output, where 
each line contains the result of _**n^p**_ as calculated by your Calculator class power method.

## Sample Input
````
4
3 5
2 4
-1 -2
-1 3
````

## Sample Output
````
243
16
n and p should be non-negative
n and p should be non-negative
````

## Explanation

_**T = 4**_

_**T0**_: _**3**_ and _**5**_ are positive, so power returns the result of _**3^5**_, which is _**243**_.

_**T1**_: _**2**_ and _**4**_ are positive, so power returns the result of _**2^4**_=, which is _**16**_.

_**T2**_: Both inputs (_**-1**_ and _**-2**_) are negative, so power throws an exception and 
``n and p should be non-negative.`` is printed.

_**T3**_: One of the inputs (_**-1**_) is negative, so power throws an exception and ``n and p should be non-negative.``
is printed.

[Day eighteen](https://www.hackerrank.com/challenges/30-more-exceptions/problem?isFullScreen=true).