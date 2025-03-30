import pygame import json import random

Inisialisasi Pygame

pygame.init()

Konstanta Game

WIDTH, HEIGHT = 800, 400 BACKGROUND_COLOR = (0, 0, 0)  # Hitam TEXT_COLOR = (255, 255, 0)  # Kuning FONT_PATH = "assets/fonts/digital.ttf" QUESTION_FILE = "questions.json"

Load Pertanyaan

with open(QUESTION_FILE, "r", encoding="utf-8") as file: questions = json.load(file)

Load Font

font = pygame.font.Font(FONT_PATH, 40)

Load Sound Effects

correct_sound = pygame.mixer.Sound("assets/sounds/correct.wav") wrong_sound = pygame.mixer.Sound("assets/sounds/wrong.wav") top_survey_sound = pygame.mixer.Sound("assets/sounds/top_survey.wav")

Setup Game Screen

screen = pygame.display.set_mode((WIDTH, HEIGHT)) pygame.display.set_caption("Family Fortunes")

Game State

current_question = random.choice(questions) revealed_answers = [False] * len(current_question["answers"]) strikes = 0

Draw Text Function

def draw_text(text, x, y): text_surface = font.render(text, True, TEXT_COLOR) screen.blit(text_surface, (x, y))

Main Game Loop

running = True while running: screen.fill(BACKGROUND_COLOR)

# Tampilkan Pertanyaan
draw_text(current_question["question"], 50, 50)

# Tampilkan Jawaban
for i, ans in enumerate(current_question["answers"]):
    if revealed_answers[i]:
        draw_text(f"{i+1}. {ans['text']} - {ans['points']} pts", 100, 100 + i * 40)
    else:
        draw_text(f"{i+1}. ______ --", 100, 100 + i * 40)

# Event Handling
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_x:  # Strike
            wrong_sound.play()
            strikes += 1
        elif pygame.K_1 <= event.key <= pygame.K_8:
            idx = event.key - pygame.K_1
            if idx < len(current_question["answers"]):
                revealed_answers[idx] = True
                correct_sound.play()

pygame.display.flip()

pygame.quit()

