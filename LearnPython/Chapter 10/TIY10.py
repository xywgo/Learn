# 10-1. Learning Python:
filename = 'learning_python.txt'
with open(filename) as lp:
	lines = lp.readlines()

contexts = ''
for line in lines:
	contexts += line

print(contexts)

#10-2. Learning C:

print(contexts.replace('Python', 'C'))

#10-3. Guest:
with open('guest.txt', 'a') as file_object:
	name = input('Please enter you name: ')
	file_object.write(name + '\n')

#10-4. Guest Book:
# see guest_book.py


#10-5. Programming Poll:
# see programing_poll.py

#10-6. Addition:
# see addition.py

#10-7. addition Calculator:
# see addition.py

#10-8. Cats and Dogs:
# see cats_and_dogs.py

#10-9 Silent cats and dogs:
# same as above

#10-10. Common Words:
# see common_words.py

#10-11. Favorite Number:
# see favorite_number.py and read_favorite_number.py

#10-12. Favorite Number Remebered:
# see comine.py

#10-13. Verify User:
