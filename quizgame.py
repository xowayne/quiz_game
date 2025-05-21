class Question:
    def __init__(self, text, options, answer_index):
        self.text = text
        self.options = options
        self.answer_index = answer_index  # 1-based (e.g., 1 for option[0])

    def is_correct(self, user_choice):
        return user_choice == self.answer_index

    def get_correct_option(self):
        return self.options[self.answer_index - 1]


class QuizGame:
    def __init__(self):
        self.questions = [
            Question("How many infinity stones are there?", ["8", "10", "6", "4"], 3),
            Question("What is the only food that cannot go bad?", ["Chocolate", "Peanut Butter", "Canned Tuna", "Honey"], 4),
            Question("Which 90s boy band member bought MySpace in 2011?", ["Nick Lachey", "Justin Timberlake", "Shawn Stockman", "AJ McLean"], 2),
            Question("Which of these is the most visited attraction in the world?", ["Eiffel Tower", "Statue of Liberty", "Forbidden City", "Colosseum"], 3),
            Question("What's the heaviest organ in the human body?", ["Brain", "Liver", "Skin", "Heart"], 3),
            Question("What type of food holds the world record for being the most stolen?", ["Coffee", "Cheese", "Wagyu beef", "Chocolate"], 2),
            Question("What element does the chemical symbol Au stand for?", ["Silver", "Magnesium", "Salt", "Gold"], 4),
            Question("What is the oldest major soft drink brand in the U.S.?", ["Coca Cola", "Pepsi", "Dr. Pepper", "Canada Dry Ginger Ale"], 3),
            Question("Highest-grossing video game franchise to date?", ["Mario", "Call of Duty", "Street Fighter", "Pokemon"], 4),
            Question("Mycology is the study of what?", ["Fungi", "Cancer cells", "Flowers", "Blood"], 1),
            Question("Closest living relative of a human?", ["Gorillas", "Monkeys", "Bonobos", "Homo sapiens"], 3),
            Question("What does “zodiac” mean in Ancient Greek?", ["Circle of animals", "Circle of personalities", "Circle of stars", "Circle of futures"], 1),
            Question("Which cereal grain is most used in beer?", ["Wheat", "Barley", "Hops", "Rice"], 2),
            Question("Pupusas are from what country?", ["Mexico", "El Salvador", "Brazil", "Poland"], 2),
            Question("Where did the croissant originate?", ["France", "Turkey", "Austria", "Tokyo"], 3),
        ]

    def start(self):
        print(" Welcome to the Python Quiz Game!\n")
        score = 0

        for i, q in enumerate(self.questions, start=1):
            print(f"Question {i}: {q.text}")
            for idx, option in enumerate(q.options, start=1):
                print(f"  {idx}. {option}")

            while True:
                answer = input("Your answer (1-4): ")
                if answer.isdigit():
                    answer = int(answer)
                    if 1 <= answer <= len(q.options):
                        break
                    else:
                        print("Please enter a number between 1 and 4.")
                else:
                    print("Invalid input. Please enter a number.")

            if q.is_correct(answer):
                print("Correct!\n")
                score += 1
            else:
                print(f"Incorrect! ")

        print(f"Quiz Complete! Your score: {score}/{len(self.questions)}")

if __name__ == "__main__":
    quiz = QuizGame()
    quiz.start()