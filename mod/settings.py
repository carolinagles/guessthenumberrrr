"""
Settings

- Creation of folder and file for statistics
    'data/statistics.xlsx' to store result statistics
- Difficulty levels: easy 20, medium 12 and hard 5
- Range of number to guess (1-1000)
- Score points per difficulty
- Heat levels for the hot/cold meter
- Shell colors (translucent 90s computer flavors)
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

# Shell colors: rgb → translucent shell, deep → shadows and outlines
flavors = {
    'Lagoon': {'emoji': '🔵', 'rgb': (31, 163, 201), 'deep': (8, 92, 122)},
    'Grape': {'emoji': '🟣', 'rgb': (123, 63, 184), 'deep': (70, 28, 115)},
    'Tangerine': {'emoji': '🟠', 'rgb': (255, 138, 30), 'deep': (176, 78, 0)},
    'Lime': {'emoji': '🟢', 'rgb': (61, 190, 76), 'deep': (24, 112, 38)},
    'Cherry': {'emoji': '🔴', 'rgb': (226, 36, 94), 'deep': (138, 12, 52)}
}
