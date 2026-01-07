example
===============================================================================

This is an example of how to typeset music.


Install
-------------------------------------------------------------------------------

On MacOS:

```
brew install lilypond
brew install abc2ly
brew install pandoc
brew install pandoc-crossref
```

On Ubuntu:

```
sudo apt install lilypond
sudo apt install abc2ly
sudo apt install pandoc
sudo apt install pandoc-crossref
```


Usage
-------------------------------------------------------------------------------

This project is an example of how to typeset music in markdown/abc and
compile it to pdf via pandoc/latex/lilypond.

You edit a top markdown file: `example.md` and the included abc music files: `tune*.abc`.

Calling `make` builds: markdown → lytex → tex → pdf.


Links
-------------------------------------------------------------------------------

Typesetting:

-   [abcnotation.com](https://abcnotation.com/)
-   [lilypond.org](https://lilypond.org/)

Wikipedia:

-   [ABC notation](https://en.wikipedia.org/wiki/ABC_notation)
-   [LilyPond](https://en.wikipedia.org/wiki/LilyPond)


Author
-------------------------------------------------------------------------------

Ryan Reece ([@rreece](https://github.com/rreece))       
Created: December 30, 2025      

