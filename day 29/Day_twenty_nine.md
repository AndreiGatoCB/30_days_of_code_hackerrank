# DAY 29
## Objective
Today, we're working with regular expressions. Check out the 
[Tutorial](https://www.hackerrank.com/challenges/30-regex-patterns/tutorial) tab for learning materials and an 
instructional video!

## Task
Consider a database table, Emails, which has the attributes First Name and Email ID. Given _**N**_ rows of data 
simulating the Emails table, print an alphabetically-ordered list of people whose email address ends in 
_**@gmail.com**_.

## Input Format

The first line contains an integer, _**N**_, total number of rows in the table.

Each of the _**N**_ subsequent lines contains _**2**_ space-separated strings denoting a person's first name and email 
ID, respectively.

## Constraints
- _**2 <= N <= 30**_
- Each of the first names consists of lower case letters _**[a - z]**_ only.
- Each of the email IDs consists of lower case letters _**[a - z]**_, _**@**_ and _**.**_ only.
- The length of the first name is no longer than 20.
- The length of the email ID is no longer than 50.

## Output Format

Print an alphabetically-ordered list of first names for every user with a gmail account. Each name must be printed on a 
new line.

## Sample Input
````
6
riya riya@gmail.com
julia julia@julia.me
julia sjulia@gmail.com
julia julia@gmail.com
samantha samantha@gmail.com
tanya tanya@gmail.com
````

## Sample Output
````
julia
julia
riya
samantha
tanya
````

[Day twenty-nine](https://www.hackerrank.com/challenges/30-regex-patterns/problem?isFullScreen=true).
