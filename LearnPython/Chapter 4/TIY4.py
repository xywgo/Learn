# 4-1 Pizzas
pizzas =['Neapolitan', 'Chicago', 'Sicilian', 'Detroit']
for pizza in pizzas:
    print(f"I like {pizza} pizza")
print("I really love pizza!")

# 4-2 Animals:
animals = ['dog', 'cat', 'rabbit']
for animal in animals:
    print(f"A {animal} would make a great pet.")
print("Any of these animals would make a great pet!")

# 4-3 Counting to Twenty:
for count in range(1, 21):
    print(count)

# 4-4 One Million:
one_million = []
for number in range(1, 1_000_000):
    # print(number)
    one_million.append(number)
max_number = max(one_million)
print(f"the max number is : {max_number}")
min_number = min(one_million)
print(f"the min number is : {min_number}")
sum_numbers = sum(one_million)
print(f"the sum of numbers is : {sum_numbers}")


# 4-6. Odd Numbers:
odd_numbers = []
for odd in range(1, 20, 2):
    print(odd)
    odd_numbers.append(odd)

# 4-7. Threes:
threes = []
for three in range(3, 31, 3):
    print(three)
    threes.append(three) 
# 4-8 Cubes:
cubes = []
for cube in range(1, 11):
    cubes.append(cube**3)
print(cubes)

# 4-9. Cube Comrehension:
cubes = [cube**3 for cube in range(1, 11)]
print(cubes)

# 4-10. Slices:
print(f"The first two items in the list are: {pizzas[:2]}")
print(f"Two items from the middle of the list are: {pizzas[2:]}")
print(f"The last two items in the list are: {pizzas[-2:]}")

# 4-11. My Pizzas, Your Pizzas:
my_pizzas = pizzas
friend_pizzas = my_pizzas[:]
my_pizzas.append("Greek")
friend_pizzas.append("St. Louis")
print("my favorite pizzas are:")
for my_pizza in my_pizzas:
    print(my_pizza)
print("\nMy friend favorite pizzas are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza)

# 4-12 More Loops:

# 4-13 Buffet:
buffet_foods = ('VEGETABLE SAMOSA', 'KEEMA SAMOSA', 'VEGETABLE PAKORA',
    'PANEER PAKORA', 'CHUNKY CHICKEN')
for buffet_food in buffet_foods:
    print(buffet_food)
# buffet_foods[2] = "FISH PAKORA"
buffet_foods = ('VEGETABLE SAMOSA', "FISH PAKORA", 'KEEMA SAMOSA', 
    'TOMATO SOUP' ,  'CHICKEN TANDOORI')
for buffet_food in buffet_foods:
    print(buffet_food)