# Edison Clock

This repository contains a small Python script that prints the current time
using an Edison bulb style font. The program relies on the `pyfiglet` library
and uses the `bulbhead` font to mimic a vintage bulb display.

## Requirements

- Python 3
- `pyfiglet` Python package

Install `pyfiglet` with pip if necessary:

```bash
pip install pyfiglet
```

## Usage

Run the script from the command line:

```bash
python3 edison_clock.py
```

The output will show the current time in large, bulb-styled letters.

## Checking Asset Suite 9 Documents

The repository also includes a utility to validate document IDs against an Asset Suite 9 instance using a list stored in an Excel file.

### Additional Requirements

- `openpyxl`
- `requests`

Install these packages if they are not available:

```bash
pip install openpyxl requests
```

### Usage

Provide the Excel file (document IDs in column A) and the API credentials for your Asset Suite 9 deployment:

```bash
python3 check_documents.py documents.xlsx --url <AS9_API_URL> --key <AS9_API_KEY> -o results.xlsx
```

The script will write a second column indicating whether each document was found ("FOUND" or "MISSING").
