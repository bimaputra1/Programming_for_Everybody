# Variables and Expression



## Constants 
Fixed values such as numbers, letters, and strings because their value does not change
- Numeric are as expect
- String use single quotes or double quotes

```
#numeric constant
print(123) 

# String Constant
print('Hello World')
```

## Variable
A named placed in memory where we can store data and retrive the data using variable name

```
# x and y are variables
x = 12.2
y = 14
```

- Variable name rules
  - start with a letter or _
  - consist of letters, numbers and underscore
  - case sensitive


## Assignment 
Statements consists of an expression on the right-hand side and a variable to store the result

```
x = 3.9 * x * (1-x)
```

- Operators are special symbols that represent computations like addition and mul
tiplication. The values the operator is applied to are called operands.
- The operators +,-, *, /, **, and % perform addition, subtraction, multiplication,
division, exponentiation, and modular
- Order of Evaluation are considered by Python
  - Parenthesis
  - Power
  - Multiplication, Division, and Remainder
  - Addition and Substraction
  - Left to Right
  - 
## Types
Python understand the type and difference. For example between number and string in expression.
- Types of Numbers
  - *Integers* are whole numbers
  - *Floating* have decimal parts
- We can convert using int() or float()
- We can instruct Python to pause and read data from the users using the input() function which returns a string
```
nam = input('Who are you?')
print('Welcome ', nam)
```

**GOOD VARIABLE NAMES WILL HELP US**

## Comments
- Comments in Python using #
- Why comment?
  - Describe what is going to happen in a sequence of code
  - Document who wrote the code or other ancillary information
  - Turn off a line of code - perhaps temporarily

