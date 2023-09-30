childs_meal = float(input('What is the price of a Childs meal? '))
adults_meal = float(input('What is the price of an Adult meal? '))
children = float(input('How many children are eating? '))
adults = float(input('How many adults are eating? '))
tax = float(input('What is the sales tax rate? '))
print('\n')


price = childs_meal * tax
price = price * children
price = adults_meal * tax
price = price * adults
subtotal = childs_meal * children + adults_meal * adults
price = subtotal + tax


print(f'Subtotal: ${subtotal}')
print(f'Sales tax: ${tax}')
print(f'Total: ${price}')
print('\n')


payment_amount = float(input('What is the payment amount? '))
change = payment_amount - price
print(f'Change: ${change}')
