"""
TODO:
Create and unpack a tuple
Create a tuple named 'coordinates' that contains three values: latitude, longitude, and altitude.
Unpack the tuple into three separate variables: lat, lon, and alt.
Create a tuple with mixed data types
Create a tuple named 'person_info' that contains a string (name), an integer (age), and a float (height).
Unpack the tuple into three separate variables: name, age, and height.
Demonstrate tuple immutability
Create a tuple named 'immutable_tuple' with three integer values.
Attempt to change the first element of the tuple to a different value and handle the exception that arises
"""

coordinates = ("27°59′18″N", "86°55′31″E", "8,848.86 meters")

lat, lon, alt = coordinates

print(lat, lon, alt)

person_info = ("Jane Doe", 18, 5.5)

name, age, height = person_info

print(name, age, height)

immutable_tuple = (1, 2, 3)

try:
    immutable_tuple[0] = 9
except TypeError:
    print("I'm sorry, I can't do that")
finally:
    print(immutable_tuple)