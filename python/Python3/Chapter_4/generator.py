# Defining a generator
number_thing = (number for number in range(1,6))

# Properly prints out the numbers
print("1st")
for number in number_thing:
    print(number)

# Numbers are not stored anymore since it was consumed in the 1st for loop.
print("2nd")
for number in number_thing:
    print(number)


