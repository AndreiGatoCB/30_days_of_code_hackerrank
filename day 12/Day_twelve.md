# DAY 12
## Objective
Today, we are building on our knowledge of arrays by adding another dimension. Check out the 
[Tutorial](https://www.hackerrank.com/challenges/30-2d-arrays/tutorial) tab for learning materials and an instructional 
video.

## Context
Given a _**6 x 6**_ 2D Array, _**A**_:
````
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
````

We define an hourglass in _**A**_ to be a subset of values with indices falling in this pattern in _**A**_'s graphical 
representation:
````
a b c
  d
e f g
````

There are _**16**_ hourglasses in _**A**_, and an hourglass sum is the sum of an hourglass' values.

## Task
Calculate the hourglass sum for every hourglass in _**A**_, then print the maximum hourglass sum.

## Example

In the array shown above, the maximum hourglass sum is _**7**_ for the hourglass in the top left corner.

## Input Format

There are _**6**_ lines of input, where each line contains _**6**_ space-separated integers that describe the 2D Array 
_**A**_.

## Constraints
- _**-9 <= a[i][j] <= 9**_
- _**0 <= i, j <= 5**_

## Output Format

Print the maximum hourglass sum in _**A**_.

## Sample Input
````
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0
````
## Sample Output
````
19
````
## Explanation

_**A**_ contains the following hourglasses:
````
1 1 1   1 1 0   1 0 0   0 0 0
  1       0       0       0
1 1 1   1 1 0   1 0 0   0 0 0

0 1 0   1 0 0   0 0 0   0 0 0
  1       1       0       0
0 0 2   0 2 4   2 4 4   4 4 0

1 1 1   1 1 0   1 0 0   0 0 0
  0       2       4       4
0 0 0   0 0 2   0 2 0   2 0 0

0 0 2   0 2 4   2 4 4   4 4 0
  0       0       2       0
0 0 1   0 1 2   1 2 4   2 4 0
````
The hourglass with the maximum sum (_**19**_) is:
````
2 4 4
  2
1 2 4
````

[Day twelve](https://www.hackerrank.com/challenges/30-2d-arrays/problem?isFullScreen=true).
