#!/bin/sh

# JDR: This script compiles slides-class.tex, slides-mine.tex, slides-blank.tex,
# and slides-web.tex, and moves them to daily/MM-DD-slides-(blah).pdf, where
# MM-DD is the date set in the beginning of slides.tex.

date=$(grep \\\\lecturedate slides.tex | head -n 1 | cut -c 18-22)

latex () {
    pdflatex $1 && pdflatex $1 || exit 1
    mv $1.pdf daily/$date-$1.pdf
}

latex slides-class
latex slides-mine
latex slides-blank
latex slides-web
