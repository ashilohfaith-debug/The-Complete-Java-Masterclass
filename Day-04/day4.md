Day 04 – Java Basics Extended: Strings & String Operations

Date: 9 May 2026
Duration: ~1 Hour
Focus: Understanding Strings, String Comparison, Manipulation & Formatting in Java

🎯 Objective

Understand how Java handles text using Strings, including creating, comparing, modifying, and formatting strings for real-world programming.

✅ What I Completed
1️⃣ Learned About Strings in Java

Understood that Strings represent sequences of characters used to store text data.

Concepts Learned:
Strings store textual information
Strings are immutable in Java
String operations are widely used in applications
Example:
String name = "Faith";
Understood:
Strings are reference data types
Once created, String objects cannot be modified directly
Java creates new String objects during modifications
2️⃣ Learned How to Create Strings

Studied different ways to create String objects.

Methods Learned:
Using String literals
Using the new keyword
Examples Practiced:
String name = "Java";

String language = new String("Java");
Understood:
String literals are memory efficient
new String() creates a separate object in memory
Both methods create String objects differently internally
3️⃣ Learned String Concatenation

Studied how multiple strings can be joined together.

Method Learned:
Using the + operator
Examples Practiced:
String firstName = "Faith";
String lastName = "Developer";

String fullName = firstName + " " + lastName;
Understood:
Concatenation combines strings
Java automatically joins text values
Frequently used in outputs and messages
4️⃣ Learned About String Length

Studied how to find the number of characters inside a string.

Method Learned:
length()
Example:
String text = "Java";

System.out.println(text.length());
Understood:
length() returns total characters
Spaces are also counted
Useful for validations and loops
5️⃣ Learned About Character Access

Studied how to access individual characters inside a String.

Method Learned:
charAt()
Example:
String word = "Java";

System.out.println(word.charAt(0));
Understood:
Indexing starts from 0
charAt() returns a single character
Useful for character-based operations
6️⃣ Learned String Comparison Using ==

Understood how == compares memory references instead of actual content.

Example:
String a = "Java";
String b = "Java";

System.out.println(a == b);
Understood:
== checks whether both variables point to the same object
It does NOT compare actual text content reliably
Can lead to confusion for beginners
7️⃣ Learned String Comparison Using equals()

Studied the correct way to compare String content.

Method Learned:
equals()
Example:
String a = "Java";
String b = "Java";

System.out.println(a.equals(b));
Understood:
equals() compares actual text values
Most commonly used for String comparison
Preferred over == for content checking
8️⃣ Learned equalsIgnoreCase()

Studied how to compare strings without considering uppercase or lowercase letters.

Example:
String a = "JAVA";

System.out.println(a.equalsIgnoreCase("java"));
Understood:
Ignores character casing
Useful for user input comparisons
Prevents case-sensitive issues
9️⃣ Learned Lexicographical Comparison Using compareTo()

Studied how Java compares strings alphabetically.

Method Learned:
compareTo()
Example:
"Apple".compareTo("Banana");
Understood:
Compares strings using dictionary order
Returns:
Positive number
Negative number
Zero
Useful for sorting and ordering data
🔟 Learned More String Operations

Studied additional built-in String methods.

🔹 Substring Extraction
Method Learned:
substring()
Example:
String text = "Programming";

System.out.println(text.substring(0, 6));
Understood:
Extracts part of a String
Start index is inclusive
End index is exclusive
🔹 Replacing Characters
Method Learned:
replace()
Example:
String text = "Java";

System.out.println(text.replace('a', 'o'));
Understood:
Creates a modified copy of the String
Original String remains unchanged
🔹 Changing Case
Methods Learned:
toUpperCase()
toLowerCase()
Example:
String name = "Java";

System.out.println(name.toUpperCase());
Understood:
Converts text casing
Useful for normalization and comparisons
1️⃣1️⃣ Learned About String Formatting

Studied how Java formats strings dynamically using placeholders.

Method Learned:
String.format()
Example:
String name = "Faith";

String result = String.format("Hello, %s!", name);
Understood:
%s is used for Strings
Helps create clean and readable output
Useful for reports and formatted messages
1️⃣2️⃣ Learned Number Formatting

Studied how numbers can be formatted inside strings.

Example:
String.format("%.2f", 1234.567);
Understood:
Controls decimal precision
Useful for financial and scientific applications
Makes outputs cleaner and professional
🧠 Key Concepts Learned
Strings and immutability
String creation methods
String concatenation
length() and charAt()
String comparison using:
==
equals()
equalsIgnoreCase()
compareTo()
String manipulation methods
String formatting and placeholders
Number formatting techniques
🔄 Mindset Shift

Moved from:

Treating text as simple output

To:

Understanding how Java internally stores, compares, manipulates, and formats textual data efficiently

💭 Reflection

Day 4 focused on mastering one of the most important concepts in Java — Strings.

Built:

Strong understanding of String operations
Awareness of immutable objects
Clarity on proper String comparison techniques
Understanding of formatting and text manipulation

This day established the foundation required for:

User input handling
Data validation
File handling
Object-Oriented Programming
Backend development
Real-world application building
✅ Status

Day 4 Complete
Streak: 4 / 60
