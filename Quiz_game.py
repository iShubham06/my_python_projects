def quiz_game():
    score = 0

    questions = [
        {"question": "What is the capital of France?", "answer": "Paris"
         },
        {"question": "What is the largest planet in our solar system?", "answer": "Jupiter"
         },
        {"question": "What is the chemical symbol for gold?", "answer": "Au"
         },
        {"question": "What is the tallest mountain in the world?", "answer": "Mount Everest"
         },
        {"question": "What is the smallest prime number?", "answer": "2"
         }   
    ]

    for question in questions:
        print(question["question"])

        user_answer = input("Your answer: ")

        while not user_answer.strip():
            print("Please enter a valid answer.")
            user_answer = input("Your answer: ")


        if user_answer.strip().lower() == question["answer"].lower():
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect! The correct answer is: {question['answer']}")

    print(f"Your final score is: {score}/{len(questions)}")

quiz_game()