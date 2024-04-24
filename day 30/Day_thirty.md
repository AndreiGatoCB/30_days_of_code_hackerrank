# DAY 30
## Objective
Welcome to the last day! Today, we're discussing bitwise operations. Check out the 
[Tutorial](https://www.hackerrank.com/challenges/30-bitwise-and/problem?isFullScreen=true) tab for learning materials 
and an instructional video!

## Task
Given set _**S = {1, 2, 3, ..., N}**_. Find two integers, _**A**_ and _**B**_ (where _**A < B**_), from set _**S**_ such
that the value of _**A&B**_ is the maximum possible and also less than a given integer, _**K**_. In this case, _**&**_ 
represents the bitwise AND operator.

## Function Description
Complete the bitwiseAnd function in the editor below.

bitwiseAnd has the following parameter(s):
- int N: the maximum integer to consider
- int K: the limit of the result, inclusive

## Returns
- int: the maximum value of _**A&B**_ within the limit.

## Input Format

The first line contains an integer, _**T**_, the number of test cases.
Each of the _**T**_ subsequent lines defines a test case as _**2**_ space-separated integers, _**N**_ and _**K**_, 
respectively.

## Constraints
- _**1 <= T <= 10^3**_
- _**2 <= N <= 10^3**_
- _**2 <= K <= N**_

## Sample Input
````
STDIN   Function
-----   --------
3       T = 3
5 2     N = 5, K = 2
8 5     N = 8, K = 5
2 2     N = 8, K = 5
````

## Sample Output
````
1
4
0
````

## Explanation

_**N = 5**_, _**K = 2**_ _**S = {1, 2, 3, 4, 5}**_ 

All possible values of _**A**_ and _**B**_ are:

1. _**A = 1 , B = 2 ; A & B = 0**_
2. _**A = 1 , B = 3 ; A & B = 1**_
3. _**A = 1 , B = 4 ; A & B = 0**_
4. _**A = 1 , B = 5 ; A & B = 1**_
5. _**A = 2 , B = 3 ; A & B = 2**_
6. _**A = 2 , B = 4 ; A & B = 0**_
7. _**A = 2 , B = 5 ; A & B = 0**_
8. _**A = 3 , B = 4 ; A & B = 0**_
9. _**A = 3 , B = 5 ; A & B = 1**_
10. _**A = 4 , B = 5 ; A & B = 4**_

The maximum possible value of _**A&B**_ that is also _**< (K = 2)**_ is _**(1**_, so we print _**1**_ on a new line.

[Day thirty](https://www.hackerrank.com/challenges/30-bitwise-and/problem?isFullScreen=true).
