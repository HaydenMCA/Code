grade = float(input('enter a grade'))

letter = 'A'

if grade < 60:
    letter = 'F'
elif grade < 70:
    letter = 'D'
elif grade < 80:
    letter = 'C'
elif grade < 90:
    letter = 'A'

modifier = ''    
if grade % 10 >=7 and grade < 90 and grade > 60: 
    modifier = '+'
elif grade % 10 < 3 and grade < 100 and grade >= 60:
    modifier = '-'

print(f'{letter}{modifier})

