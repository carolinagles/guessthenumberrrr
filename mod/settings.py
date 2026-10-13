"""
Settings

- Creation of folder and file for statistics
    'data/statistics.xlsx' to store result statistics
- Difficulty levels: easy 20, medium 12 and hard 5
- Range of number to guess (1-1000)
- Score points per difficulty
- Heat levels for the hot/cold meter
- Color palette and glass shell colors
- Animated GIF background
"""

import os
import openpyxl
from pathlib import Path


# Create folder and statistics file (inside the project, works on Streamlit Cloud)
folder = Path(__file__).resolve().parent.parent / "data"
statistics_file = folder / "statistics.xlsx"
os.makedirs(folder, exist_ok=True)

columns = ["Date", "Name", "Mode", "Difficulty", "Attempts", "Result"]

# Create file
if not os.path.exists(statistics_file):
    excel_document = openpyxl.Workbook()
    sheet = excel_document.active
    sheet.title = "Statistics"
    sheet.append(columns)
    excel_document.save(statistics_file)

# Difficulty levels
# base  → points for winning
# bonus → extra points for every attempt left
difficulty = {
    '1': {'level': 'Easy', 'attempts': 20, 'base': 100, 'bonus': 10},
    '2': {'level': 'Medium', 'attempts': 12, 'base': 250, 'bonus': 25},
    '3': {'level': 'Hard', 'attempts': 5, 'base': 600, 'bonus': 100}
}

# Same levels, searchable by name (used to score old records)
levels_by_name = {config['level']: config for config in difficulty.values()}

# Range for guessing
min_num = 1
max_num = 1000

# Hint: reveals the hundred block of the secret number
hint_cost = 1

# Heat levels: (max distance, label, meter fill %)
heat_levels = [
    (10, "Burning", 100),
    (50, "Hot", 80),
    (150, "Warm", 58),
    (300, "Cool", 34),
    (max_num, "Freezing", 12)
]

# Palette
palette = {
    'sage': '#99B898',
    'peach': '#FECEA8',
    'salmon': '#FF847C',
    'coral': '#E84A5F',
    'slate': '#2A363B'
}

# Animated background (liquid bubbles) and how much white goes on top (0 = original, 1 = white)
background_gif = ("https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExYnN6YTViaWl2OGpjdWo2enNyMnU4dGkz"
                  "d3lhOTZmMzZuMHdsMzJmcCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3Z1b8Z5ESU2fgScGab/giphy.gif")
background_light = 0.35

# Shell colors (from the palette)
# rgb → glass tint, deep → shadows and outlines, text → text on top of the color
flavors = {
    'Sage': {'rgb': (153, 184, 152), 'deep': (74, 110, 74), 'text': '#2A363B'},
    'Peach': {'rgb': (254, 206, 168), 'deep': (176, 110, 60), 'text': '#2A363B'},
    'Salmon': {'rgb': (255, 132, 124), 'deep': (168, 58, 52), 'text': '#2A363B'},
    'Coral': {'rgb': (232, 74, 95), 'deep': (130, 22, 40), 'text': '#FFFFFF'}
}
