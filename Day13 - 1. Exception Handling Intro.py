'''
An exception in programming refers to an anomalous condition or error that occurs during the execution of a program.
When an exceptional situation arises that disrupts the normal flow of a program, Python raises an exception.
This could be due to various reasons such as invalid input, division by zero, attempting to access a file that does not exist,
or a programming error like attempting to call a method on an object that does not support it.

Exceptions are Python's way of handling runtime errors and abnormal conditions. When an exception occurs,
it typically interrupts the normal flow of the program and transfers control to the nearest exception handler.

Python provides a mechanism to handle exceptions using the try, except, else, and finally blocks.
By catching and handling exceptions, you can gracefully manage errors and prevent your program from crashing.


What is Error?

In programming, an error refers to any deviation from the intended or expected behavior of a program.
Errors can occur for various reasons, including syntactical mistakes in the code, logical flaws, runtime issues,
or external factors such as hardware failures or network disruptions.

Errors in programming can be broadly categorized into three main types:

1. **Syntax Errors**: Syntax errors occur when the code violates the rules of the programming language.
These errors are typically detected by the compiler or interpreter during the parsing phase.
Examples include missing parentheses, incorrect indentation, or using undefined variables.

   ```python
   # Syntax error: missing closing parenthesis
   print("Hello, world"
   ```

2. **Runtime Errors**: Runtime errors occur while the program is executing.
These errors are not detected by the compiler or interpreter during the compilation
or parsing phase but are instead encountered during program execution. Examples include division by zero,
accessing an index out of bounds in a list, or attempting to perform operations on incompatible data types.

   ```python
   # Runtime error: division by zero
   result = 10 / 0
   ```

3. **Semantic Errors**: Semantic errors occur when the program runs without throwing any exceptions,
but the output is incorrect due to logical flaws in the code. These errors are often the most challenging
to identify and debug because they do not result in immediate failure. Examples include using the wrong algorithm
to solve a problem or misunderstanding the requirements.

   ```python
   # Semantic error: incorrect algorithm
   # Calculate the average of two numbers
   a = 10
   b = 20
   average = a + b / 2  # Incorrect: should be (a + b) / 2
   ```

Handling errors and debugging code effectively is an essential skill for programmers. Techniques such as testing,
code reviews, and using debugging tools can help identify and fix errors in software development.
'''
