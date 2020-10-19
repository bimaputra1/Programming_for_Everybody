# Loops and Iteration

The basic idea is sometimes we need to go back and run code again and again.

## Indefinite Loop
Repeat until the condition doesn't meet

```py
n = 5
while n>0:
    print(n)
    n = n-1
print('Blastoff!')
print (n)
```
Output:
5
4
3
2
1
Blastoff!
0

There are two another while loop:
- Infinite Loop : Where the condition always true
- Zero trip loop: Where the condition always false 

### Break
To end the loop we can use *break* statement. This ends the current loop and jumps to the statement after loop.

### Continue
The *continue* statement end the current iteration and jumps to tht top of the loop and starts the next iteration.

```py
while True:
    line = raw_input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')
```

## Definite Loop
We can use *for* statements for definite loop. In this loop, we have explicit iteration variables that change each time through a loop. These iteration variables move through the sequence or set.

```py
for i in [5,4,3,2,1]:
    print(i)
print('Blastoff')
```
Output:
5
4
3
2
1
Blastoff

In for loops
- The iteration variable 'iterates' through the sequence (ordered set)
- The block(body) of code is executed once fir each value in sequence
- The iteration variable moves through all of the values in sequence

## Using Loops 
We are gonna implement loops to find someting after the iteration.

We are gonna find the highest number.

```py
largest = -1
print('Before', largest)

for the_num in [9,41,12,3,74,15]:
    if the_num > largest:
        largest = the_num
    print(largest, the num)

print('After',largest)
```
Output:
Before -1
9 9
41 41
41 12
41 3
74 74
74 15
After 74

## Loop Idiom

### Counting in a Loop
To count how many times we excecute a loop, we use counter variable that starts at 0 and add one to it each time through the loop.

### Summing in a Loop
To add up a value we encounter in a loop, we use a sum variable that starts at 0 and we add the value to the sum each time through the loop.

### Finding the Average in a Loop
Just combining Counting and Sum patterns and divides when the loop is done

### Filtering in a Loop
We use an if statement in the loop to catch/filter the values we are looking for


### Search Using a Boolean Variables
If we just want to search and know if a value was found, we use a variable that starts at False and is set to True as soon as we find what we are looking for.

