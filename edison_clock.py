from datetime import datetime
import pyfiglet


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
