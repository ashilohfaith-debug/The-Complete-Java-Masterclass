📘 Day 6 — Control Statements & Conditional Operators in Java
📖 Overview

Today I learned about Control Statements in Java, which allow a program to make decisions and execute different blocks of code based on conditions.

Conditional statements are important because they help control the flow of a program and make applications interactive and logical.

🚀 Topics Covered
1️⃣ If Statement

The if statement executes a block of code only when a condition is true.

🔹 Syntax
if(condition) {
    // code executes if condition is true
}
🔹 Example
int age = 18;

if(age >= 18) {
    System.out.println("Eligible to vote");
}
🔹 What I Learned
Used for decision-making.
Executes code only when the condition evaluates to true.
2️⃣ If-Else Statement

The if-else statement provides two possible execution paths.

🔹 Syntax
if(condition) {
    // code if true
} else {
    // code if false
}
🔹 Example
int number = 7;

if(number % 2 == 0) {
    System.out.println("Even Number");
} else {
    System.out.println("Odd Number");
}
🔹 What I Learned
Helps programs choose between two outcomes.
Useful for validation and logical checks.
3️⃣ Nested If-Else Statements

Nested conditions allow checking multiple levels of conditions.

🔹 Example
int age = 20;
boolean hasID = true;

if(age >= 18) {
    if(hasID) {
        System.out.println("Entry Allowed");
    }
} else {
    System.out.println("Entry Denied");
}
🔹 What I Learned
One if statement can exist inside another.
Useful for complex decision-making.
4️⃣ If-Else-If Ladder

Used when checking multiple conditions sequentially.

🔹 Syntax
if(condition1) {
    // code
}
else if(condition2) {
    // code
}
else {
    // code
}
🔹 Example
int marks = 85;

if(marks >= 90) {
    System.out.println("Grade A");
}
else if(marks >= 75) {
    System.out.println("Grade B");
}
else {
    System.out.println("Grade C");
}
🔹 What I Learned
Checks conditions one by one.
Executes only the first true condition.
5️⃣ Ternary Operator

The ternary operator is a shorthand version of a simple if-else statement.

🔹 Syntax
condition ? expression1 : expression2;
🔹 Example
int number = 10;

String result = (number % 2 == 0) ? "Even" : "Odd";

System.out.println(result);
🔹 What I Learned
Makes code shorter and cleaner.
Best used for simple conditions.
💡 Importance of Conditional Statements

Conditional statements are used in:

User input validation
Decision-making systems
Login authentication
Menu-driven applications
Game logic
Control flow management
🧠 Key Takeaways

✅ Learned how Java makes decisions using conditions
✅ Understood if, if-else, and nested conditions
✅ Learned how to handle multiple conditions using if-else-if
✅ Explored the ternary operator for concise code
✅ Improved logical thinking and programming flow understanding

📂 Concepts Practiced
Boolean conditions
Comparison operators
Logical flow
Code execution control
Decision-making structures
🛠️ Technologies Used
Java
VS Code / IntelliJ IDEA
JDK
📌 Conclusion

Today’s session helped me understand how programs make decisions using conditional statements in Java. These concepts form the foundation of problem-solving and logical programming and are essential for building real-world applications.

✨ Learning Java one concept at a time.
