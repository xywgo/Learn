#alien_0 = {}

# alien_0['color'] = 'green'
# alien_0['points'] = 5

# new_points = alien_0['points']
# print(f"You just earned {new_points} points!")

# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# del alien_0['points']
# print(alien_0)

# alien_0 = {'color': 'green'}
# print(f"The alien is {alien_0['color']}.")

# alien_0['color'] = 'yellow'
# print(f"The alien is now {alien_0['color']}")


# alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
# print(f"Original y_position: {alien_0['x_position']}")

# # Move the alien to the right.
# # Determine how far to move the alien based on its current speed.
# if alien_0['speed'] == 'slow':
# 	x_increment = 1
# elif alien_0['speed'] == 'medium':
# 	x_increment = 2
# else:
# 	# This must be a fast alien.
# 	x_increment = 3

# # The new position is the old position plus the incremnet.
# alien_0['x_position'] = alien_0['x_position'] + x_increment

# print(f"New position: {alien_0['x_position']}")

# Make an empty list for storing aliens.
aliens = []

# Make 30 green aliens.
for alien_number in range(30):
	new_alein = {'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alein)

for alien in aliens[:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = 10
	elif alien['color'] == 'yellow':
		alien['color'] = 'red'
		alien['speed'] = 'fast'
		alien['points'] = 15

# Show the first 5 aliens.
for alien in aliens[:5]:
	print(alien)
print("...")

# Show how many aliens have been created.
print(f"Total numer of aliens: {len(aliens)}")

