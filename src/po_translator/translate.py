#!/usr/bin/env python3

import argparse
import polib
import subprocess
import arabic_reshaper
import os
from tqdm import tqdm
import shutil

from bidi.algorithm import get_display

def translate_po_file(input_pot, output_po, target_language='ar', verbose=False):
    # TODO: check function documentation
    """
    Translate a .pot file to a target language using translate-shell.
    
    Args:
        input_pot (str): Path to input .pot file
        output_po (str, optional): Path to output .po file. Defaults to '<input>-<language>.po'.
        target_language (str, optional): Target language code. Defaults to 'ar'.
    """
    # Load the .pot file
    pot_entries = polib.pofile(input_pot)
    po_entries = polib.POFile()
    
    # Set metadata
    po_entries.metadata = pot_entries.metadata
    
    for entry in tqdm(pot_entries,desc="Translating", unit="entries"):
        if entry.msgstr == "":
            # Call translate-shell for translation
            try:
                translation = subprocess.run(
                    ['trans', '-b', f':{target_language}', entry.msgid],
                    capture_output=True, text=True, check=True
                ).stdout.strip()
                
                # Reshape and display Arabic text
                if target_language == 'ar':
                    reshaped_translation = arabic_reshaper.reshape(translation)
                    displayed_translation = get_display(reshaped_translation)
                else:
                    displayed_translation = translation
                
                # Set the translated string
                entry.msgstr = displayed_translation
            except subprocess.CalledProcessError as e:
                print(f"Translation failed for: {entry.msgid}")
                print(f"Error: {e}")
                entry.msgstr = entry.msgid  # Fallback to original text
            if verbose:
               reshaped_msgstr = get_display(arabic_reshaper.reshape(entry.msgstr)) if target_language == 'ar' else entry.msgstr
               print(f"{entry.msgid} -> {reshaped_msgstr}")
        
        else:
            if verbose:
                reshaped_msgstr = get_display(arabic_reshaper.reshape(entry.msgstr)) if target_language == 'ar' else entry.msgstr
                print(f"Translation for {entry.msgid} already exists! {reshaped_msgstr}")
                
                
        # Add entry to PO file
        po_entries.append(entry)
    
    # Save as .po file
    po_entries.save(output_po)
    print(f"Translation complete! Saved as {output_po}")

def main():
    """
    Command-line interface for PO file translation.
    """
     
    parser = argparse.ArgumentParser(description='Translate PO/POT files')
    parser.add_argument('input', help='Input .pot file path')
    parser.add_argument('output', help='Output .po file path (default: <input>-<language>.po)', nargs='?')
    parser.add_argument('-l', '--language', default='ar', 
                        help='Target language code (default: ar)')
    parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output: shows each translation')
    parser.add_argument('--version', action='version', version='%(prog)s 1.0')
    args = parser.parse_args()
    
    
    if not shutil.which('trans'):
        print("Error: 'trans' command-line tool is not installed. Please install it and try again.")
        exit(1)

    
    if not os.path.isfile(args.input):
        print(f"Error: Input file '{args.input}' does not exist.")
        exit(1)
    
    if not args.output:
        args.output = f"{args.input}-{args.language}.po"
    translate_po_file(args.input, args.output, args.language, args.verbose)

if __name__ == '__main__':
    main()