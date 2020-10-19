'''
Write a program which repeatedly reads number
until the user enters 'done'. Once 'done' is entered,
print out the total, count, and average of the numbers.
If the user enters anything other than a number, detect their 
mistake using try and except and print an error mesaage and 
skip to the next number.
'''

# Print Guide
print('--------------------------------------------------')
print('I will calculate sum, count, and average')
print('What you need to do is just insert the number')
print('When youre done, just write done')
print('--------------------------------------------------')

# Iterate
tot = 0.0
cnt = 0
while True:
    sinp = input('Enter a number: ')
    if sinp =='done':
        break
    try:
        finp = float(sinp)
    except:
        print('Invalid Input')
        continue
    tot = tot + finp
    cnt = cnt + 1
print('All Done')
print('Sum: ',tot, ',Count: ', cnt,',Average: ', tot/cnt)
