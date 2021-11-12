"""Convert text(english) to morse code
and play morse code sound.
"""

# Standard Library import
from time import sleep

# Third party import
from vlc import MediaPlayer

# Local import
from assets import morse_rules


def play_sound(set_time_number: int):
    song = MediaPlayer('beep.mp3')
    song.play()
    song.set_time(set_time_number)
    sleep(0.5)


def play_morse(characters: "str"):
    for character in characters:
        if character == ".":
            play_sound(500)
        elif character == "-":
            play_sound(250)
        else:
            sleep(2)
    sleep(1)


text = input("Text: ").upper()
morse_codes = ""

for letter in text:
    letter_morse = morse_rules.get(letter, "")
    morse_codes += f"{letter_morse} "
    play_morse(letter_morse)


morse_code_style = morse_codes.replace(
    ".", "•").replace("-", "−").replace("  ", " |  ")
print(f"{text} : {morse_code_style}")
