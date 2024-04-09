# DAY 16
## Objective
Today we will work with a Linked List. Check out the 
[Tutorial](https://www.hackerrank.com/challenges/30-linked-list/tutorial) tab for learning materials and an 
instructional video.
-----
A Node class is provided for you in the editor. A Node object has an integer data field, _**data**_, and a Node instance
pointer, _**next**_, pointing to another node (i.e.: the next node in the list).

A Node insert function is also declared in your editor. It has two parameters: a pointer, _**head**_, pointing to the 
first node of a linked list, and an integer, _**data**_, that must be added to the end of the list as a new Node object.

## Task
Complete the insert function in your editor so that it creates a new Node (pass _**data**_ as the Node constructor 
argument) and inserts it at the tail of the linked list referenced by the _**head**_ parameter. Once the new node is
added, return the reference to the _**head**_ node.

**Note:** The _**head**_ argument is null for an empty list.

## Input Format

The first line contains T, the number of elements to insert.
Each of the next _**T**_ lines contains an integer to insert at the end of the list.

## Output Format

Return a reference to the _**head**_ node of the linked list.

Sample Input
````
STDIN   Function
-----   --------
4       T = 4
2       first data = 2
3
4
1       fourth data = 1
````

## Sample Output
````
2 3 4 1
````

## Explanation

_**T = 4**_, so your method will insert _**4**_ nodes into an initially empty list.
First the code returns a new node that contains the data value _**2**_ as the _**head**_ of the list. Then create and 
insert nodes _**3**_, _**4**_, and _**1**_ at the tail of the list.

![Linked list explanation](../imgs/test_day_16_b.PNG)

[Day sixteen](https://www.hackerrank.com/challenges/30-linked-list/problem?isFullScreen=true)