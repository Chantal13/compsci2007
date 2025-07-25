# Edison Clock

This repository contains a small Python script that prints the current time in
an Edison bulb style font. Each digit is displayed in a cascading rainbow of
colors that refreshes every second.

## Requirements

- Python 3
- `colorama` Python package
- `pyfiglet` Python package

Install the required packages with pip if necessary:

```bash
pip install colorama pyfiglet
```

## Usage

Run the script from the command line:

```bash
python3 edison_clock.py
```

The output will show the current time in a colored "bulbhead" font that
refreshes every second. Press `Ctrl+C` to exit.
