class QuizGame:
    def __init__(self):
        self.questions = [
            {
                "question": "How many infinity stones are there?",
                "options": ["8", "10", "6", "4"],
                "answer": 3  # 6 is at index 3 (1-based)
            },
            {
                "question": "What is the only food that cannot go bad?",
                "options": ["Chocolate", "Peanut Butter", "Canned Tuna", "Honey"],
                "answer": 4  # Honey
            },
            {
                "question": "Which 90s boy band member bought MySpace in 2011?",
                "options": ["Nick Lachey", "Justin Timberlake", "Shawn Stockman", "AJ McLean"],
                "answer": 2  # Justin Timberlake
            }
        ]

    def start(self):
        print("🎉 Welcome to the Python Quiz Game!\n")
        score = 0

        for i, q in enumerate(self.questions, start=1):
            print(f"Question {i}: {q['question']}")
            for idx, option in enumerate(q['options'], start=1):
                print(f"  {idx}. {option}")

            while True:
                answer = input("Your answer (1-4): ")
                if answer.isdigit():
                    answer = int(answer)
                    if 1 <= answer <= len(q['options']):
                        break
                    else:
                        print("Please enter a number between 1 and 4.")
                else:
                    print("Invalid input. Please enter a number.")

            if answer == q['answer']:
                print("✅ Correct!\n")
                score += 1
            else:
                correct_option = q['options'][q['answer'] - 1]
                print(f"❌ Incorrect! The correct answer was: {correct_option}\n")

        print(f"🏁 Quiz Complete! Your score: {score}/{len(self.questions)}")


# Run the game
if __name__ == "__main__":
    quiz = QuizGame()
    quiz.start()