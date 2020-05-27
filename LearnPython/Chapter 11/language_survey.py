from survey import AnomymousSurvery

# Define a question, and make a survey.
question = "What language did you first learn to speak?"
my_survery = AnomymousSurvery(question)

# Show the quesion, and store resposes to the question.
my_survery.show_quesion()
print("Enter 'q' at any time to quit.\n")
while True:
	response = input("Language: ")
	if response == 'q':
		break
	my_survery.store_response(response)


# Show the survey results.
print("\nThank you to everyone who  participated in the survey!")
my_survery.show_results()

