"""
Guess the Number (1-1000) - Streamlit App

- Two game modes: single player or two players
- Three difficulty levels
- Range scanner, hot/cold meter and one hint per game
- Random kid-friendly challenge when you lose
- Score, game history recording and results visualization
- Liquid glass shell in four palette colors, WordArt title

Run:
streamlit run app.py
"""

import streamlit as st
from mod.settings import (difficulty, flavors, min_num, max_num, hint_cost,
                          background_gif, background_light)
from mod.game import (new_game, validate_secret, play_turn, use_hint, can_use_hint,
                      attempts_used, game_score, save_record)
from mod.records import (load_statistics, summary_stats, leaderboard, last_games,
                         player_performance, games_pie_chart)
from mod.challenges import challenges, safety_note, random_challenge
from mod.style import inject_style
from mod import ui


st.set_page_config(page_title="Guess the Number", layout="centered")

# Session state
defaults = {'game': None, 'page': "Play", 'flavor': "Salmon",
            'mode_choice': "Single", 'level_choice': '2',
            'setup_error': None, 'save_error': None,
            'challenge': None}
for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value

flavor = flavors[st.session_state.flavor]
inject_style(flavor, background_gif, background_light)


# Callbacks (run before the screen is drawn, so the LCD is always up to date)
def start_game():
    mode = st.session_state.get('mode_choice') or "Single"
    level_key = st.session_state.get('level_choice') or '2'
    secret_number = None

    if mode == "Double":
        secret_number, error = validate_secret(st.session_state.get('secret_input', ""))
        if error:
            st.session_state.setup_error = error
            return

    st.session_state.game = new_game(mode, level_key, secret_number)
    st.session_state.challenge = None
    st.session_state.secret_input = ""
    st.session_state.setup_error = None
    st.session_state.save_error = None


def submit_guess():
    play_turn(st.session_state.game, st.session_state.get('guess_input'))


def request_hint():
    use_hint(st.session_state.game)


def quit_game():
    st.session_state.game = None


def save_game():
    game = st.session_state.game
    ok, error = save_record(st.session_state.get('player_name', ""), game['mode'],
                            game['configuration'], attempts_used(game), game['guessed'])
    game['saved'] = ok
    st.session_state.save_error = error


def pick_challenge():
    st.session_state.challenge = random_challenge(st.session_state.challenge)


def go_to_records():
    st.session_state.game = None
    st.session_state.page = "Records"


# Header and menus
st.markdown(ui.bezel(), unsafe_allow_html=True)

menu_col, color_col = st.columns([1, 1.25], vertical_alignment="bottom")
with menu_col:
    st.segmented_control("Menu", ["Play", "Records", "Challenges", "Rules"], key="page",
                         required=True, label_visibility="collapsed")
with color_col:
    st.segmented_control("Shell color", list(flavors), key="flavor", required=True,
                                                  help="Change the shell color", label_visibility="collapsed")


# Play: setup screen
def setup_screen():
    st.markdown(ui.part_name("Mode"), unsafe_allow_html=True)
    st.segmented_control("Mode", ["Single", "Double"], key="mode_choice", required=True,
                         format_func=lambda mode: "Single player" if mode == "Single" else "Two players",
                         label_visibility="collapsed")

    st.markdown(ui.part_name("Difficulty"), unsafe_allow_html=True)
    st.segmented_control("Difficulty", list(difficulty), key="level_choice", required=True,
                         format_func=lambda key: f"{difficulty[key]['level']} ({difficulty[key]['attempts']})",
                         label_visibility="collapsed")

    if st.session_state.mode_choice == "Double":
        st.markdown(ui.part_name("Player 1"), unsafe_allow_html=True)
        st.text_input(f"Think of the number you want the second player to guess ({min_num}-{max_num})",
                      key="secret_input", type="password", placeholder="Type it where player 2 can't see")

    if st.session_state.setup_error:
        st.error(st.session_state.setup_error)

    st.write("")
    st.button("Start game", type="primary", on_click=start_game, width="stretch")


# Play: game screen
def game_screen(game):
    st.markdown(ui.lcd(game), unsafe_allow_html=True)

    if not game['finished']:
        with st.form("guess_form", clear_on_submit=True, border=False):
            input_col, button_col = st.columns([3, 1], vertical_alignment="bottom")
            input_col.number_input("Your guess", min_value=min_num, max_value=max_num, value=None,
                                   step=1, key="guess_input", placeholder=f"{min_num} – {max_num}",
                                   label_visibility="collapsed")
            button_col.form_submit_button("Guess", type="primary", on_click=submit_guess, width="stretch")

        hint_col, quit_col = st.columns(2)
        hint_col.button(f"Hint (costs {hint_cost})", on_click=request_hint,
                        disabled=not can_use_hint(game), width="stretch",
                        help="Shows which hundred the number is in. One per game.")
        quit_col.button("Quit game", on_click=quit_game, width="stretch")

    else:
        # Lost: random challenge to do at home
        if not game['guessed']:
            st.markdown(ui.part_name("Lost? Time for a challenge"), unsafe_allow_html=True)
            if st.session_state.challenge:
                st.markdown(ui.challenge_card(st.session_state.challenge, safety_note), unsafe_allow_html=True)
            label = "Another challenge" if st.session_state.challenge else "Random challenge"
            st.button(label, on_click=pick_challenge, width="stretch",
                      type="secondary" if st.session_state.challenge else "primary")

        if not game['saved']:
            label = "Enter your name" if game['mode'] == "Single" else "Name of the player who guessed"
            st.text_input(label, key="player_name", max_chars=24)
            save_col, again_col = st.columns(2)
            save_col.button("Save game", type="primary", on_click=save_game, width="stretch")
            again_col.button("Play again", on_click=quit_game, width="stretch")
            if st.session_state.save_error:
                st.error(st.session_state.save_error)
        else:
            st.success(f"Game saved. Score: {game_score(game)}")
            again_col, records_col = st.columns(2)
            again_col.button("Play again", type="primary", on_click=quit_game, width="stretch")
            records_col.button("See records", on_click=go_to_records, width="stretch")

    st.markdown(ui.range_bar(game) + ui.heat_meter(game) + ui.history(game), unsafe_allow_html=True)


# Records screen
def records_screen():
    df = load_statistics()
    if df.empty:
        st.info("No games saved yet. Play one and save it to start the records.")
        return

    level = st.segmented_control("Difficulty filter", ["All", "Easy", "Medium", "Hard"],
                                 default="All", required=True, key="records_level",
                                 label_visibility="collapsed")
    if level != "All":
        df = df[df['Difficulty'] == level]
    if df.empty:
        st.info(f"No {level} games saved yet.")
        return

    st.markdown(ui.stat_tiles(summary_stats(df)), unsafe_allow_html=True)

    st.markdown(ui.part_name("Leaderboard by score"), unsafe_allow_html=True)
    st.markdown(ui.retro_table(leaderboard(df), numeric=('Rank', 'Score', 'Wins', 'Games', 'Win rate', 'Best')),
                unsafe_allow_html=True)

    st.markdown(ui.part_name("Last 20 games"), unsafe_allow_html=True)
    st.markdown(ui.retro_table(last_games(df), numeric=('Attempts', 'Score')), unsafe_allow_html=True)

    st.markdown(ui.part_name("Player performance"), unsafe_allow_html=True)
    st.pyplot(player_performance(df, flavor))

    st.markdown(ui.part_name("Games won or lost"), unsafe_allow_html=True)
    st.pyplot(games_pie_chart(df, flavor))


# Challenges screen
def challenges_screen():
    st.markdown(ui.part_name("Random challenge"), unsafe_allow_html=True)
    if st.session_state.challenge:
        st.markdown(ui.challenge_card(st.session_state.challenge, safety_note), unsafe_allow_html=True)
    st.button("Random challenge", type="primary", on_click=pick_challenge, width="stretch")

    st.markdown(ui.part_name("All challenges"), unsafe_allow_html=True)
    st.markdown(f'<p>Lose a game and you get one of these. {safety_note}</p>', unsafe_allow_html=True)
    st.markdown(ui.challenge_list(challenges), unsafe_allow_html=True)


# Rules screen
def rules_screen():
    rows = "".join(
        f"<tr><td>{config['level']}</td><td class='num'>{config['attempts']}</td>"
        f"<td class='num'>{config['base']}</td><td class='num'>+{config['bonus']}</td></tr>"
        for config in difficulty.values()
    )
    st.markdown(
        '<div class="pearl rules">'
        f"<p>The machine hides a number from {min_num} to {max_num}. After every attempt it tells you "
        "to go higher or lower, and the range bar shrinks to show what's left.</p>"
        "<p>The heat meter shows how close your last guess was, from Freezing to Burning. "
        f"Once per game you can ask for a hint: it shows which hundred the number is in "
        f"and costs {hint_cost} attempt. Repeated or out-of-range guesses don't use attempts.</p>"
        "<p>In two player mode, player 1 types the secret number hidden, then hands over to player 2.</p>"
        "<p>If you lose, press Random challenge and do a quick challenge at home: "
        "moving, silly, brain or helper challenges, all safe for kids.</p>"
        '</div>'
        '<div class="pearl table-wrap"><table class="retro-table"><thead><tr>'
        "<th>Difficulty</th><th class='num'>Attempts</th><th class='num'>Win points</th>"
        "<th class='num'>Per attempt left</th></tr></thead>"
        f"<tbody>{rows}</tbody></table></div>",
        unsafe_allow_html=True
    )


# Main menu
if st.session_state.page == "Play":
    if st.session_state.game is None:
        setup_screen()
    else:
        game_screen(st.session_state.game)
elif st.session_state.page == "Records":
    records_screen()
elif st.session_state.page == "Challenges":
    challenges_screen()
else:
    rules_screen()
