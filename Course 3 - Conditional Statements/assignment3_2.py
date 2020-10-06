"""
3.2 Use code on previous section
Then use try except to handle errors. 
"""

hrs = input("Enter Hours:")
rate = input("Enter Rates:")
try:
    rt = float(rate)
    h = float(hrs)
except:
    print('Error, please insert a numbers')
    quit()

print(rt,h)
if h>40.0:
    reg=h*rt
    ot=(h-40.0)*(rt*0.5) #Additional payment
    pay = reg+ot
else:
    pay=h*rt
print(pay)
