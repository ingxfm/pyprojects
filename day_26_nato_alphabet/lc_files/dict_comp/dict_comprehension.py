sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:
list_words = sentence.split()
result = {word: len(word) for word in list_words}


print(result)

