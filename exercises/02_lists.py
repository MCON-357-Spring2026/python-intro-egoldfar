"""
TODO:
1. Create list of favorite foods
2. Print first and last
3. Add one item
4. Remove one item
5. Print all items with loop
6. List comprehension for the lengths of each food item -
 create a new list where each item is  the length of the corresponding food item in the original list.
"""

foods = ['steak', 'lamb chops', 'broccoli', 'chocolate cake', 'waffles']

print(foods[0] + "\t" + foods[len(foods) - 1] + "\n")

foods.append('blueberries')

foods.remove('chocolate cake')

for food in foods:
    print(food)

lengths = [len(food) for food in foods]

print(lengths)

