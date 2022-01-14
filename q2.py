#question 2
#all values are in dollars

gross_inc = float(input("Please enter gross income: "))

std_deduc = 10000
dependents = int(input("Enter the no. of dependents: "))

dep_deduc = 3000
tax_inc = gross_inc - std_deduc - (dep_deduc * dependents)
print("taxable income:")
print(tax_inc)
tax = (tax_inc * 20) / 100
print("tax:")
print(tax)