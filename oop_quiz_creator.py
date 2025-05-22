#oop_quizzing_game
import pygame
import sys
import os

#main quiz creator screen/ allcaps po variable ko rito kasi na-search ko kapag constant all caps daw po
pygame.init()
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
PURPLE = (255, 0, 255)
DARK_PURPLE = (100, 0, 150)
FONT = pygame.font.SysFont("Helvetica", 25)
BIG_FONT = pygame.font.SysFont("Helvetica", 50)

# screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("QUIZ CREATOR GAME")


# class game user interface
class GameUI:
    def __init__(self, screen):
        self.screen = screen

    def draw_text(self, text, font, color, x, y, center=True):
        rendered = font.render(text, True, color)
        rect = rendered.get_rect(center=(x, y) if center else (x, y))
        self.screen.blit(rendered, rect)

    def get_input(self, prompt):
        user_input = ''
        active = True
        while active:
            self.screen.fill(PURPLE)
            self.draw_text(prompt, FONT, WHITE, WIDTH // 2, HEIGHT // 3)
            self.draw_text(user_input + '|', FONT, WHITE, WIDTH // 2, HEIGHT // 2)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        active = False
                    elif event.key == pygame.K_BACKSPACE:
                        user_input = user_input[:-1]
                    else:
                        user_input += event.unicode
        return user_input.strip()

    def draw_progress_bar(self, current, total):
        bar_width = 400
        bar_height = 30
        progress = int((current / total) * bar_width)
        pygame.draw.rect(self.screen, WHITE, [150, 400, bar_width, bar_height], 2)
        pygame.draw.rect(self.screen, DARK_PURPLE, [150, 400, progress, bar_height])
        percent = f"{int((current / total) * 100)}%"
        self.draw_text(f"Question {current} of {total} | {percent} completed", FONT, WHITE, WIDTH // 2, 150)

# class sfx
class SoundManager:
    def __init__(self, ding_path, music_path):
        self.ding = pygame.mixer.Sound(ding_path)
        pygame.mixer.music.load(music_path)

    def play_ding(self):
        self.ding.play()

    def play_music(self):
        pygame.mixer.music.play(-1, 0.0)

# clas questions
class QuizQuestion:
    def __init__(self, question, options, correct):
        self.question = question
        self.options = options
        self.correct =  correct

    def format(self):
        lines = [f"Q: {self.question}"]
        for label, text in zip(['a', 'b', 'c', 'd'], self.options):
            lines.append(f"{label}) {text}")
        lines.append(f"Answer: {self.correct}")
        lines.append("-" * 50)
        return "\n".join(lines) + "\n"

# class main game
class QuizCreatorGame:
    def __init__(self):
        self.ui = GameUI(screen)
        self.sound = SoundManager(
            "C:/Users/HANZ JOSEPH CALING/Downloads/sounds/ding.wav.mp3",
            "C:/Users/HANZ JOSEPH CALING/Downloads/sounds/from_the_start.mp3"
        )
        self.questions = []

    def start_screen(self):
        self.sound.play_music()
        running = True
        while running:
            screen.fill(PURPLE)
            self.ui.draw_text("Welcome to Quiz Creator Game!", BIG_FONT, WHITE, WIDTH // 2, HEIGHT // 3)
            self.ui.draw_text("Click to Start!", FONT, WHITE, WIDTH // 2, HEIGHT // 1.5)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.sound.play_ding()
                    running = False

    def create_questions(self, total):
        for i in range(total):
            screen.fill(PURPLE)
            self.ui.draw_text(f"Loading question {i+1} of {total}...", FONT, WHITE, WIDTH // 2, 150)
            pygame.display.flip()
            pygame.time.wait(1000)

            screen.fill(PURPLE)
            self.ui.draw_progress_bar(i + 1, total)
            pygame.display.flip()
            pygame.time.wait(1000)

            question = self.ui.get_input("Enter your question:")
            options = [
                self.ui.get_input("A."),
                self.ui.get_input("B."),
                self.ui.get_input("C."),
                self.ui.get_input("D.")
            ]

            correct = ''
            while correct not in ['A', 'B', 'C', 'D']:
                correct = self.ui.get_input("Enter answer A/B/C/D:").upper()

            q = QuizQuestion(question, options, correct)
            self.questions.append(q)

    def save_to_file(self):
        with open("quiz_data.txt", "w", encoding="utf-8") as f:
            for q in self.questions:
                f.write(q.format())
        return "quiz_data.txt"
    
    def show_end_screen(self, filepath):
        screen.fill(PURPLE)
        self.ui.draw_text("Saved to quiz_data.txt", BIG_FONT, WHITE, WIDTH // 2, HEIGHT // 3)
        pygame.display.flip()
        pygame.time.wait(1500)
        os.startfile(filepath)
        pygame.quit()
        sys.exit()

    def run(self):
        self.start_screen()
        total = int(self.ui.get_input("How many questions will you input?"))
        self.create_questions(total)
        path = self.save_to_file()
        self.show_end_screen(path)


# Run the game
if __name__ == "__main__":
    game = QuizCreatorGame()
    game.run()