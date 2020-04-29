motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
# motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# motorcycles[0] = 'ducati'
# print(motorcycles)

# motorcycles.append('ducati')
# print(motorcycles)

# motorcycles.insert(0, 'ducati')
# print(motorcycles)

# Removing an Item Using the del Statement
# del motorcycles[0]
# print(motorcycles)
# del motorcycles[1]
# print(motorcycles)


# Remving an Item Using the pop() Method
# popped_motorcycle = motorcycles.pop()
# print(motorcycles)
# print(popped_motorcycle)
# last_owned = motorcycles.pop()
# print(f"the last motorcycles I owned was a {last_owned.title()}.")

# Popping Items from any Position in a List
# first_owned = motorcycles.pop(0)
# print(f'The first motorcycle I owned was a {first_owned.title()}.')

# Removing an Item by Value
# motorcycles.remove('suzuki')
# print(motorcycles)
too_expensive = 'yamaha'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too_expensive for me.")