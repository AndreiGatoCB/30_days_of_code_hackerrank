# DAY 27
## Objective
Today's challenge puts your understanding of nested conditional statements to the test. You already have the knowledge 
to complete this challenge, but check out the 
[Tutorial](https://www.hackerrank.com/challenges/30-nested-logic/problem?isFullScreen=true) tab for a video on testing.

## Task
Your local library needs your help! Given the expected and actual return dates for a library book, create a program that
calculates the fine (if any). The fee structure is as follows:

1. If the book is returned on or before the expected return date, no fine will be charged (i.e.: _**fine = 0**_.
2. If the book is returned after the expected return day but still within the same calendar month and year as the
expected return date, _**fine = 15 Hackos x (the number of days late)**_.
3. If the book is returned after the expected return month but still within the same calendar year as the expected 
return date, the _**fine = 500 Hackos x (the number of months late)**_.
4. If the book is returned after the calendar year in which it was expected, there is a fixed fine of 
_**10000 Hackos**_.

## Example
_**d1, m1, y1 = 12312014**_ returned date
_**d2, m2, y2 = 112015**_ due date

The book is returned on time, so no fine is applied.

_**d1, m1, y1 = 112015**_ returned date
_**d2, m2, y2 = 12312014**_ due date

The book is returned in the following year, so the fine is a fixed 10000.

## Input Format

The first line contains _**3**_ space-separated integers denoting the respective _**day**_, _**month**_, and _**year**_
on which the book was actually returned.

The second line contains _**2**_ space-separated integers denoting the respective _**day**_, _**month**_, and _**year**_
on which the book was expected to be returned (due date).

## Constraints
- _**1 <= D <= 31**_
- _**1 <= M <= 12**_
- _**1 <= Y <= 3000**_
- _**It is guaranteed that the dates will be valid Gregorian calendar dates**_

## Output Format

Print a single integer denoting the library fine for the book received as input.

## Sample Input
````
STDIN       Function
-----       --------
9 6 2015    day = 9, month = 6, year = 2015 (date returned)
6 6 2015    day = 6, month = 6, year = 2015 (date due)
````

## Sample Output
````
45
````

## Explanation

Given the following return dates:
Returned: _**D1 = 9, M1 = 6, Y1 = 2015**_
Due: _**D2 = 6, M2 = 6, Y2 = 2015**_

Because _**Y2 = Y1**_, it is less than a year late.
Because _**M2 = M1**_, it is less than a month late.
Because _**D2 < D1**_, it was returned late (but still within the same month and year).

Per the library's fee structure, we know that our fine will be _**15 Hackos x (#days late)**_. We then print the result
of _**15 x (D1 - D2) = 15 x (9 - 6) = 45**_ as our output.

[Day twenty-seven](https://www.hackerrank.com/challenges/30-nested-logic/problem?isFullScreen=true)
