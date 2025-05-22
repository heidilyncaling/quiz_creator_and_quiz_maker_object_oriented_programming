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
