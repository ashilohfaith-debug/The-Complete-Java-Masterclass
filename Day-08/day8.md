# Day 8: Loops - For, While and Do-while Loop
22.05.2026

<br/>

# Overview
Today, I learnt about Loops in Java, which are used to repeatedly execute a block of code as long as a condition is true.

<br/>

# Topics Covered
1️⃣ Introduction to Loops

A loop repeatedly executes a block of code while a condition is satisfied. The purpose of loops are as follows: <br/>
🔹 Perform repetitive tasks efficiently <br/>
🔹 Reduce code redundancy <br/>
🔹 Simplify complex problems <br/>
🔹 Improve readability and maintainability <br/>

<br/>

2️⃣ Types of Loops in Java

🔹 for loop <br/>
🔹 while loop <br/>
🔹 do-while loop

<br/>

3️⃣ The For Loop

The for loop is used when the number of iterations is known.
🔹 Syntax:
```
for(initialization; condition; iteration) {

    // Code to be executed
}
```

<br/>

🔹 Syntax Breakdown: <br/>
Initialization → runs once at the start <br/>
Condition → checked before every iteration <br/>
Iteration → executes after every loop cycle

<br/>

4️⃣ The While Loop

The while loop executes code repeatedly as long as the condition remains true. The while loop is useful when the number of iterations is unknown. <br/>
🔹 Syntax:
```
while(condition) {

    // Code to be executed
}
```

<br/>

5️⃣ The Do-While Loop

The do-while loop executes the code block at least once before checking the condition. <br/>
🔹 Syntax:
```
do {

    // Code to be executed

} while(condition);
```

<br/>

6️⃣ Difference Between for, while, and do-while Loops

🔹 for loop:

- Best when iteration count is known <br/>
- Initialization, condition, and update are written together

🔹 while loop:

- Checks condition before execution <br/>
- Best for unknown iteration counts

🔹 do-while loop:

- Executes at least once <br/>
- Checks condition after execution

<br/>

7️⃣ Controlling Loops

🔹 Break Statement: The break statement immediately terminates the loop. <br/>
🔹 Continue Statement: The continue statement skips the current iteration and moves to the next iteration.

<br/>

8️⃣ Labels in Loops

Labels are used to control nested loops more effectively. <br/>
🔹 Syntax:
```
labelName:
for(initialization; condition; update) {

    // Statements
}
```
🔹 Labeled break: Exits a specific loop
🔹 Labeled continue: Skips to the next iteration of a specific loop

<br/>

9️⃣ Infinite Loops

An infinite loop runs continuously because its condition never becomes false. This occurs when the condition always remains true or when there is no proper exit condition.

<br/>

## Key Takeaways
💡 Loops are useful for:

🔹 Repetitive tasks <br/>
🔹 Iterating through data

<br/>

🧠 What I learnt:

🔹 Different types of loops in Java <br/>
🔹 Syntax of for, while, and do-while loops <br/>
🔹 Difference between loop types <br/>
🔹 Usage of break and continue and labels <br/>
🔹 Infinite loops and common mistakes
