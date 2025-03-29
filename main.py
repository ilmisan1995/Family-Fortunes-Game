import pygame import random import json

Inisialisasi Pygame

pygame.init() pygame.mixer.init()

Ukuran layar

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 400 screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) pygame.display.set_caption("Family Fortunes Game")

Warna

BLACK, BLUE, YELLOW, WHITE, RED = (0, 0, 0), (0, 0, 255), (255, 255, 0), (255, 255, 255), (255, 0, 0)

Font

digital_font = pygame.font.Font("fonts/digital-7.ttf", 28)

Load Sound Effects

top_survey_sound = pygame.mixer.Sound("sounds/top_survey.wav") strike_sound = pygame.mixer.Sound("sounds/strike.wav") round_start_sound = pygame.mixer.Sound("sounds/round_start.wav") fast_money_sound = pygame.mixer.Sound("sounds/fast_money.wav") winner_sound = pygame.mixer.Sound("sounds/winner.wav")

Load pertanyaan dari file JSON

def load_questions(filename): with open(filename, "r", encoding="utf-8") as file: return json.load(file)

questions = load_questions("questions.json") current_question_index = 0

def next_question(): global current_question_index if current_question_index < len(questions): question_data = questions[current_question_index] display_text(question_data["question"], 200, 50, digital_font, YELLOW) current_question_index += 1

def reveal_answer(key_number): if key_number <= len(questions[current_question_index - 1]["answers"]): answer_data = questions[current_question_index - 1]["answers"][key_number - 1] display_text(f"{answer_data['text']} - {answer_data['points']} Pts", 200, 100 + key_number * 30, digital_font, YELLOW) top_survey_sound.play()

Babak permainan

rounds = [ {"type": "Single Point", "answers": 8}, {"type": "Single Point", "answers": 8}, {"type": "Double Point", "answers": 6}, {"type": "Double Point", "answers": 6}, {"type": "Triple Point", "answers": 4}, {"type": "Triple Point", "answers": 4}, {"type": "Fast Money", "answers": 5} ] current_round, strikes, fast_money_mode, fast_money_player = 0, 0, False, 0 revealed_answers, fast_money_scores = [], [[], []]

def draw_board(): screen.fill(BLACK) pygame.draw.rect(screen, BLUE, (150, 50, 500, 250))  # Panel jawaban pygame.draw.rect(screen, BLACK, (650, 150, 100, 50))  # Kotak skor

display_text("TOTAL", 670, 120, digital_font, YELLOW)
display_text(f"Round: {rounds[current_round]['type']}", 320, 20, digital_font, YELLOW)
draw_buttons()
draw_strikes()
if fast_money_mode:
    draw_fast_money()

def display_text(text, x, y, font, color): text_surface = font.render(text, True, color) screen.blit(text_surface, (x, y))

def draw_buttons(): pygame.draw.rect(screen, WHITE, (100, 320, 200, 50))  # Tombol Next Question pygame.draw.rect(screen, WHITE, (500, 320, 200, 50))  # Tombol Reveal Answers pygame.draw.rect(screen, WHITE, (320, 320, 150, 50))  # Tombol Next Round pygame.draw.rect(screen, RED, (650, 50, 100, 50))  # Tombol X (strike) display_text("NEXT QUESTION", 120, 335, digital_font, BLACK) display_text("REVEAL ANSWERS", 520, 335, digital_font, BLACK) display_text("NEXT ROUND", 340, 335, digital_font, BLACK) display_text("X", 690, 60, digital_font, WHITE)

def draw_strikes(): for i in range(strikes): display_text("X", 150 + (i * 50), 10, digital_font, RED)

def draw_fast_money(): y_offset = 70 display_text(f"FAST MONEY - PLAYER {fast_money_player + 1}", 180, 40, digital_font, YELLOW) for i, (answer, score) in enumerate(fast_money_scores[fast_money_player], start=1): display_text(f"{i}. {answer} - {score}", 180, y_offset, digital_font, YELLOW) y_offset += 30

def start_fast_money(): global fast_money_mode, fast_money_scores, fast_money_player fast_money_mode = True fast_money_scores = [[], []]  # Reset skor fast_money_player = 0 fast_money_sound.play()

def record_fast_money_answer(answer, score): if len(fast_money_scores[fast_money_player]) < 5: fast_money_scores[fast_money_player].append((answer, score)) if len(fast_money_scores[fast_money_player]) == 5 and fast_money_player == 0: fast_money_player = 1

def next_round(): global current_round, strikes, revealed_answers, fast_money_mode if current_round < len(rounds) - 1: current_round += 1 strikes = 0 revealed_answers = [] round_start_sound.play() if current_round == len(rounds) - 1: start_fast_money()

running = True while running: draw_board() for event in pygame.event.get(): if event.type == pygame.QUIT: running = False elif event.type == pygame.KEYDOWN: if event.key == pygame.K_n: next_question() elif pygame.K_1 <= event.key <= pygame.K_8: reveal_answer(event.key - pygame.K_0) elif event.key == pygame.K_x and strikes < 3: strikes += 1 strike_sound.play() elif event.key == pygame.K_n: next_round() pygame.display.update() pygame.quit()

