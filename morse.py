"""Convert text(english) to morse code
and play morse code sound.
"""

# Standard Library import
from time import sleep

# Third party import
from vlc import MediaPlayer

# Local import
from assets import morse_rules


def play_sound(time_left: int):
    song = MediaPlayer('beep.mp3')
    song.play()
    song.set_time(time_left)
    sleep(0.2)


def play_morse(characters: "str"):
    for character in characters:
        if character == ".":
            play_sound(300)
        elif character == "-":
            play_sound(800)
        else:
            sleep(2)
    sleep(0.5)


text = input("Text: ").upper()
morse_codes = ""

for letter in text:
    morse_codes += morse_rules.get(letter, " ")

play_morse(morse_codes)

morse_code_style = morse_codes.replace(
    ".", "•").replace("-", "−").replace(" ", " |  ")
print(f"{text} : {morse_code_style}")
