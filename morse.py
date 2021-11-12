"""Convert text(english) to morse code
and play morse code sound.
"""

# Standard Library import
from time import sleep

# Third party import
from vlc import MediaPlayer

# Local import
from assets import morse_rules


def play_sound(characters: "str"):
    pass


text = input("Text: ").upper()
morse_code = ""

for letter in text:
    pass

play_sound(morse_code)

morse_code_style = morse_code.replace(".", "•").replace("-", "−")
print(f"{text} : {morse_code_style}")
