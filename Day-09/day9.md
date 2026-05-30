# Day 09 – Arrays and ArrayList in Java
24.05.2026

<br/>

## Overview
Today, I learnt about Arrays, 2D Arrays, the Arrays class, and ArrayList in Java. These concepts are used to store and manage collections of data efficiently in Java programs.

<br/>

## Topics Covered
1️⃣ Introduction to Arrays

An array in Java stores multiple values of the same data type. Array elements are accessed using indexes starting from 0. <br/>
🔹 Example:
```
int[] numbers;
```

<br/>

2️⃣ Declaring and Initializing Arrays

🔹 Declaring Arrays:

int[] numbers;

🔹 Initializing Arrays:

numbers = new int[5];

🔹 Initializing with Values:

int[] numbers = {1, 2, 3, 4, 5};
<br/>

3️⃣ Accessing Array Elements

Array elements are accessed using indexes.

🔹 Example:

int first = numbers[0];
numbers[1] = 10;
<br/>

4️⃣ Looping Through Arrays

🔹 Using a For Loop:

for(int i = 0; i < numbers.length; i++) {
    System.out.println(numbers[i]);
}

🔹 Using a For-each Loop:

for(int num : numbers) {
    System.out.println(num);
}
<br/>

5️⃣ Common Array Operations

🔹 Finding Length:

numbers.length
<br/>

6️⃣ The Arrays Class

The Arrays class from java.util provides useful methods for array manipulation.

🔹 Import Statement:

import java.util.Arrays;
<br/>

7️⃣ Common Methods in Arrays Class

🔹 Arrays.toString()

Arrays.toString(numbers);

🔹 Arrays.sort()

Arrays.sort(numbers);

🔹 Arrays.binarySearch()

Arrays.binarySearch(numbers, 5);

🔹 Arrays.copyOf()

Arrays.copyOf(numbers, 10);

🔹 Arrays.fill()

Arrays.fill(numbers, 0);

🔹 Arrays.equals()

Arrays.equals(arr1, arr2);
<br/>

8️⃣ Introduction to 2D Arrays

2D arrays are arrays of arrays arranged in rows and columns.

🔹 Example:

int[][] matrix = new int[3][3];
<br/>

9️⃣ Initializing 2D Arrays

int[][] matrix = {
    {1, 2, 3},
    {4, 5, 6},
    {7, 8, 9}
};
<br/>

🔟 Iterating Through 2D Arrays

🔹 Using Nested Loops:

for(int i = 0; i < matrix.length; i++) {
    for(int j = 0; j < matrix[i].length; j++) {
        System.out.println(matrix[i][j]);
    }
}

🔹 Using Enhanced For Loop:

for(int[] row : matrix) {
    for(int element : row) {
        System.out.println(element);
    }
}
<br/>

1️⃣1️⃣ Introduction to ArrayList

ArrayList is a dynamic and resizable array provided by Java.

🔹 Import Statement:

import java.util.ArrayList;

🔹 Creating an ArrayList:

ArrayList<String> fruits = new ArrayList<String>();
<br/>

1️⃣2️⃣ Common ArrayList Operations

🔹 Adding Elements:

fruits.add("Apple");
fruits.add("Banana");

🔹 Accessing Elements:

String fruit = fruits.get(0);

🔹 Modifying Elements:

fruits.set(1, "Orange");

🔹 Removing Elements:

fruits.remove(0);

🔹 Finding Size:

fruits.size();

🔹 Checking Elements:

fruits.contains("Apple");

🔹 Clearing the ArrayList:

fruits.clear();
<br/>

1️⃣3️⃣ Difference Between Arrays and ArrayList

🔹 Arrays have fixed size <br/>
🔹 ArrayList can grow and shrink dynamically <br/>
🔹 Arrays are faster and memory efficient <br/>
🔹 ArrayList provides many built-in methods <br/>
🔹 Arrays directly support multi-dimensional arrays <br/>
🔹 ArrayList is better for frequent modifications

<br/>
Key Takeaways

💡 Arrays and ArrayLists are useful for:

🔹 Storing multiple values <br/>
🔹 Organizing data efficiently <br/>
🔹 Processing collections using loops <br/>
🔹 Managing dynamic data

<br/>

🧠 What I learnt:

🔹 How arrays work in Java <br/>
🔹 Declaring and initializing arrays <br/>
🔹 Looping through arrays <br/>
🔹 Using the Arrays class methods <br/>
🔹 Working with 2D arrays <br/>
🔹 Creating and managing ArrayLists <br/>
🔹 Difference between Arrays and ArrayList
