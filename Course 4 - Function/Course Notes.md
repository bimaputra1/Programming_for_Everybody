# Function

We don't like to repeat writing the same code so (D-R-Y) Don't Repeat Yourself
Function are something we store and use it. 
Function not executed unless it called. 

```py
def thing():
    print('Hello')
    print('World')

thing()
print('Zip')
thing()
```

It takes some input (arguments) and return output.
Python have some built in function that ready to use.

## Building our own function
The function build using **def** keyword followed by optional parameters in parentheses.
It just define but not execute the code.

Parameters are variables which we use in the function definition. It is a 'handle' that allows the code in the function to access the arguments for a particular function invocation

Sometimes a function will return values after computes the input. This return end the function excecution and sends back the return values as a result of the function.

```py
# declare function with parameters
def addboth(a,b):
    added = a+b
    return added

#call function
x = addtwo(3,5)
print(x)
```
