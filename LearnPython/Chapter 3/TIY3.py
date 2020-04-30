# 3-1 Names:
names = ["yang", "jason", "jacob", "alex", "lucy"]
print(names[0],names[1],names[2],names[3],names[4])

# 3-2 Greetings:
massage = f"hello {names[3].title()}, Have a nice day!"
print(massage)

# 3-3 Your Own List:
vehicle = ["motorcycle", "car", "train", "bullet train"]
massage = f"I want to go BeiJing by {vehicle[-1]}."
print(massage)

# 3-4 Guest List:
guest_name = ['jason', 'jay', 'charles', 'alex']
massage = f"Hi our guests :{guest_name}, we would like to invite you to dinner tonight 7pm."
print(massage)

# 3-5 Changing Guest list:
cant_come = guest_name.pop(2)
print(f"{cant_come} can't make the dinner, now we have {guest_name}.")
guest_name.insert(2, "lucy")
print(f"we have a new guest {guest_name[2]},our new guest list is : {guest_name}")


# 3-6 More Guests:
guest_name.insert(0, "July")
guest_name.insert(2, "Jacob")
guest_name.append("lily")
print(f"We just found a bigger dinner table,so we invite 3 more guests :{guest_name[0]}, {guest_name[2]}, {guest_name[-1]}, now our guest list is : \n{guest_name}." )

# 3-7 Shringking Guest List:
print("The new dinner table won't arrive in time, so we just have space fore only two guests")


for i in range(len(guest_name) - 2):
	guest_removed = guest_name.pop()
	print(f"Sorry {guest_removed}, We don't have enough seat to inivte you to the dinner ,maybe next time!")

print(f"Hi, {guest_name}, you still on the list. Welcome to the dinner tonigt!")
# for the 3-9
print(f"we have invited {len(guest_name)} guests at last.")
del guest_name[0]
del guest_name[0]
print(f"Ok finished, there is have : {guest_name} in list.")

# 3-8 Seeing the World:
locations = ['beijing', 'nanjing', "xi'an", 'hangzhong', 'luoyang']
print(f"this is the original list:\n\t{locations}")
print(f"this is the list in alphabetical order:\n\t{sorted(locations)},\nand the original list still is : \n\t{locations}")
locations.reverse()
print(f"this is the list in reverse:\n\t{locations}")
locations.reverse()
print(f"and reverse another time :\n\t{locations}")
locations.sort()
print(f'the list hasbeen sort by alphabetical order permannentily:\n\t{locations}')
locations.sort(reverse=True)
print(f"the list has been reverse permannentily: \n\t{locations}")

# 3-9 Dinner Guests:
print(f"we have invited {len(guest_name)} guests at last.")

# 3-10 Every Function:
countryies = ['China', "US", "Japan", "UK", "Franch", "Germany"]
print(sorted(countryies))
print(countryies)
countryies.reverse()
print(countryies)
countryies.sort()
print(countryies)
countryies.sort(reverse=True)
print(countryies)

# 3-11 intentional Error
print(guest_name[-1])

