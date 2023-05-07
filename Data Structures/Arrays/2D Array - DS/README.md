
## Problem
Given a **_6 X 6_** 2D Array, **_arr_**:


```
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
```

An hourglass in **_A_** is a subset of values with indices falling in this pattern in **_arr_**'s graphical representation:

```
a b c
  d
e f g
```

There are **16** hourglasses in **_arr_**. An hourglass sum is the sum of an hourglass' values. Calculate the hourglass sum for every hourglass in **_arr_**, then print the maximum hourglass sum. The array will always be **_6 X 6_**.

**Example**

**_arr=_**

```
-9 -9 -9  1 1 1 
 0 -9  0  4 3 2
-9 -9 -9  1 2 3
 0  0  8  6 6 0
 0  0  0 -2 0 0
 0  0  1  2 4 0
```

The **16** hourglass sums are:

```
-63, -34, -9, 12, 
-10,   0, 28, 23, 
-27, -11, -2, 10, 
  9,  17, 25, 18
```

The highest hourglass sum is **28** from the hourglass beginning at row **1**, column **2**:

```
0 4 3
  1
8 6 6
```


**Function Description**

Complete the function hourglassSum in the editor below.

hourglassSum has the following parameter(s):

- int arr[6][6]: an array of integers


**Returns**

- int: the maximum hourglass sum


**Input Format**

Each of the **6** lines of inputs **_arr[i]_** contains **6** space-separated integers **_arr[i][j]_**.

**Constraints**

- **-9 <= arr[i][j] <= 9**
- **0 <= i,j <= 5**


**Output Format**

Print the largest (maximum) hourglass sum found in **_arr_**.

 
**Sample Input**

```
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0
```

**Sample Output**
```
19
```

## How I solved
Using list comprehension on a range of 0 to 4 in the 2D list, it traverses both directions (row and column) to iterate over all possible hourglasses and sends to the calculate_hourglass method as row and column parameter values.

for each iteration, the method calculate hourglasses is responsible for calculating the value of each hourglass and returning its value that will be saved in a list.

Finally, the maximum hourglass value is responded to using Python's max() function on the list values.
