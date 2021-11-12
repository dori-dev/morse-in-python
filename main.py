"""Convert text(english) to morse code
and play morse code sound.
"""

# Local import
from assets import morse_rules
from functions import play_morse


text = input("Text: ").upper()
morse_codes = []
for letter in text:
    letter_morse = morse_rules.get(letter, "")
    if letter_morse:
        morse_codes.append(letter_morse)

print(f"{text} : {' '.join(morse_codes)}")

for letter in morse_codes:
    play_morse(letter)
