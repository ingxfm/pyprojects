list1 = [{
    "email": "jauncagabriel@gmail.com",
    "gmail": "ramon@gmail.com"
},
    {
    "2222": "gaga@gmail.com",
    "3223": "nora@gmail.com"
},
]

dict1 = list1[1]
print(list1)
print(dict1)
position = list1.index(dict1)
print(f"Here: {position}")

list1.remove(list1[position])

print(list1)

