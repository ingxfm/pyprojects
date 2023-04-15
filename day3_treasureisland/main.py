import matplotlib as mt
import numpy as np

height = float(input('What is your height in meters? '))
weight = float(input('What is your weight in kilograms (kg)? '))

bmi_index = weight/(height**2)
diagnostic: str = ''
if bmi_index < 18.5:
    diagnostic = 'underweight'
elif bmi_index < 25:
    diagnostic = 'normal weight'
elif bmi_index < 30:
    diagnostic = 'overweight'
elif bmi_index < 35:
    diagnostic = 'obese'
else:
    diagnostic = 'clinically obese'


print(f"Your BMI index is {round(bmi_index,2)} kg/m^2. You are {diagnostic}.")


