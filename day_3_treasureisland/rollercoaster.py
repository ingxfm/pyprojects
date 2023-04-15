height = float(input('What is your height in centimeters? '))

if height > 120:
    print('can ride')
    age = int(input('what is your age? '))
    bill: int = 0
    if age < 12:
        bill += 5
    elif age < 18:
        bill += 7
    elif 45 <= age <= 55:
        bill += 0
    else:
        bill += 12
    want_photo = input('Do you want a photo? Type "y" for y, otherwise is No: ').lower()

    if want_photo == 'y':
        bill += 3

    print(f'Your bill is ${bill}.')
