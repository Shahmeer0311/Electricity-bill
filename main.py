a = int(input("How many units consumed"))
if (a < 50 ):
    amount = a * 2.6 
    tax = 25
elif (a <= 100 ):
    amount = a * 3.25
    tax = 35
elif (a <= 200):
    amount = a * 5.26
    tax = 45
else:
    amount = a * 8.35
    tax = 75
amount = amount + tax
print("Your total is",amount)