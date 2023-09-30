#input for information
first = input("What is your First name? ").lower()
last = input("What is your Last name? ").lower()
email = input("What is your Email Address? ").lower()
phone = input("What is your Phone Number? ").lower()
jobtitle = input("What is your Job Title? ").lower()
idnumber = input("What is you ID Number? ").lower()
hair = input("What is your hair color? ")
eyes = input("What is your eye color? ")
month = input("What is your birth month? ")
training = input("How many years of expierence do you have? ")

#quick inputs
#first = 'hayden'
#last = 'mcallister'
#email = 'mcallister.hayden05@gmail.com'
#phone = '208-576-1763'
#jobtitle = 'computer science'
#idnumber = '64-9821'

#output for information
print('\nYour ID Card is:')
print('----------------------------------------')
print(f'{last.upper()}, {first.capitalize()}')
print(f'{jobtitle.title()}')
print(f'{idnumber}')
print(f'\n{email}')
print(f'{phone}')
print(f'\nHair: {hair:15} Eyes: {eyes}')
print(f'Month: {month:14} Training: {training}')
print('----------------------------------------')