# DAY 15
## Objective
Today we're discussing scope. Check out the 
[Tutorial](https://www.hackerrank.com/challenges/30-scope/tutorial) tab for learning materials and an instructional
video!

------------------------------------------------------------------------------------------------------------------

The absolute difference between two integers, _**a**_ and _**b**_, is written as _**|a-b|**_. The maximum absolute 
difference between two integers in a set of positive integers, _**elements**_, is the largest absolute difference 
between any two integers in _**__elements**_.

The Difference class is started for you in the editor. It has a private integer array (_**elements**_) for storing 
_**N**_ non-negative integers, and a public integer (_**maximumDifference**_) for storing the maximum absolute 
difference.

## Task
Complete the Difference class by writing the following:
- A class constructor that takes an array of integers as a parameter and saves it to the _**__elements**_ instance 
variable.
- A computeDifference method that finds the maximum absolute difference between any _**2**_ numbers in _**__elements**_ 
and stores it in the _**maximumDifference**_ instance variable.

## Input Format
You are not responsible for reading any input from stdin. The locked Solution class in the editor reads in _**2**_ lines
of input. The first line contains _**N**_, the size of the elements array. The second line has _**N**_ space-separated 
integers that describe the _**__elements**_ array.

## Constraints
- _**1 <= N <= 10**_
, _**1 <= __elements[i] <= 100, where 0 <= i <= N-1**_

## Output Format
You are not responsible for printing any output; the Solution class will print the value of the _**maximumDifference**_ 
instance variable.

## Sample Input
````
STDIN   Function
-----   --------
3       __elements[] size N = 3
1 2 5   __elements = [1, 2, 5]
````

## Sample Output
````
4
````

## Explanation
The scope of the _**__elements**_ array and _**maximumDifference**_ integer is the entire class instance. The class 
constructor saves the argument passed to the constructor as the _**__elements**_ instance variable (where the 
computeDifference method can access it).

To find the maximum difference, computeDifference checks each element in the array and finds the maximum difference 
between any _**2**_ elements: 
- _**|1 - 2| = 1**_
- _**|1 - 5| = 4**_
- _**|2 - 5| = 3**_

The maximum of these differences is _**4**_, so it saves the value _**4**_ as the _**maximumDifference**_ instance 
variable. The locked stub code in the editor then prints the value stored as _**maximumDifference**_, which is _**4**_.

[Day fifteen](https://www.hackerrank.com/challenges/30-scope/problem?isFullScreen=true).