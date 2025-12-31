# Chord Symbol Formatting

## Overview

This project uses a **reusable, maintainable** approach to format chord symbols with properly spaced accidentals (flats and sharps) in ABC music notation.

## How It Works

1. **Write ABC files with simple notation**: Just use `"E♭m11"`, `"B♭7"`, `"F♯m"`, etc.
2. **Build automatically formats them**: The Makefile runs `format-lily-chords.py` after converting ABC to LilyPond
3. **Result**: Smaller, consistently formatted chord symbols with tight spacing around accidentals

## Usage

### In Your ABC Files

```abc
V: 1 clef=treble
| "Em11"[...] "E♭m11"[...] | "B♭7"[...] "F♯dim"[...] |
```

### Building

```bash
make          # Builds with automatic chord formatting
make clean    # Clean and rebuild from source
```

## The Solution

### Files

- **`format-lily-chords.py`**: Python script that formats chord symbols
  - Handles ANY chord (with or without accidentals)
  - Makes ALL chord names smaller
  - Adds tight spacing around ♭ and ♯ symbols

- **`Makefile`**: Automatically runs the script during build
  ```makefile
  %.ly: %.abc
      abc2ly $< -o $@
      ./format-lily-chords.py $@
  ```

### Customization

Edit `format-lily-chords.py` to adjust:
- Font size for all chords: `\\fontsize #-3` (lines 37, 47)
- Horizontal spacing around accidentals: `\\hspace #-0.15` (lines 38-39)

## Reusing in Other Projects

Copy these files to any ABC/LilyPond project:
1. `format-lily-chords.py` - The formatting script
2. The Makefile rule (lines 25-28)

That's it! Works with any chord notation.

## Why Not Pure LaTeX?

LilyPond renders music (including chord symbols) as graphics that get embedded in LaTeX. We can't use LaTeX macros for text inside those graphics. This Python script is the cleanest way to get professional formatting while keeping your ABC source files simple and readable.
