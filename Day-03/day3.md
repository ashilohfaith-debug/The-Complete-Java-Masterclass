# Day 03 – Java Basics: Operators, Expressions & Strings
08.05.2026

Date: 8 May 2026
Duration: ~1 Hour
Focus: Understanding Java Operators, Expressions, User Input & Basic String Concepts

🎯 Objective

Understand how Java performs calculations, comparisons, logical operations, and handles user input using operators, expressions, and strings.

✅ What I Completed
1️⃣ Learned About User Input in Java

Understood how Java accepts input from the user using the Scanner class.

Concepts Learned:
Importing the Scanner class
Creating Scanner objects
Reading user input from the keyboard
Syntax Practiced:
import java.util.Scanner;

Scanner sc = new Scanner(System.in);
Examples Learned:
int age = sc.nextInt();
String name = sc.nextLine();
Understood:
Scanner belongs to the java.util package
Scanner allows interactive programs
Different methods are used for different data types
Common Scanner Methods:
nextInt()
nextDouble()
next()
nextLine()
nextBoolean()
2️⃣ Learned About Operators

Understood that operators are special symbols used to perform operations on variables and values.

Understood:
Operators help manipulate data
Operators are essential for calculations and decision-making
Java provides different categories of operators
3️⃣ Learned About Expressions

Studied how expressions combine variables, operators, and values to produce results.

Example:
a + b
salary * bonus
Understood:
Expressions evaluate to a value
Operators work inside expressions
Expressions are the foundation of program logic
4️⃣ Learned Arithmetic Operators

Studied operators used for mathematical calculations.

Operators Covered:
+   Addition
-   Subtraction
*   Multiplication
/   Division
%   Modulus (Remainder)
Examples Practiced:
int sum = a + b;
int product = a * b;
int remainder = a % b;
Understood:
% returns remainder
/ behaves differently for integers and decimals
Arithmetic operators are heavily used in programming logic
5️⃣ Learned Unary Operators

Studied operators that work on a single operand.

Operators Covered:
+a
-a
a++
++a
a--
--a
Examples Learned:
int a = 5;
a++;
++a;
Understood:
Post-increment uses value first, then increases
Pre-increment increases first, then uses value
Unary operators simplify variable updates
6️⃣ Learned Relational Operators

Studied operators used for comparisons.

Operators Covered:
==
!=
>
<
>=
<=
Examples Practiced:
a > b
age >= 18
marks == 100
Understood:
Relational operators return true or false
Frequently used in conditions and loops
Form the basis of decision-making in Java
7️⃣ Learned Logical Operators

Studied logical operations using boolean values.

Operators Covered:
&&   AND
||   OR
!    NOT
Example:
boolean result = (a > 0) && (b < 15);
Understood:
&& requires both conditions to be true
|| requires at least one condition to be true
! reverses boolean values
8️⃣ Learned Short-Circuit Evaluation

Understood how Java avoids unnecessary condition checks.

Example:
(a > 0) && (b < 15)
Understood:
Second condition runs only if needed
Improves efficiency
Prevents unnecessary computations and errors
9️⃣ Learned Assignment Operators

Studied operators used to assign and update variable values.

Operators Covered:
=
+=
-=
*=
/=
%=
Examples Practiced:
a += 5;
a -= 2;
a *= 3;
Understood:
Assignment operators shorten code
Useful for updating values quickly
Commonly used in loops and calculations
🔟 Learned Operator Precedence & Associativity

Studied how Java decides the order of operations.

Understood:
Unary operators have high precedence
Assignment operators have low precedence
Java generally evaluates left to right
Example:
int result = 5 + 3 * 2;
Learned:
Multiplication happens before addition
Parentheses improve readability and control order
1️⃣1️⃣ Learned Common Mistakes in Operators

Studied issues beginners commonly face.

Topics Covered:
Integer division problems
Floating-point precision issues
Incorrect operator precedence
Examples:
5 / 2      // returns 2
5.0 / 2    // returns 2.5
Understood:
Integer division truncates decimals
Floating-point calculations may lose precision
Using parentheses avoids confusion
1️⃣2️⃣ Introduction to Strings

Learned basic understanding of Strings in Java.

Example:
String name = "Faith";
Understood:
Strings store text data
Strings are reference data types
Strings are widely used in user input and output
🧠 Key Concepts Learned
Java operators and expressions
Arithmetic, relational, logical, and unary operators
Assignment operators and shorthand updates
User input using Scanner
Boolean logic and comparisons
Operator precedence and associativity
Integer division and floating-point issues
Basic introduction to Strings
🔄 Mindset Shift

Moved from:

Writing simple values and print statements

To:

Understanding how Java performs calculations, comparisons, logic handling, and user interaction internally

💭 Reflection

Day 3 focused on building logical thinking and computation skills in Java.

Built:

Better understanding of how Java processes operations
Clarity on comparisons and logical conditions
Understanding of user interaction using Scanner
Awareness of common arithmetic and precedence mistakes

This day established the foundation required for:

Conditional statements
Loops
Decision-making logic
Input-driven programs
Problem solving in Java
✅ Status

Day 3 Complete
Streak: 3 / 60
