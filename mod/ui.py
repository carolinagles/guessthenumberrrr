"""
Screen pieces (HTML)

- Bezel header
- LCD screen with attempts left
- Range scanner and hot/cold meter
- Guess history chips
- Stat tiles and retro tables
"""
import html
from .settings import min_num, max_num
from .game import last_guess, game_score


def _pos(number):
    return (number - min_num) / (max_num - min_num) * 100


# Header
def bezel():
    return ('<div class="bezel"><div class="bezel-led" aria-hidden="true"></div>'
            '<div class="bezel-title">Guess the Number</div>'
            f'<p class="bezel-sub">A number from {min_num} to {max_num} is hiding. '
            'Find it before the attempts run out.</p></div>')


def part_name(text):
    return f'<div class="part-name">{html.escape(text)}</div>'


# LCD screen
def lcd(game):
    configuration = game['configuration']
    mode_text = "Single player" if game['mode'] == "Single" else "Two players"
    secret_number = game['secret_number']

    cells = "".join(
        f'<span class="cell{" used" if i >= game["remaining_attempts"] else ""}"></span>'
        for i in range(game['max_attempts'])
    )

    state = ""
    if game['finished'] and game['guessed']:
        state = "win"
        caption = f"Got it in {game['max_attempts'] - game['remaining_attempts']}! Score {game_score(game)}"
        big = f"{secret_number}"
    elif game['finished']:
        state = "lose"
        caption = "Out of attempts. The number was"
        big = f"{secret_number}"
    elif game['low'] == game['high']:
        caption = "Only one number left"
        big = f"{game['low']}"
    else:
        caption = "The number is between"
        big = f"{game['low']}–{game['high']}"

    feedback = game['feedback']
    return (
        '<div class="lcd-frame">'
        f'<div class="lcd {state}" role="status" aria-live="polite">'
        '<div class="lcd-row">'
        f'<div>{mode_text}<br>{configuration["level"]}</div>'
        f'<div style="text-align:right">{game["remaining_attempts"]} left'
        f'<div class="cells" style="margin-left:auto;max-width:none">{cells}</div></div>'
        '</div>'
        f'<div class="lcd-caption">{caption}</div>'
        f'<div class="lcd-big">{big}</div>'
        f'<div class="lcd-feedback {feedback["kind"]}">{html.escape(feedback["text"])}</div>'
        '</div>'
        '<div class="lcd-brand"><span>Number machine</span><span>Power<i aria-hidden="true"></i></span></div>'
        '</div>'
    )


# Range scanner: the window shrinks with every hint
def range_bar(game):
    left = _pos(game['low'])
    width = max(_pos(game['high']) - left, 0.6)

    ticks = "".join(
        f'<span class="tick" style="left:{_pos(entry["guess"]):.2f}%"></span>'
        for entry in game['history'] if entry['type'] == 'guess'
    )
    if game['finished']:
        ticks += f'<span class="tick secret" style="left:calc({_pos(game["secret_number"]):.2f}% - 2px)"></span>'

    return (
        part_name("Range")
        + f'<div class="track" aria-label="Possible range {game["low"]} to {game["high"]}">'
        + f'<div class="window" style="left:{left:.2f}%;width:{width:.2f}%"></div>{ticks}</div>'
        + f'<div class="track-scale"><span>{min_num}</span><span>500</span><span>{max_num}</span></div>'
    )


# Hot/cold meter: five LEDs, one per heat level
LED_COLORS = ["#99B898", "#d8cf9c", "#FECEA8", "#FF847C", "#E84A5F"]


def heat_meter(game):
    entry = last_guess(game)
    if entry is None:
        label, lit = "No reading", 0
    else:
        label, lit = entry['heat'], max(1, round(entry['fill'] / 20))

    leds = "".join(
        f'<span class="led{" on" if i < lit else ""}" style="--c:{color}"></span>'
        for i, color in enumerate(LED_COLORS)
    )
    return (
        part_name("Heat")
        + '<div class="heat-row">'
        + f'<div class="heat-leds" role="img" aria-label="Heat: {label}">{leds}</div>'
        + f'<div class="heat-label">{label}</div></div>'
    )


# Guess history
def history(game):
    chips = []
    for entry in game['history']:
        if entry['type'] == 'hint':
            start, end = entry['block']
            chips.append(f'<span class="chip hint">hint {start}–{end}</span>')
        else:
            arrow = {'up': '↑', 'down': '↓', 'hit': '='}[entry['direction']]
            chips.append(f'<span class="chip {entry["direction"]}">{entry["guess"]} {arrow}</span>')

    body = "".join(chips) if chips else '<span class="empty-note">Your guesses show up here.</span>'
    return part_name("Your guesses") + f'<div class="chips">{body}</div>'


# Stat tiles
def stat_tiles(stats):
    tiles = [
        (stats['games'], "games played"),
        (f"{stats['win_rate']}%", "win rate"),
        (stats['best_score'], "best score"),
        (html.escape(str(stats['top_player'])), "top player")
    ]
    body = "".join(
        f'<div class="pearl stat"><div class="stat-value">{value}</div>'
        f'<div class="stat-name">{name}</div></div>'
        for value, name in tiles
    )
    return f'<div class="stats">{body}</div>'


# Retro table (names are escaped, they come from players)
def retro_table(df, numeric=()):
    head = "".join(
        f'<th class="{"num" if column in numeric else ""}">{html.escape(str(column))}</th>'
        for column in df.columns
    )
    rows = []
    for _, row in df.iterrows():
        cells = []
        for column in df.columns:
            value = row[column]
            if column == 'Result':
                cells.append(f'<td><span class="badge {str(value).lower()}">{html.escape(str(value))}</span></td>')
            elif column == 'Mode':
                cells.append(f'<td>{"Single" if value == "Single" else "Two players"}</td>')
            else:
                css_class = "num" if column in numeric else ""
                cells.append(f'<td class="{css_class}">{html.escape(str(value))}</td>')
        rows.append(f'<tr>{"".join(cells)}</tr>')

    return (f'<div class="pearl table-wrap"><table class="retro-table">'
            f'<thead><tr>{head}</tr></thead><tbody>{"".join(rows)}</tbody></table></div>')
