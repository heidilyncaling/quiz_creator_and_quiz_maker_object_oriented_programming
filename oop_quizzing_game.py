import os
import random

# class for the questions
class QuizQuestion:
    def __init__(self, text, options, answer):
        self.text = text
        self.options = options  # dict: {"A": "...", "B": "...", ...}
        self.answer = answer.upper()

    def display(self, number):
        print(f"\nQuestion {number}: {self.text}")
        for key in ["A", "B", "C", "D"]:
            print(f"{key}. {self.options[key]}")

    def is_correct(self, user_answer):
        return user_answer.upper() == self.answer

    def correct_answer_text(self):
        return f"{self.answer}: {self.options[self.answer]}"
    
# class handle the data.txt
class QuizLoader:
    def load_from_file(self, file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read().strip()
        except FileNotFoundError:
            print("File not found.")
            return []

        blocks = content.split("-" * 50)
        questions = []

        for block in blocks:
            lines = block.strip().splitlines()
            if len(lines) >= 6:
                question

# class, runs the mismong quiz game
class QuizGame:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def run(self):
        if not self.questions:
            print("No valid questions to run.")
            return

        random.shuffle(self.questions)

        for idx, question in enumerate(self.questions, 1):
            question.display(idx)

            while True:
                user_input = input("A/B/C/D or EXIT: ").strip().upper()
                if user_input == "EXIT":
                    print("\nExiting. Thanks for playing!")
                    print(f"Your score: {self.score}/{idx - 1}")
                    return
                if user_input in ["A", "B", "C", "D"]:
                    break
                print("Invalid input. Please enter A, B, C, D or EXIT.")

            if question.is_correct(user_input):
                print("Correct!")
                self.score += 1
            else:
                print(f"Wrong. The correct answer is: {question.correct_answer_text()}")

        print("\nThanks for playing!")
        print(f"Your score: {self.score}/{len(self.questions)}")

#main
def main():
    default_path = "quiz_data.txt"
    file_path = default_path

    if not os.path.isfile(file_path):
        print("Default file not found.")
        file_path = input("Enter full path to quiz file: ").strip()
        if not os.path.isfile(file_path):
            print("Still can't find the file. Exiting.")
            return

    loader = QuizLoader()  # Create an instance
    questions = loader.load_from_file(file_path)  # Use instance method
    game = QuizGame(questions)
    game.run()

if __name__ == "__main__":
    main()
