from datetime import datetime
import time

import pyfiglet
from colorama import Fore, Style, init


def display_time():
    """Show an updating time display in a colored Edison bulb style."""
    init(autoreset=True)

    colors = [
        Fore.RED,
        Fore.YELLOW,
        Fore.GREEN,
        Fore.CYAN,
        Fore.BLUE,
        Fore.MAGENTA,
    ]
    shift = 0

    try:
        while True:
            now = datetime.now()
            time_str = now.strftime('%H:%M:%S')

            char_lines = [
                pyfiglet.figlet_format(ch, font="bulbhead").rstrip().split("\n")
                for ch in time_str
            ]
            height = len(char_lines[0])
            lines = []
            for row in range(height):
                line = ""
                for idx, art in enumerate(char_lines):
                    color = colors[(idx + shift) % len(colors)]
                    line += color + art[row] + Style.RESET_ALL
                lines.append(line)

            print("\033[H\033[J", end="")  # Clear screen
            print("\n".join(lines), flush=True)

            shift = (shift + 1) % len(colors)
            time.sleep(1)
    except KeyboardInterrupt:
        # Move to a new line on exit for clean terminal
        print()


if __name__ == '__main__':
    display_time()
