# Conditional Statement
Using if statement to do some conditional which return True or False.

## Comparison Operators
Used to make the condition. Look to the variable without changes it and return True or False
For examples
- < : Less than
- <= : Less than or Equal to
- == : Equal to
- \>= : Greater than or Equal to
- \>: Greater than
- != : Not Equal

## Indenting in Python
Its important to do indentation in Python because Python cares about spaces

## Decision Types
### One way decision
When we only provide a condition
```py
x = 5
if x=5:
    print('this is 5')
print('Done')
```
### Two way decision
When we want to do something where condition is true and something else when the conditio is failed

We can use else statement here:
```py
x = 5
if x=5:
    print('this is 5')
else:
    print('this is not 5')
print('Done')
```

### Multiway decision
We can use elif to make more complex code
```py
x = 5
if x<2:
    print('Small')
elif x<6:
    print('Medium')
else:
    print('Huge')
print('Done')
```

## Try and Excep Statement
We use it if we know the code might failed. So it don't blow up/traceback.
We use the code inside try and except. The scenario will be:
- Use try and if succeded skip except
- Use try and if failed try except
```py
raw = input('Enter a number:')
try:
    ival = int(raw)
except:
    ival = -1

if ival>0:
    print('Nice Work')
else:
    print('Not a number')
```
Tips: Don't put too much code, just put the essential 