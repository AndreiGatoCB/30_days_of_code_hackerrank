# DAY 20
## Objective
Today, we're discussing a simple sorting algorithm called Bubble Sort. Check out the 
[Tutorial](https://www.hackerrank.com/challenges/30-sorting/tutorial) tab for learning materials and an instructional 
video!

Consider the following version of Bubble Sort:
````
for (int i = 0; i < n; i++) {
    // Track number of elements swapped during a single array traversal
    int numberOfSwaps = 0;
    
    for (int j = 0; j < n - 1; j++) {
        // Swap adjacent elements if they are in decreasing order
        if (a[j] > a[j + 1]) {
            swap(a[j], a[j + 1]);
            numberOfSwaps++;
        }
    }
    
    // If no elements were swapped during a traversal, array is sorted
    if (numberOfSwaps == 0) {
        break;
    }
}
````
## Task
Given an array, _**a**_, of size _**n**_ distinct elements, sort the array in ascending order using the Bubble Sort 
algorithm above. Once sorted, print the following _**3**_ lines:

1. ``Array is sorted in numSwaps swaps.``
where _**numSwaps**_ is the number of swaps that took place.
2. ``First Element: firstElement``
where _**firstElement**_ is the first element in the sorted array.
3. ``Last Element: lastElement``
where _**lasElement**_ is the last element in the sorted array.

**Hint:** To complete this challenge, you will need to add a variable that keeps a running tally of all swaps that occur
during execution.

## Example
_**a = [4, 3, 1, 2]**_

````
original a: 4 3 1 2
round 1  a: 3 1 2 4 swaps this round: 3
round 2  a: 1 2 3 4 swaps this round: 2
round 3  a: 1 2 3 4 swaps this round: 0
````
In the first round, the _**4**_ is swapped at each of the _**3**_ comparisons, ending in the last position. In the
second round, the _**3**_ is swapped at _**2**_ of the _**3**_ comparisons. Finally, in the third round, no swaps are
made so the iterations stop.

The output is the following:
````
Array is sorted in 5 swaps.
First Element: 1
Last Element: 4
````

## Input Format

The first line contains an integer, _**n**_, the number of elements in array _**a**_.

The second line contains _**n**_ space-separated integers that describe _**a[0], a[1], ..., a[n-1]**_.

## Constraints
- _**2 <= n <= 600**_
- _**1 <= a[i] <= 2 x 10^6**_, where _**0 <= i < n**_.

## Output Format

Print the following three lines of output:

1. ``Array is sorted in numSwaps swaps.``
where _**numSwaps**_ is the number of swaps that took place.
2. ``First Element: firstElement``
where _**firstElement**_ is the first element in the sorted array.
3. ``Last Element: lastElement``
where _**lasElement**_ is the last element in the sorted array.

## Sample Input 0
````
3
1 2 3
````

## Sample Output 0
````
Array is sorted in 0 swaps.
First Element: 1
Last Element: 3
````

## Explanation 0

The array is already sorted, so _**0**_ swaps take place and we print the necessary _**3**_ lines of output shown above.

## Sample Input 1
````
3
3 2 1
````

## Sample Output 1
````
Array is sorted in 3 swaps.
First Element: 1
Last Element: 3
````

## Explanation 1

The array _**a = [3, 2, 1]**_ is not sorted, so we perform the following _**3**_ swaps. Each line shows _**a**_ after
each single element is swapped.

1. **[3, 2, 1] -> [2, 3, 1]**
2. **[2, 3, 1] -> [2, 1, 3]**
3. **[2, 1, 3] -> [1, 2, 3]**

After _**3**_ swaps, the array is sorted.

[Day twentyone](https://www.hackerrank.com/challenges/30-sorting/problem?isFullScreen=true).
