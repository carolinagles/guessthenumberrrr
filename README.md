# Guess the Number

A retro Streamlit version of the console game: a liquid glass shell, a lilac WordArt title and a handheld-style LCD screen.

**Main Structure:**
- **Menu** with 3 screens: Play, Records, Rules
- **Palette**: sage #99B898, peach #FECEA8, salmon #FF847C, coral #E84A5F, slate #2A363B
- **Shell color** picker: Sage, Peach, Salmon, Coral
- **Mode and difficulty** before each game: Single or Two players, Easy (20 tries), Medium (12 tries), Hard (5 tries)

**Game Rules:**
- Target number is always between **1 and 1000**
- Player gets hints if their guess is too high or too low
- **Range bar** shrinks to show which numbers are still possible
- **Heat meter** shows how close the last guess was (Freezing → Burning)
- **One hint per game**: reveals the hundred the number is in, costs 1 attempt
- Repeated or out-of-range guesses don't use attempts
- In two player mode, player 1 types the secret number hidden
- Game ends when player guesses correctly or runs out of attempts

**Score:**
| Difficulty | Win points | Per attempt left |
|---|---|---|
| Easy | 100 | +10 |
| Medium | 250 | +25 |
| Hard | 600 | +100 |

Score is calculated from the saved columns, so old records get a score too.

**Data Tracking:**
- After each game, player enters their name
- All results are saved to `data/statistics.xlsx` (same columns as before)
- Records screen: summary, leaderboard by score, last 20 games, player performance and won/lost charts, with a difficulty filter

## Project structure
```
app.py              # Streamlit app (replaces main_menu)
mod/
  settings.py       # file, difficulty, range, score, heat levels, colors
  game.py           # game logic, score and save_record
  records.py        # statistics, leaderboard and charts
  ui.py             # screen pieces (LCD, range bar, heat meter, tables)
  style.py          # liquid glass + WordArt CSS
data/statistics.xlsx
requirements.txt
.streamlit/config.toml
```

## Run
```
pip install -r requirements.txt
streamlit run app.py
```

## Deploy on Streamlit Community Cloud
Push the folder to GitHub, create a new app and choose `app.py` as the main file.
Note: on Streamlit Cloud the file system resets when the app restarts, so new games saved there can be lost. For permanent records, connect a database or Google Sheets later.
