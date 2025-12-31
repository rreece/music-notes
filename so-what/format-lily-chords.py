#!/usr/bin/env python3
"""
Format chord symbols in LilyPond files with superscript accidentals.
Handles any chord with flats (♭) or sharps (♯).
"""

import sys
import re

def format_chord_with_accidental(match):
    """Format a chord name with superscript flat or sharp."""
    chord_name = match.group(1)

    # Pattern to find accidental and split the chord
    # Matches: note + accidental + rest of chord
    accidental_pattern = r'^([A-G])(♭|♯|b|#)(.*)$'
    acc_match = re.match(accidental_pattern, chord_name)

    if not acc_match:
        return match.group(0)  # No accidental, return unchanged

    note = acc_match.group(1)
    accidental = acc_match.group(2)
    rest = acc_match.group(3)

    # Normalize accidental symbols
    if accidental in ('b', '♭'):
        acc_symbol = '♭'
    elif accidental in ('#', '♯'):
        acc_symbol = '♯'
    else:
        acc_symbol = accidental

    # Build the LilyPond markup (no superscript)
    formatted = (
        f'^\\markup \\fontsize #-3 {{ '
        f'\\concat {{ {note} \\hspace #-0.15 '
        f'{acc_symbol} '
        f'\\hspace #-0.15 {rest} }} }}'
    )

    return formatted

def format_regular_chord(match):
    """Format a regular chord name (no accidentals) with smaller font."""
    chord_name = match.group(1)
    return f'^\\markup \\fontsize #-3 {{ {chord_name} }}'

def process_file(filepath):
    """Process a LilyPond file to format chord symbols."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # First, replace chord symbols WITH accidentals (with superscript formatting)
    # Matches ^"ChordName" where ChordName contains accidentals
    pattern_with_accidental = r'\^"([A-G][♭♯b#][^"]*)"'
    content = re.sub(pattern_with_accidental, format_chord_with_accidental, content)

    # Then, replace remaining regular chord symbols (just smaller font)
    # Matches ^"ChordName" where ChordName is just letters/numbers (no accidentals)
    pattern_regular = r'\^"([A-G][^"♭♯b#]*)"'
    content = re.sub(pattern_regular, format_regular_chord, content)

    # Add global chord name font size if not present
    if 'ChordName.font-size' not in content:
        content = re.sub(
            r'(\\time 4/4 \\key c \\major)',
            r'\1 \\override ChordName.font-size = #-3',
            content
        )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file.ly>")
        sys.exit(1)

    process_file(sys.argv[1])
