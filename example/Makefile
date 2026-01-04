# Main document (without extension)
MAIN = example

# Source files
MD_FILE = $(MAIN).md
META_FILE = meta.yaml
LYTEX_FILE = $(MAIN).lytex

# Find all ABC files
ABC_FILES = $(wildcard *.abc)

# Generate corresponding .ly filenames
LY_FILES = $(ABC_FILES:.abc=.ly)

# Final output
PDF = $(MAIN).pdf

# Default target
all: $(PDF)

# Convert markdown to lytex using pandoc
$(LYTEX_FILE): $(MD_FILE) $(META_FILE)
	pandoc $(MD_FILE) $(META_FILE) -o $(LYTEX_FILE) --standalone --from markdown --to latex --filter pandoc-crossref

# Convert ABC to LilyPond
%.ly: %.abc
	abc2ly $< -o $@

# Process LilyPond snippets in LaTeX
$(MAIN).tex: $(LYTEX_FILE) $(LY_FILES)
	lilypond-book --output=. --pdf $(LYTEX_FILE)

# Compile LaTeX to PDF
$(PDF): $(MAIN).tex
	pdflatex $(MAIN)
	pdflatex $(MAIN)  # Run twice for references

# Clean intermediate files
clean:
	rm -f $(LY_FILES)
	rm -f $(LYTEX_FILE)
	rm -f $(MAIN).tex $(MAIN).dep
	rm -f *.aux *.log *.out
	rm -f lock
	rm -f tmp*.pdf
	rm -f snippet-*
	rm -rf [0-9a-f][0-9a-f]/

# Clean everything including final PDF
cleanall: clean
	rm -f $(PDF)

# Phony targets
.PHONY: all clean cleanall
