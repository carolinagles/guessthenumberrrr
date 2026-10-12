"""
Game Records

- Load game history from the Excel file
- Summary numbers and leaderboard by score
- Last 20 games
- Best/Worst players in bar chart
- Pie chart for wins/losses
"""
import pandas as pd
import matplotlib.pyplot as plt
from .settings import statistics_file, columns
from .game import calculate_score


# Load records
def load_statistics():
    try:
        df = pd.read_excel(statistics_file)
    except Exception:
        return pd.DataFrame(columns=columns + ['Score'])

    df = df[[column for column in columns if column in df.columns]]
    df = df.dropna(subset=['Name', 'Result'])
    if df.empty:
        return pd.DataFrame(columns=columns + ['Score'])

    df['Name'] = df['Name'].astype(str)
    df['Attempts'] = pd.to_numeric(df['Attempts'], errors='coerce').fillna(0).astype(int)
    df['Score'] = df.apply(
        lambda row: calculate_score(row['Difficulty'], row['Attempts'], row['Result']), axis=1)
    return df


# Summary numbers
def summary_stats(df):
    games = len(df)
    wins = (df['Result'] == 'Won').sum()
    win_rate = round(wins / games * 100) if games else 0
    best_score = int(df['Score'].max()) if games else 0

    top_player = "—"
    if games:
        totals = df.groupby('Name')['Score'].sum()
        top_player = totals.idxmax()

    return {'games': games, 'win_rate': win_rate, 'best_score': best_score, 'top_player': top_player}


# Leaderboard
def leaderboard(df, top=10):
    board = df.groupby('Name').agg(
        Games=('Result', 'count'),
        Wins=('Result', lambda results: (results == 'Won').sum()),
        Score=('Score', 'sum'),
        Best=('Score', 'max')
    )
    board['Win rate'] = (board['Wins'] / board['Games'] * 100).round().astype(int).astype(str) + "%"
    board = board.sort_values(['Score', 'Wins'], ascending=False).head(top).reset_index()
    board.insert(0, 'Rank', range(1, len(board) + 1))
    return board[['Rank', 'Name', 'Score', 'Wins', 'Games', 'Win rate', 'Best']]


# Last games
def last_games(df, n=20):
    return df.tail(n).iloc[::-1][['Date', 'Name', 'Mode', 'Difficulty', 'Attempts', 'Result', 'Score']]


# Chart look: transparent background, pearl plot area
def _rgb(values, alpha=1):
    return tuple(value / 255 for value in values) + (alpha,)


def _retro_axes(ax):
    ax.set_facecolor((1, 1, 1, 0.55))
    for side in ['top', 'right', 'left']:
        ax.spines[side].set_visible(False)
    ax.spines['bottom'].set_color('#1F2430')
    ax.tick_params(colors='#1F2430')
    ax.title.set_fontfamily('monospace')
    ax.title.set_fontweight('bold')


def player_performance(df, flavor):
    shell = _rgb(flavor['rgb'])
    deep = _rgb(flavor['deep'])

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4.6))
    fig.patch.set_alpha(0)

    # Top 10 players with most wins
    wins_count = df[df['Result'] == 'Won']['Name'].value_counts()
    if not wins_count.empty:
        wins_count.head(10).plot.bar(
            ax=ax1,
            title="Most Wins",
            color=[shell],
            edgecolor=[deep],
            linewidth=1.5
        )
        ax1.set_ylabel("Wins")
        ax1.set_xlabel("")
        ax1.tick_params(axis='x', rotation=45)
    else:
        ax1.text(0.5, 0.5, 'No wins recorded',
                 ha='center', va='center', transform=ax1.transAxes)
        ax1.set_title("Most Wins")

    # Top 10 players with most losses
    losses_count = df[df['Result'] == 'Lost']['Name'].value_counts()
    if not losses_count.empty:
        losses_count.head(10).plot.bar(
            ax=ax2,
            title="Most Losses",
            color=["#AEB6C1"],
            edgecolor=["#5A6270"],
            linewidth=1.5
        )
        ax2.set_ylabel("Losses")
        ax2.set_xlabel("")
        ax2.tick_params(axis='x', rotation=45)
    else:
        ax2.text(0.5, 0.5, 'No losses recorded',
                 ha='center', va='center', transform=ax2.transAxes)
        ax2.set_title("Most Losses")

    for ax in (ax1, ax2):
        _retro_axes(ax)
        plt.setp(ax.get_xticklabels(), ha='right')

    plt.tight_layout()
    return fig


# Pie charts
def games_pie_chart(df, flavor):
    color_map = {'Won': _rgb(flavor['rgb']), 'Lost': (0.93, 0.94, 0.95, 1)}
    fig, axes = plt.subplots(1, 3, figsize=(12, 3.8))
    fig.patch.set_alpha(0)

    groups = [
        ("All Games", df),
        ("Single Player Games", df[df['Mode'] == "Single"]),
        ("Two Player Games", df[df['Mode'] == "Double"])
    ]

    for ax, (title, data) in zip(axes, groups):
        counts = data['Result'].value_counts()
        if counts.empty:
            ax.text(0.5, 0.5, 'No games yet', ha='center', va='center', transform=ax.transAxes)
            ax.axis('off')
        else:
            counts.plot.pie(
                ax=ax,
                colors=[color_map.get(label, (0.7, 0.7, 0.7, 1)) for label in counts.index],
                autopct='%1.0f%%',
                startangle=90,
                wedgeprops={'edgecolor': _rgb(flavor['deep']), 'linewidth': 1.5},
                textprops={'fontfamily': 'monospace', 'color': '#1F2430'}
            )
            ax.set_ylabel('')
        ax.set_title(title, fontfamily='monospace', fontweight='bold', color='#1F2430')

    plt.tight_layout()
    return fig
