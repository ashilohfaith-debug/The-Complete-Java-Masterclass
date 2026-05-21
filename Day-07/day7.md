# Day 7: Switch Statements and Enums in Java
21.05.2026

<br/>

## Overview
Today, I learnt Switch Control Statements in Java, which provide a cleaner and more readable alternative to long `if-else-if` ladders when handling multiple conditions based on a single variable.

<br/>

## Topics Covered
1️⃣ Introduction to Switch Statements

A switch statement evaluates an expression and executes the matching case block. <br/>
🔹 Syntax:
```
switch(expression) {

    case value1:
        // code
        break;
        
    case value2:
        // code
        break;
        
    default:
        // code if no cases match
}
```

<br/>

2️⃣ Key Components of Switch Statements

🔹 Expression: the variable or value being evaluated <br/>
🔹 Case: defines possible matching values <br/>
🔹 Break: the keyword which stops execution after a case is matched <br/>
🔹 Default: executes when none of the cases match

<br/>

3️⃣ If Statements vs. Switch Statements

If Statements are used when: <br/>
🔹 Conditions involve ranges or inequalities <br/>
🔹 Complex logical expressions are required <br/>
🔹 Multiple variables are involved

<br/>

Switch Statements are used when: <br/>
🔹 Comparing a single variable <br/>
🔹 Checking against constant values

<br/>

4️⃣ Switch Statements with Enums

🔹 Enums define a fixed set of constants. <br/>
🔹 Example Enum: <br/>
```
enum Day {
    SUNDAY,
    MONDAY,
    TUESDAY,
    WEDNESDAY
}
```
🔹 Using Enum with Switch: <br/>
```
Day today = Day.MONDAY;
switch(today) {

    case SUNDAY:
        System.out.println("Start of the week");
        break;

    case MONDAY:
        System.out.println("Second day");
        break;

    default:
        System.out.println("Another day");
}
```

<br/>

5️⃣ Break Keyword & Fall Through

🔹 The `break` keyword exits the switch block after a match. <br/>
🔹 Fall Through: If break is missing, execution continues into the next case. Example: <br/>

```
int number = 1;
switch(number) {

    case 1:
        System.out.println("One");

    case 2:
        System.out.println("Two");
}
```
**Output:** <br/>
One <br/>
Two

<br/>

## Key Takeaways
💡 Switch statements are useful for: 

🔹 Menu-driven programs <br/>
🔹 Calculator applications <br/>
🔹 Game controls <br/>
🔹 Option selection systems

<br/>

🧠  What I learnt:

🔹 How switch statements work in Java <br/>
🔹 The difference between if and switch statements <br/>
🔹 Enums with switch statements <br/>
🔹 Fall-through behavior

<br/>

🛠️ Technologies used:

🔹 Java <br/>
🔹 IntelliJ IDEA <br/>
🔹 JDK
