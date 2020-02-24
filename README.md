# Lecture 7 - CYBR 2980
## Objectives
- Design with functions:
  - hiding redundancy, complexity
  - arguments and return values
  - formal vs actual arguments, named arguments.
- Program structure and design.

### Functions
In Python, a function is a named sequence of statements that belong together. Their primary purpose is to help us organize programs into chunks that match how we think about the solution to the problem.

The syntax for a function definition is:
```
def name( parameters ):
    statements
```
The **parameters** we give to a function are values that are passed into the function when it is called. For example, when we had a turtle, we made a funciton called *drawSquare()* that took two parameters, a turtle and a size.
```
def drawSquare(myTurtle, size):
  myTurtle.penDown()

  for i in range(4):
    myTurtle.forward(size)
    myTurtle.right(90)

  myTurtle.penUp()
```
In this case, a turtle and a number are passed to the function as parameters. These values can now be used by the function.

**Note:** any changes made to a parameter passed to a function, will not change the original value that called it.


### docstirngs
If the first thing after the function header is a string (some tools insist that it must be a triple-quoted string), it is called a docstring and gets special treatment in Python and in some of the programming tools.

Another way to retrieve this information is to use the interactive interpreter, and enter the expression <function_name>.__doc__, which will retrieve the **docstring** for the function. So the string you write as documentation at the start of a function is retrievable by python tools at runtime. This is different from comments in your code, which are completely eliminated when the program is parsed.

By convention, Python programmers use **docstrings** for the key documentation of their functions.

```
def checkPrime(num):
  """Check to see if the given number is prime. Returns True or False"""
  statements
```

### Return Values
A function can send a value back to the code that called it. We have been using this type of function in python for a while.

Example:
```
>>> abs(10)
>>> abs(-15)

>>> import math
>>> math.pow(2, 5)
```

When you are defining your own functions, the **return** statement will be the last thing that happens in your function. As soon as a return statement is reached, the function ends and any lines that happen after the return statement will not be executed.

```
def hasValue(myList, value):
  for e in myList:
    if e == value:
      return True

  return False


nums = [5, 10, 15, 20]
print( hasValue(nums, 8) )
```

### Problem deconstruction (abstraction)
One of the big ideas in computer science is taking a large problem and breaking it down into smaller, more manageable parts.
For example, imagine that we have the problem of finding the sum of many squares. We can begin by breaking this down into the smallest possible problem.
```
def square(x):
  y = x * x
  return y
```
Then, we can use this small solution as part of the larger solution.
```
def sumOfSquares(start, end):
  total = 0
  for num in range(start, end + 1):
    total = total + square(num)

  return total
```
Then finally, we could call this in the context of our program. Perhaps after we have some data or user input.
```
def main():
  tot = sumOfSquares(4, 7)
  print(tot)

main()
```



### Quiz

1. What is a function in Python?
  - A named sequence of statements.
  - Any sequence of statements.
  - A mathematical expression that calculates a value.
  - A statement of the form x = 5 + 4.  


2. What is one main purpose of a function?
  - To improve the speed of execution
  - To help the programmer organize programs into chunks that match how they think about the solution to the problem.
  - All Python programs must be written using functions
  - To calculate values.


3. Which of the following is a valid function header (first line of a function definition)?
  - def drawCircle(t):
  - def drawCircle:
  - drawCircle(t, sz):
  - def drawCircle(t, sz)


4. What is wrong with the following function definition:
```
def addEm(x, y, z):
    return x + y + z
    print('the answer is', x + y + z)
```
  - You should never use a print statement in a function definition.
  - You should not have any statements in a function after the return statement. Once the function gets to the return statement it will immediately stop executing the function.
  - You must calculate the value of x+y+z before you return it.
  - A function cannot return a number.


5. What will the following function return?
```
def addEm(x, y, z):
    print(x + y + z)
```
  - None
  - The value of x + y + z
  - The string 'x + y + z'


6. Consider the following Python code. Note that line numbers are included on the left.

  ```
  def pow(b, p):
      y = b ** p
      return y

  def square(x):
      a = pow(x, 2)
      return a

  n = 5
  result = square(n)
  print(result)
  ```
  What does this function print?
    - 25
    - 5
    - 125
    - 32
