# DAY 17
## Objective
Today, we're getting started with Exceptions by learning how to parse an integer from a string and print a custom error 
message. Check out the [Tutorial](https://www.hackerrank.com/challenges/30-exceptions-string-to-integer/tutorial) tab 
for learning materials and an instructional video!

## Task
Read a string, _**S**_, and print its integer value; if _**S**_ cannot be converted to an integer, print ``Bad String``.

**Note:** You must use the String-to-Integer and exception handling constructs built into your submission language. If 
you attempt to use loops/conditional statements, you will get a _**0**_ score.

## Input Format
A single string, _**S**_.

## Constraints
- _**1 <= |S| <= 6**_, where _**|S|**_ is the length of string _**S**_.
- _**S**_ is composed of either lowercase letters (_**a - 2**_) or decimal digits (_**0 - 9**_).

## Output Format
Print the parsed integer value of _**S**_, or ``Bad String`` if _**s**_ cannot be converted to an integer.

## Sample Input 0
````
3
````

## Sample Output 0
````
3
````

## Sample Input 1
````
za
````

## Sample Output 1
````
Bad String
````

## Explanation

Sample Case _**0**_ contains an integer, so it should not raise an exception when we attempt to convert it to an 
integer. Thus, we print the _**3**_.

Sample Case _**1**_ does not contain any integers, so an attempt to convert it to an integer will raise an exception. 
Thus, our exception handler prints ``Bad String``.

[Day seventeen](https://www.hackerrank.com/challenges/30-exceptions-string-to-integer/problem?isFullScreen=true).
