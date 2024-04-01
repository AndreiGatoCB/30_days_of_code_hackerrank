# DAY 14
## Objective
Today, we will extend what we learned yesterday about 
[Inheritance](https://docs.python.org/3/tutorial/classes.html#inheritance) to
[Abstract Classes](https://docs.python.org/3.5/library/abc.html). Because this is a very specific object-oriented 
concept, submissions are limited to the few languages that use this construct. Check out the 
[Tutorial](https://www.hackerrank.com/challenges/30-abstract-classes/tutorial) tab for learning materials and an 
instructional video.

## Task
Given a Book class and a Solution class, write a MyBook class that does the following:

- Inherits from Book
- Has a parameterized constructor taking these _**3**_ parameters:
  1. string _**title**_
  2. string _**author**_
  3. int _**price**_
- Implements the Book class' abstract display() method, so it prints these _**3**_ lines:
  1. _**Title:**_, a space, and then the current instance's _**title**_.
  2. _**Author:**_, a space, and then the current instance's _**author**_.
  3. _**Price:**_, a space, and then the current instance's _**price**_. 
  
**Note:** Because these classes are being written in the same file, you must not use an access modifier (e.g.:
_**public**_) when declaring MyBook or your code will not execute.

## Input Format

You are not responsible for reading any input from stdin. The Solution class creates a Book object and calls the MyBook 
class constructor (passing it the necessary arguments). It then calls the display method on the Book object.

## Output Format

The _**void display()**_ method should print and label the respective _**title**_, _**author**_, and _**price**_ of the 
MyBook object's instance (with each value on its own line) like so:
````
Title: $title
Author: $author
Price: $price
````
**Note:** The _**$**_ is prepended to variable names to indicate they are placeholders for variables.

## Sample Input
The following input from stdin is handled by the locked stub code in your editor:
````
The Alchemist
Paulo Coelho
248
````

## Sample Output
The following output is printed by your display() method:
````
Title: The Alchemist
Author: Paulo Coelho
Price: 248
````

[Day fourteen](https://www.hackerrank.com/challenges/30-abstract-classes/problem?isFullScreen=true).
