print('Welcome to the tip calculator!')
total_bill = float(input('What was the total bill? '))
split_number = int(input('How many people to split the bill? '))
choose_tip_percent = \
    input('What percentage tip would you like to give? 10, 12, or 15. Choose A,B, or C respectively. ').lower()

tip_percent = 0

if choose_tip_percent == 'a':
    tip_percent = 0.10
elif choose_tip_percent == 'b':
    tip_percent = 0.12
elif choose_tip_percent == 'c':
    tip_percent = 0.15
else:
    print('Not valid choice')

per_capita: float = (total_bill*(1+tip_percent))/split_number

print(f'Each person should pay: ${per_capita:.2f}')
