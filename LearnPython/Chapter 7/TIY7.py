# print("7-1.Rental Car:")
# rental_car = input("What kind of rental car do you like? ")
# print(f"Let me see if I can find you a {rental_car}.")


# print("\n 7-2.Restaurant Seating:")
# numbers_of_people = int(input("How man people in your dinner group? "))
# if numbers_of_people >= 8:
    # print("Sorry, you have to wait for a table.")
# else:
    # print("Your table is ready.")

# print("\n 7-3.Multiples of Ten:")
# multiples_of_ten = int(input("Please enter a number and then I'll tell you it's a multiple of 10 or not. "))
# if multiples_of_ten % 10 == 0:
    # print(f"{multiples_of_ten} is a multiples of 10.")
# else:
    # print(f"{multiples_of_ten} is not a multiples of 10.")

# print("\n7-4.Pizza Toppings:")
# 
# prompt = "\nwhat topping would you want to add to your pizza? "
# prompt += "\n(Enter 'quit' when you are finished.)"
# 
# active = True
# while active:
    # toppings = input(prompt)
    # if toppings == 'quit':
        # active = False
    # else:
        # print(f"you'll add {toppings}")

# print("7-5.Movie Tickets:")  
# prompt = "\nHow old are you?"
# active = True
# while active:
    # age = int(input(prompt))
    # if age < 3:
        # price = 'free'
    # elif age < 12:
        # price = '$10'
    # else:
        # price = '$15'
    # print(f"your ticket price is {price}.")

# print("\n7-6.Three Exits:")
# prompt = "\nHow old are you?"
# prompt += "\n(Enter '0' to quit.)\n"
# while True:
    # age = int(input(prompt))
    # if age == 0:
        # break
    # elif age < 3:
        # price = 'free'
    # elif age < 12:
        # price = '$10'
    # else:
        # price = '$15'
        # 
    # print(f"your ticket price is {price}.")

# print("\n7-7.Infinity:")
# 
# print("\n7-8.Deli")
# sandwich_orders = ['Roast Pork', 'pastrami','Smoked Salmon Salad', 'pastrami','Chicken', 'pastrami']
# finished_sandwiches = []
# 
# print("The deli has run out of pastrami.")
# while 'pastrami' in sandwich_orders:
    # sandwich_orders.remove('pastrami')
# 
# while  sandwich_orders:
    # sandwich = sandwich_orders.pop()
    # print(f"I made your {sandwich} sandwich.")
    # finished_sandwiches.append(sandwich)
# 
# for finished_sandwich in finished_sandwiches:
    # print(finished_sandwich)
# 
# print("\n7-9.No Pastrami:")

print("\n7-10.Dream Vacation")
places = {}

polling_active = True

while polling_active:
    name = input("What's your name?")
    place = input("If you could vist one place in the world, where would you go?")

    places[name] = place

    repeat = input("would you like to let another person repond?(yes/no)")
    if repeat == 'no':
        polling_active = False
    
for name, place in places.items():
    print(f"{name} would like to vist {place}.")