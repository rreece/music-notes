# Makefile for LaTeX documents with ABC music notation

# Main document (without extension)
MAIN = document

# Find all ABC files
ABC_FILES = $(wildcard *.abc)

# Generate corresponding .ly filenames
LY_FILES = $(ABC_FILES:.abc=.ly)

# Final output
PDF = $(MAIN).pdf

# LilyPond working directory
LILY_DIR = lily-tmp

# Default target
all: $(PDF)

# Convert ABC to LilyPond
%.ly: %.abc
	abc2ly $< -o $@

# Process LilyPond snippets in LaTeX
$(MAIN).tex: $(MAIN).lytex $(LY_FILES)
	lilypond-book --output=. --pdf --lily-output-dir=$(LILY_DIR) $(MAIN).lytex

# Compile LaTeX to PDF
$(PDF): $(MAIN).tex
	pdflatex $(MAIN)
	pdflatex $(MAIN)  # Run twice for references

# Clean intermediate files
clean:
	rm -f $(LY_FILES)
	rm -f $(MAIN).tex
	rm -f *.aux *.log *.out
	rm -f $(MAIN).dep
	rm -f tmp-*.pdf tmp-*.eps tmp-*.ly
	rm -rf $(LILY_DIR)/
	rm -rf out-www/
	rm -rf [0-9a-f][0-9a-f]/

# Clean everything including final PDF
cleanall: clean
	rm -f $(PDF)

# Phony targets
.PHONY: all clean cleanall
