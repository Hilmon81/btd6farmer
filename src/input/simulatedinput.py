import keyboard
import mouse
from time import sleep
# Maybe add static in here somewhere?
def send_key( keybind, timeout=0.1, amount=1):
    """"""
    for _ in range(amount):
        keyboard.send(keybind)
        sleep(timeout)


def move_mouse(location, move_timeout=0.1):
    """"""
    mouse.move(x=location[0], y=location[1])
    sleep(move_timeout)


def click(location: tuple | tuple, amount=1, timeout=0.5, move_timeout=0.1, press_time=0.075):
    """"""
    """
    Method to click on a specific location on the screen
    @param location: The location to click on
    @param amount: amount of clicks to be performed
    @param timeout: time to wait between clicks
    @param move_timeout: time to wait between move and click
    @param press_time: time to wait between press and release
    """

    # If location is a string then assume that its a static button
    if isinstance(location, str):
        location = static.button_positions[location]
    
    # Move mouse to location
    self._move_mouse(self._scaling(location), move_timeout)

    for _ in range(amount):
        mouse.press(button='left')
        sleep(press_time) # https://www.reddit.com/r/AskTechnology/comments/4ne2tv/how_long_does_a_mouse_click_last/ TLDR; dont click too fast otherwise shit will break
        mouse.release(button='left')
        
        """
            We don't need to apply cooldown and slow down the bot on single clicks
            So we only apply the .1 delay if the bot has to click on the same spot multiple times
            This is currently used for level selection and levelup screen
        """
        if amount > 1:
            sleep(timeout)
    
        sleep(timeout)