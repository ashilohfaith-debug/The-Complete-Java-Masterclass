# Day 04: String Manipulation and Comparison
09.05.2026

<br/>

## Overview
Today, I learnt about Strings in Java, including string creation, comparison, manipulation, and formatting techniques.

<br/>

## Topics Covered
1️⃣ Introduction to Strings

🔹 Strings represent sequences of characters in Java. <br/>
🔹 Strings in Java are immutable, meaning their values cannot be changed after creation.

<br/>

2️⃣ Creating Strings

Strings can be created by two ways: <br/>
🔹 String literals
```
String name = "Java";
```
🔹 By using `new` keyword
```
String language = new String("Java");
```

<br/>

3️⃣ String Concatenation

Concatenation joins multiple strings together using the `+` operator.

<br/>

4️⃣ String Length

The `length()` method returns the number of characters in a string. <br/>
🔹 Example:
```
String text = "Hello";
System.out.println(text.length());
```

<br/>

5️⃣ Accessing Characters

The `charAt()` method returns the character at a specific index. <br/>
🔹 Example:
```
String word = "Java";
System.out.println(word.charAt(1));
```

<br/>

6️⃣ Comparing Strings

🔹 Using `==` which checks whether two references point to the same object <br/>
🔹 Using `equals()` which compares the actual content of strings <br/>
🔹 Using `equalsIgnoreCase()` which compares strings without considering case sensitivity <br/>
🔹 Using `compareTo()` which compares strings lexicographically (dictionary order)

<br/>

7️⃣ More String Methods

🔹 `substring()`: extracts part of a string <br/>
🔹 `replace()`: replaces characters in a string <br/>
🔹 `toUpperCase()`: converts string to uppercase <br/>
🔹 `toLowerCase()`: converts string to lowercase

<br/>

8️⃣ String Formatting

String formatting creates strings with embedded variables and formatted values. This can be done by using `String.format()`: <br/>
```
String.format("Hello, %s!", name);
```

<br/>

9️⃣ Formatting Numbers

Numbers can be formatted to control decimal places. Example: <br/>
```
String.format("%.2f", 1234.567);
```

**Output:** <br/>
1234.57

<br/>

## Key Takeaways

💡 Strings are useful for:

🔹 Storing text data <br/>
🔹 User interaction <br/>
🔹 Data formatting <br/>
🔹 Text manipulation

<br/>

🧠 What I learnt:

🔹 String creation in Java <br/>
🔹 Operations on Strings <br/>
🔹 String formatting techniques
