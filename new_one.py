questions = [
    {"question": "units of resistance?", "options": ["A. watts", "B. henry", "C. ohms"], "answer": "C"},
    {"question": "units of power?", "options": ["A. watts", "B. henry", "C. ohms"], "answer": "A"},
    {"question": "units of inductor?", "options": ["A. watts", "B. henry", "C. ohms"], "answer": "B"},
    {"question": "units of capacitor?", "options": ["A. watts", "B. farad", "C. ohms"], "answer": "B"},
    {"question": "units of force?", "options": ["A. watts", "B. henry", "C. newtons"], "answer": "C"},
]

score = 0

for i in questions:
    print(i["question"])
    for option in i["options"]:
        print(option)

    # keep the valid letters, e.g. ["A", "B", "C"]
    valid_choices = [option[0] for option in i["options"]]

    user_answer = input("Your answer (A/B/C): ").upper()

    # keep asking until they type a valid letter
    while user_answer not in valid_choices:
        print("Invalid choice. Please type one of:", valid_choices)
        user_answer = input("Your answer (A/B/C): ").upper()

    if user_answer == i["answer"]:
        score += 1
        print("Correct!")
    else:
        print("Wrong! The correct answer was", i["answer"])

print("Your final score:", score, "/", len(questions))