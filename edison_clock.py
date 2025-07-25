from datetime import datetime
import time
import os

import pyfiglet
from colorama import Fore, Style, init


def display_time():
    """Continuously display the current time in a style reminiscent of Edison bulbs."""
    init(autoreset=True)

    try:
        while True:
            now = datetime.now()
            # Format time as HH:MM:SS
            time_str = now.strftime('%H:%M:%S')
            # Render using the 'bulbhead' font which resembles vintage bulb lettering
            art = pyfiglet.figlet_format(time_str, font='bulbhead')

            # Clear the screen so the time updates in place
            os.system('cls' if os.name == 'nt' else 'clear')
            print(Fore.YELLOW + art + Style.RESET_ALL)
            time.sleep(1)
    except KeyboardInterrupt:
        # Allow graceful exit on Ctrl+C
        pass


if __name__ == '__main__':
    display_time()
