from datetime import datetime

try:
    import pyfiglet
except ImportError as e:  # pragma: no cover - simple import guard
    raise SystemExit(
        "pyfiglet is required to run this program.\n" "Install it with 'pip install pyfiglet'."
    ) from e


def display_time():
    """Display the current time in a style reminiscent of Edison bulbs."""
    now = datetime.now()
    # Format time as HH:MM:SS
    time_str = now.strftime('%H:%M:%S')
    # Render using the 'bulbhead' font which resembles vintage bulb lettering
    art = pyfiglet.figlet_format(time_str, font='bulbhead')
    print(art)


if __name__ == '__main__':
    display_time()
