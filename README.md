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

### Using a Main Function
Most of the work we have done so far involve code that has a **main()** function. This function is the one we tend to call as a first step. Sometimes, your code will be imported by another python file so automatically calling a main function becomes unnecessary or undesired.

Before the Python interpreter executes your program, it defines a few special variables. One of those variables is called __name__ and it is automatically set to the string value "__main__" when the program is being executed by itself in a standalone fashion. On the other hand, if the program is being imported by another program, then the __name__ variable is set to the name of that module. This means that we can know whether the program is being run by itself or whether it is being used by another program and based on that observation, we may or may not choose to execute some of the code that we have written.

For example, assume that we have written a collection of functions to do some simple math. We can include a main function to invoke these math functions. It is much more likely, however, that these functions will be imported by another program for some other purpose. In that case, we would not want to execute our main function.

```
def squareit(n):
  return n * n

def cubeit(n):
  return n*n*n

def main():
  anum = int(input("Please enter a number"))
  print(squareit(anum))
  print(cubeit(anum))

if __name__ == "__main__":
  main()
```

### Program Development
At this point, you should be able to look at complete functions and tell what they do. Also, if you have been doing the exercises, you have written some small functions. As you write larger functions, you might start to have more difficulty, especially with runtime and semantic errors.

To deal with increasingly complex programs, we are going to suggest a technique called incremental development. The goal of incremental development is to avoid long debugging sessions by adding and testing only a small amount of code at a time.

As an example, suppose you want to find the distance between two points, given by the coordinates (x1, y1) and (x2, y2). By the Pythagorean theorem, the distance is:

![Distance Formula](distance_formula.png)

The first step is to consider what a distance function should look like in Python. In other words, what are the inputs (parameters) and what is the output (return value)?

In this case, the two points are the inputs, which we can represent using four parameters. The return value is the distance, which is a floating-point value.

Already we can write an outline of the function that captures our thinking so far.
```
def distance(x1, y1, x2, y2):
  return 0.0
```
Obviously, this version of the function doesn’t compute distances; it always returns zero. But it is syntactically correct, and it will run, which means that we can test it before we make it more complicated.

For the second test the horizontal distance equals 3 and the vertical distance equals 4; that way, the result is 5 (the hypotenuse of a 3-4-5 triangle). For the third test, we have a 1-1-sqrt(2) triangle.

At this point we have confirmed that the function is syntactically correct, and we can start adding lines of code. After each incremental change, we test the function again. If an error occurs at any point, we know where it must be — in the last line we added.

A logical first step in the computation is to find the differences x2- x1 and y2- y1. We will store those values in temporary variables named dx and dy.

```
def distance(x1, y1, x2, y2):
  dx = x2 - x1
  dy = y2 - y1
  return 0.0
```
Next we compute the sum of squares of dx and dy.
```
def distance(x1, y1, x2, y2):
  dx = x2 - x1
  dy = y2 - y1
  dsquared = dx**2 + dy**2
  return 0.0
```
Finally, we have our working function we can test.
```
def distance(x1, y1, x2, y2):
  dx = x2 - x1
  dy = y2 - y1
  dsquared = dx**2 + dy**2
  result = dsquared**0.5
  return result
```

### Composition
As we have already seen, you can call one function from within another. This ability to build functions by using other functions is called composition.

As an example, we’ll write a function that takes two points, the center of the circle and a point on the perimeter, and computes the area of the circle.

Assume that the center point is stored in the variables xc and yc, and the perimeter point is in xp and yp. The first step is to find the radius of the circle, which is the distance between the two points. Fortunately, we’ve just written a function, distance, that does just that, so now all we have to do is use it:
```
radius = distance(xc, yc, xp, yp)
```
The second step is to find the area of a circle with that radius and return it. Again we will use one of our earlier functions:
```
result = area(radius)
return result
```
Wrapping that up in a function, we get:
```
def distance(x1, y1, x2, y2):
  dx = x2 - x1
  dy = y2 - y1
  dsquared = dx**2 + dy**2
  result = dsquared**0.5
  return result

def area(radius):
  b = 3.14159 * radius**2
  return b

def area2(xc, yc, xp, yp):
  radius = distance(xc, yc, xp, yp)
  result = area(radius)
  return result

print(area2(0,0,1,1))
```
We called this function area2 to distinguish it from the area function defined earlier. There can only be one function with a given name within a module.

Note that we could have written the composition without storing the intermediate results.
```
def area2(xc, yc, xp, yp):
  return area(distance(xc, yc, xp, yp))
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
