'''
Write a program that repeatedly prompts a user
for integer numbers until the user enters 'done'.
Once 'done' is entered, print out the largest and
smallest numbers. If the user enters anything other
than a valid number put an error messages.
'''

largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : 
        break

    # Catching error
    try:
        num = int(num)
    except:
        print('Invalid input')
        continue

    # find largest
    if largest is None:
        largest = num
    elif num > largest:
        largest = num
    
    # find smallest
    if smallest is None:
        smallest = num
    elif num < smallest:
        smallest = num

print("Maximum is", largest)
print("Minimum is", smallest)