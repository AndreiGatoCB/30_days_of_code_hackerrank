# DAY 7
## Objective
Today we will expand our knowledge of strings, combining it with what we have already learned about loops. Check out the 
[Tutorial](https://www.hackerrank.com/challenges/30-review-loop/tutorial) tab for learning materials and an 
instructional video.

## Task
Given a string, _**S**_, of length _**N**_ that is indexed from _**0**_ to _**N - 1**_, print its even-indexed and 
odd-indexed characters as _**2**_ space-separated strings on a single line (see the Sample below for more detail).

*Note:* _**0**_ is considered to be an even index.

## Example
_**s = adbecf**_

Print ``abc def``

## Input Format

The first line contains an integer, _**T**_ (the number of test cases).

Each line _**i**_ of the _**T**_ subsequent lines contain a string, _**S**_.

## Constraints
- _**1 <= T <= 10**_
- _**2 <= length of S <= 10000**_
- 
## Output Format
For each String _**Sj**_ (where _**0 <= j <= T-1**_), print _**Sj**_'s even-indexed characters, followed by a space, 
followed by _**Sj**_'s odd-indexed characters.

## Sample Input
````
2
Hacker
Rank
````
## Sample Output
````
Hce akr
Rn ak
````
## Explanation

Test Case 0: _**S = Hacker**_

_**S[0] = "H"**_

_**S[1] = "a"**_

_**S[2] = "c"**_

_**S[3] = "k"**_

_**S[4] = "e"**_

_**S[5] = "r"**_

The even indices are _**0**_, _**2**_, and _**4**_, and the odd indices are _**1**_, _**3**_, and _**5**_. We then print
a single line of _**2**_ space-separated strings; the first string contains the ordered characters from _**S**_'s even 
indices (_**Hce**_), and the second string contains the ordered characters from _**S**_'s odd indices (_**akr**_).

Test Case 1: _**Rank**_

_**S[0] = "R"**_

_**S[1] = "a"**_

_**S[2] = "n"**_

_**S[3] = "k"**_

The even indices are _**0**_ and _**2**_, and the odd indices are _**1**_ and _**3**_. We then print a single line of 
_**2**_ space-separated strings; the first string contains the ordered characters from _**S**_'s even indices
(_**Rn**_), and the second string contains the ordered characters from _**S**_'s odd indices (_**ak**_).

[Day seven](https://www.hackerrank.com/challenges/30-review-loop/problem?isFullScreen=true)