"""
Game mode and sequential game logic

- Game logic (no UI here, the Streamlit app only reads the game state)
- Single or Two Player mode
- Hot/cold meter, live range and one hint per game
- Score and store results
"""

import random
from datetime import datetime
from .settings import (difficulty, levels_by_name, min_num, max_num,
                       statistics_file, hint_cost, heat_levels)
import openpyxl


# New game state (stored in st.session_state)
def new_game(mode, level_key, secret_number=None):
    configuration = difficulty[level_key]

    if secret_number is None:
        secret_number = random.randint(min_num, max_num)

    return {
        'mode': mode,                       # "Single" or "Double"
        'configuration': configuration,
        'secret_number': secret_number,
        'max_attempts': configuration['attempts'],
        'remaining_attempts': configuration['attempts'],
        'low': min_num,                     # smallest possible number left
        'high': max_num,                    # biggest possible number left
        'history': [],
        'hint_used': False,
        'hint_block': None,
        'guessed': False,
        'finished': False,
        'saved': False,
        'feedback': {'kind': 'info', 'text': "Enter your first attempt"}
    }


# Secret number for 2 Player mode
def validate_secret(text):
    try:
        secret_number = int(str(text).strip())
    except ValueError:
        return None, f"Remember, number between {min_num} and {max_num}"

    if min_num <= secret_number <= max_num:
        return secret_number, None
    return None, f"Number must be between {min_num} and {max_num}."


# Hot/cold meter
def heat_level(distance):
    for max_distance, label, fill in heat_levels:
        if distance <= max_distance:
            return label, fill
    return heat_levels[-1][1], heat_levels[-1][2]


# One attempt
def play_turn(game, guess):
    if game['finished']:
        return

    # Invalid guesses don't use attempts
    if guess is None:
        game['feedback'] = {'kind': 'warn', 'text': f"Type a number between {min_num} and {max_num}"}
        return

    guess = int(guess)
    if guess < min_num or guess > max_num:
        game['feedback'] = {'kind': 'warn', 'text': f"Please enter a number between {min_num} and {max_num}"}
        return

    if guess in [entry['guess'] for entry in game['history'] if entry['type'] == 'guess']:
        game['feedback'] = {'kind': 'warn', 'text': f"You already tried {guess}, attempt not used"}
        return

    game['remaining_attempts'] -= 1
    secret_number = game['secret_number']
    heat, fill = heat_level(abs(guess - secret_number))

    if guess == secret_number:
        direction = 'hit'
        game['guessed'] = True
        game['feedback'] = {'kind': 'win', 'text': "Congratulations! You guessed the number!"}
    elif guess < secret_number:
        direction = 'up'
        game['low'] = max(game['low'], guess + 1)
        game['feedback'] = {'kind': 'info', 'text': f"{guess}? Try with a HIGHER number"}
    else:
        direction = 'down'
        game['high'] = min(game['high'], guess - 1)
        game['feedback'] = {'kind': 'info', 'text': f"{guess}? Try with a LOWER number"}

    game['history'].append({'type': 'guess', 'guess': guess, 'direction': direction,
                            'heat': heat, 'fill': fill})

    if game['guessed']:
        game['finished'] = True
    elif game['remaining_attempts'] == 0:
        game['finished'] = True
        game['feedback'] = {'kind': 'lose',
                            'text': f"Sorry, you didn't make it this time, {secret_number} was the number"}


# Hint: shows the hundred block, costs attempts
def can_use_hint(game):
    return (not game['finished'] and not game['hint_used']
            and game['remaining_attempts'] > hint_cost)


def use_hint(game):
    if not can_use_hint(game):
        return

    secret_number = game['secret_number']
    block_start = (secret_number - 1) // 100 * 100 + 1
    block_end = min(block_start + 99, max_num)

    game['remaining_attempts'] -= hint_cost
    game['hint_used'] = True
    game['hint_block'] = (block_start, block_end)
    game['low'] = max(game['low'], block_start)
    game['high'] = min(game['high'], block_end)
    game['history'].append({'type': 'hint', 'block': (block_start, block_end)})
    game['feedback'] = {'kind': 'info', 'text': f"Hint: it's between {block_start} and {block_end}"}


# Last guess (for the hot/cold meter)
def last_guess(game):
    guesses = [entry for entry in game['history'] if entry['type'] == 'guess']
    return guesses[-1] if guesses else None


def attempts_used(game):
    return game['max_attempts'] - game['remaining_attempts']


# Score: base points + bonus per attempt left (0 if lost)
def calculate_score(level, attempts, result):
    configuration = levels_by_name.get(level)
    won = result in (True, "Won")
    if configuration is None or not won:
        return 0

    attempts_left = max(configuration['attempts'] - int(attempts), 0)
    return configuration['base'] + configuration['bonus'] * attempts_left


def game_score(game):
    return calculate_score(game['configuration']['level'], attempts_used(game), game['guessed'])


# Store results (same columns as before)
def save_record(name, mode, configuration, attempts, result):
    try:
        workbook = openpyxl.load_workbook(statistics_file)
        sheet = workbook.active

        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        result_text = "Won" if result else "Lost"
        level = configuration['level']
        name = name.strip() or "Anonymous"

        sheet.append([date, name, mode, level, attempts, result_text])
        workbook.save(statistics_file)
        return True, None

    except Exception as e:
        return False, f"An error occurred while saving: {e}"
