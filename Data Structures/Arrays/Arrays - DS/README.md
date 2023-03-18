
## Problem
An array is a type of data structure that stores elements of the same type in a contiguous block of memory. In an array, **_A_**, of size **_N_**, each memory location has some unique index, **_i_** (where **_0_**<=**_i_**<**_N_**), that can be referenced as **_A[i]_** or **_A<sub>i</sub>_**.

Reverse an array of integers.

**Example**
```
A = [1, 2, 3]
Return [3, 2, 1]
```


**Function Description**

Complete the function reverseArray in the editor below.

reverseArray has the following parameter(s):

- int A[n]: the array to reverse
**Returns**

- int[n]: the reversed array


**Input Format**

The first line contains an integer, **_N_**, the number of integers in **_A_**.
The second line contains **_N_** space-separated integers that make up **_A_**.

**Constraints**

- **1 <= _N_ <= 10<sup>3</sup>**
- **1 <= _A[_i_]_ <= 10<sup>4</sup>, where A[_i_] is the i<sup>_th_</sup> integer in **A****

 
**Sample Input 1**

| 1   | 4   | 3   | 2   |
|-----|-----|-----|-----|
Array: arr
```
4
1 4 3 2
```


**Sample Output 1**
```
2 3 4 1
```

## How I solve
I use the reversed Build-in function, This function takes an iterator as a parameter and return a reverse iterator.