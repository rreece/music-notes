# Makefile for LaTeX documents with ABC music notation

# Main document (without extension)
MAIN = example

# Find all ABC files
ABC_FILES = $(wildcard *.abc)

# Generate corresponding .ly filenames
LY_FILES = $(ABC_FILES:.abc=.ly)

# Final output
PDF = $(MAIN).pdf

# Default target
all: $(PDF)

# Convert ABC to LilyPond
%.ly: %.abc
	abc2ly $< -o $@

# Process LilyPond snippets in LaTeX
$(MAIN).tex: $(MAIN).lytex $(LY_FILES)
	lilypond-book --output=. --pdf $(MAIN).lytex

# Compile LaTeX to PDF
$(PDF): $(MAIN).tex
	pdflatex $(MAIN)
	pdflatex $(MAIN)  # Run twice for references

# Clean intermediate files
clean:
	rm -f $(LY_FILES)
	rm -f $(MAIN).tex $(MAIN).dep
	rm -f *.aux *.log *.out
	rm -r lock
	rm -rf [0-9a-f][0-9a-f]/

# Clean everything including final PDF
realclean: clean
	rm -f $(PDF)

# Phony targets
.PHONY: all clean realclean
