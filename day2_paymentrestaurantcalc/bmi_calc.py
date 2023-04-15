height = float(input('What is your height in meters? '))
weight = float(input('What is your weight in kilograms (kg)? '))

bmi_index = weight/(height**2)

print(f"Your BMI index is {round(bmi_index,2)} kg/m^2.")