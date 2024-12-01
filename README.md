# PO File Translator

A command-line tool for translating PO (Portable Object) files using translate-shell.
It is free, straightforward, no api key needed and unlimited translations

## Features

- Translate PO/POT files to target languages
- Easy command-line interface

## Prerequisites

- Python 3.7+
- translate-shell installed (`apt-get install translate-shell` on Ubuntu)

## Installation

```bash
pip install .
```

## Usage

```bash
# Basic usage
po-translate input.pot

# Specify output file name
po-translate input.pot ar.po

# Specify a different language
po-translate input.pot es.po -l es

# Observe each translation
po-translate input.pot --verbose

```

## Command-line Options

- `input`: Path to the input .pot file (required)
- `output`: Path to the output .po file (optional, default: <input>-<language>.po)
- `-l, --language`: Target language code (default: ar)
- `-h, --help`: show a brief help on how to use the tool
- `-v, --verbose`: output each translation to the stdout

## Dependencies

- polib
- arabic-reshaper
- python-bidi

## Limitations

- Requires translate-shell to be installed
- Translation quality depends on the translate-shell service

