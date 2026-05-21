# Day 02 – Variables and Data Types in Java
07.05.2026

<br/>

## Overview
Today, I learnt about Variables, Data Types, and Type Casting in Java, which are the basic building blocks used to store and manipulate data in Java programs.

<br/>

## Topics Covered
1️⃣ Introduction to Variables

A variable is a container used to store data values in Java. Every variable must be declared with a data type. <br/>
🔹 Example:
```
int myNumber;
```

<br/>

2️⃣ Declaring and Initializing Variables

🔹 Declaring Variables:
```
int age;
```
🔹 Initializing Variables:
```
int age = 18;
```
🔹 Reassigning Values:
```
age = 20;
```

<br/>

3️⃣ Variable Naming Rules

🔹 Must start with a letter, $, or _ <br/>
🔹 Cannot contain spaces <br/>
🔹 Cannot use Java keywords <br/>
🔹 Variable names are case-sensitive <br/>
🔹 Use short, descriptive names <br/>
🔹 Follow camelCase convention

<br/>

Example:
```
int studentAge = 17;
```

<br/>

4️⃣ Introduction to Data Types

Data types define the type of data a variable can store and the operations that can be performed on it.

<br/>

5️⃣ Primitive Data Types

```
byte age = 30;
short year = 2024;
int salary = 50000;
long population = 7800000000L;

float temperature = 36.6f;
double pi = 3.141592653589793;

char initial = 'A';
boolean isJavaFun = true;
```

<br/>

6️⃣ Reference Data Types

Reference data types store references to objects. Classes, Arrays, Interfaces and Strings are reference datat types. <br/>

🔹 Example:
```
String message = "Hello";
```

<br/>

7️⃣ Type Casting

Type casting converts one data type into another. <br/>
🔹 Widening Conversion (Implicit Casting): automatically converts smaller data types into larger ones

Example:
```
int number = 10;
double value = number;
```

<br/>

🔹 Narrowing Conversion (Explicit Casting): converts larger data types into smaller ones manually; may result in data loss

Example:
```
double number = 9.78;
int result = (int) number;
```

<br/>

## Key Takeaways
💡 Variables and data types are useful for:

🔹 Storing information <br/>
🔹 Performing calculations <br/>
🔹 Managing program data

<br/>

🧠 What I learnt:

🔹 What variables are in Java <br/>
🔹 How to declare and initialize variables <br/>
🔹 Variable naming conventions <br/>
🔹 Primitive and reference data types <br/>
🔹 Type casting in Java
