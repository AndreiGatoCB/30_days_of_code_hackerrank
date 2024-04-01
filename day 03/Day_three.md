# DAY 3
## Objective
In this challenge, you will work with arithmetic operators. Check out the 
[Tutorial](https://www.hackerrank.com/challenges/30-operators/tutorial) tab for learning materials and an instructional 
video.

## Task
Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip), and tax 
percent (the percentage of the meal price being added as tax) for a meal, find and print the meal's total cost. Round 
the result to the nearest integer.

## Example
**_meal coast = 100_**
**_tip percent = 15_**
**_tax percent = 8_**
A tip of 15% * 100 = 15, and the taxes are 8% * 100 = 8. Print the value _123_ and return from the function.

## Function Description
Complete the solve function in the editor below.

solve has the following parameters:

- int meal_cost: the cost of food before tip and tax
- int tip_percent: the tip percentage
- int tax_percent: the tax percentage
Returns The function returns nothing. Print the calculated value, rounded to the nearest integer.

**Note:** Be sure to use precise values for your calculations, or you may end up with an incorrectly rounded result.

## Input Format
There are _3_ lines of numeric input:
- The first line has a double, _meal cost_ (the cost of the meal before tax and tip).
- The second line has an integer, _tip percent_ (the percentage of  being added as tip).
- The third line has an integer, _tax percent_ (the percentage of  being added as tax).

## Sample Input
```
12.00
20
8
```

## Sample Output
```
15
```

## Explanation

**Given:**
_meal_cost = 12, tip_percent = 20, tax_percent = 8_

**Calculations:**

_tip = 12 and 12/100 * 20 = 2.4_

_tax = 8 and 8/100 * 12 = 0.96_

_total_cost = meal_cost + tip + tax = 12 + 2.4 + 0.96 = 15.36_

_round(total_cost) = 15_

We round _total_cost_ to the nearest integer and print the result, _15_.

[Day three](https://www.hackerrank.com/challenges/30-operators/problem?isFullScreen=true).
