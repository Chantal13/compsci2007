# Edison Clock

This repository contains a small Python script that prints the current time in
an Edison bulb style ASCII art. Each digit appears in a different color that
cascades like a rainbow and refreshes every second. The program relies on the
`pyfiglet` and `colorama` libraries for the styled, colored output.

## Requirements

- Python 3
- `pyfiglet` Python package
- `colorama` Python package

Install the required packages with pip if necessary:

```bash
pip install pyfiglet colorama
```

## Usage

Run the script from the command line:

```bash
python3 edison_clock.py
```

The output will show the current time in large bulb-styled letters that update
every second. The digits cycle through rainbow colors as the clock refreshes.
Press `Ctrl+C` to exit.
