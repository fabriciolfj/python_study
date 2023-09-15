from survey import AnonymousSurvey

question = "what language did you first learn to speak?"
language_survey = AnonymousSurvey(question)

language_survey.show_question()
print("enter 'q' at any time to quit.\n")
while True:
    response = input("language: ")

    if response == 'q':
        break

    language_survey.store_response(response)

print("\nthank you to everyone who participated in the survey!")
language_survey.show_results()