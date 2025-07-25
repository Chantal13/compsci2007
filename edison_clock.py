from datetime import datetime
import time

from colorama import Fore, Style, init
import pyfiglet

COLORS = [
    Fore.RED,
    Fore.YELLOW,
    Fore.GREEN,
    Fore.CYAN,
    Fore.BLUE,
    Fore.MAGENTA,
]


def render_colored_time(time_str: str, offset: int) -> str:
    """Return the bulb-style time string with cascading rainbow colors."""
    fig = pyfiglet.Figlet(font="bulbhead")
    char_art = [fig.renderText(ch).splitlines() for ch in time_str]
    height = len(char_art[0])
    lines = []
    for row in range(height):
        parts = []
        for i, art_lines in enumerate(char_art):
            color = COLORS[(i + offset) % len(COLORS)]
            parts.append(color + art_lines[row] + Style.RESET_ALL)
        lines.append("".join(parts))
    return "\n".join(lines)


def display_time():
    """Display the current time in a rainbow Edison bulb style."""
    init(autoreset=True)
    offset = 0

    try:
        while True:
            now = datetime.now()
            time_str = now.strftime("%H:%M:%S")
            art = render_colored_time(time_str, offset)
            print("\033[H\033[J" + art, end="", flush=True)
            time.sleep(1)
            offset = (offset + 1) % len(COLORS)
    except KeyboardInterrupt:
        print()


if __name__ == '__main__':
    display_time()
