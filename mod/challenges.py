"""
Challenges

- Kid-friendly challenges to do at home after losing a game
- Grouped by type: Move, Silly, Brain, Helper
- Random challenge (never the same one twice in a row)
- Safe on purpose: no climbing, spinning, food dares or anything with stairs
"""

import random


safety_note = "Clear a little space around you, and ask a grown-up if you're not sure about a challenge."

challenges = {
    'Move': [
        "Do 10 jumping jacks.",
        "Hop on one foot 5 times, then switch feet.",
        "Do 5 frog jumps across the room.",
        "Touch your toes 10 times.",
        "Freeze dance: dance for 20 seconds, then freeze like a statue.",
        "Walk like a crab for 5 steps.",
        "Do 15 arm circles forward and 15 backward.",
        "March in place for 30 seconds, knees up high.",
        "Do 5 bear crawl steps on hands and feet.",
        "Stretch up to the sky and count to 10."
    ],
    'Silly': [
        "Talk like a robot until the next game ends.",
        "Make your funniest face and hold it for 10 seconds.",
        "Sing 'Happy Birthday' in your tiniest whisper voice.",
        "Do your best impression of your favorite animal.",
        "Tell a joke to someone in the room.",
        "Pretend to be a statue for 20 seconds. No laughing!",
        "Say your next 3 sentences in a superhero voice.",
        "Walk like a penguin to the door and back.",
        "Invent a new dance move and give it a name."
    ],
    'Brain': [
        "Count backwards from 20 to 1, as fast as you can.",
        "Name 5 fruits in 10 seconds.",
        "Spell your name backwards.",
        "Find 3 things around you that are blue.",
        "Say the days of the week backwards.",
        "Name 5 animals that live in the ocean.",
        "Think of 3 words that rhyme with 'cat'.",
        "Count how many windows are in the room."
    ],
    'Helper': [
        "Put away 5 things that are out of place.",
        "Ask someone in your family for a high five.",
        "Fold 3 pieces of clothing.",
        "Drink a glass of water.",
        "Draw a quick picture and give it to someone.",
        "Say 3 nice things about someone in the room.",
        "Help set or clear the table at the next meal."
    ]
}


# All challenges in one list: [{'category': 'Move', 'text': '...'}, ...]
def all_challenges():
    return [{'category': category, 'text': text}
            for category, texts in challenges.items() for text in texts]


# Random challenge, different from the previous one
def random_challenge(previous=None):
    options = all_challenges()
    if previous in options and len(options) > 1:
        options.remove(previous)
    return random.choice(options)
