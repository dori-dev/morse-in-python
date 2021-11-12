"""Project functions
"""

# Standard Library import
from time import sleep

# Third party import
from vlc import MediaPlayer


def play_sound(set_time_number: int):
    """play beep sound with time number

    Args:
        set_time_number (int): set time number
    """
    song = MediaPlayer('beep.mp3')
    song.play()
    song.set_time(set_time_number)
    sleep(0.5)


def play_morse(characters: "str"):
    """play morse sound

    Args:
        characters (str): characters of a letter
    """
    for character in characters:
        if character == "•":
            play_sound(500)
        elif character == "−":
            play_sound(250)
        else:
            sleep(1)
    sleep(0.5)
