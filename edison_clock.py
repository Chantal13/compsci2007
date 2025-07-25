from datetime import datetime
import time

from colorama import Fore, Style, init
from pyfiglet import Figlet


def _render_colored_time(fig: Figlet, time_str: str, start_index: int) -> str:
    """Return the current time rendered in bulbhead font with cascading colors."""
    colors = [
        Fore.RED,
        Fore.YELLOW,
        Fore.GREEN,
        Fore.CYAN,
        Fore.BLUE,
        Fore.MAGENTA,
    ]

    # Generate ASCII art for each character with its own color
    ascii_chars = []
    for i, char in enumerate(time_str):
        color = colors[(start_index + i) % len(colors)]
        lines = fig.renderText(char).rstrip("\n").splitlines()
        lines = [color + line + Style.RESET_ALL for line in lines]
        ascii_chars.append(lines)

    # Combine characters horizontally
    height = len(ascii_chars[0])
    combined = []
    for row in range(height):
        combined.append("".join(char[row] for char in ascii_chars))

    return "\n".join(combined)


def display_time():
    """Continuously display the current time in rainbow Edison bulb style."""
    init(autoreset=True)
    fig = Figlet(font="bulbhead")

    index = 0
    try:
        while True:
            now = datetime.now()
            time_str = now.strftime("%H:%M:%S")

            print("\033[2J\033[H", end="")
            print(_render_colored_time(fig, time_str, index))

            index = (index + 1) % 6
            time.sleep(1)
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    display_time()
