
# Materials for Core Linear Algebra at Georgia Tech

## Getting Started

### Downloading

Make sure you have a recent version of TeXLive / MacTeX installed (2015+).  Earlier versions will not compile some of the figures.

If you're comfortable with git, just clone this repository.

If not, you can always download the latest version [here](https://github.com/QBobWatson/ref-155x/archive/master.zip)

### Overview

The slides are written in [Beamer](http://ctan.org/pkg/beamer).  Figures are written in [TikZ](http://ctan.org/pkg/pgf).  All materials use several of my style files (in `style/`):
* `jdr-macros.sty`: My generic LaTeX macros.
* `jdr-tikz.sty`: My TikZ extensions (in particular, facilities for 3D plots).
* `jdr-linalg.sty`: Macros common to the slides and other materials.
* `jdr-hwexam.sty`: Macros for quizzes, exams, etc.
* `jdr-style.sty`: Configures fonts, theorem environments, etc. for some material (not slides).
* `spalign.sty`: My [package](http://ctan.org/pkg/spalign) for quickly typesetting matrices.  (Should be included in TeXLive 2017+.)
These are included automatically.

Most of the macros specific to the slides are defined in `slides.tex`.  The code has some documentation, but it's easiest to just look through the slides to find examples of how things work.

### Contents

This is a description of the included files.
* `slides*.tex`: Base files for compiling slides.
* `slides/*`: Slides content.
* `announcements.tex`: Announcements get compiled into certain slides.
* `compile.sh` (also `autogen.py`): Automation for compiling slides.
* `daily/`: The `compile.sh` script puts it output here.
* `slides-pdf/*`: Compiled versions of the current reference slides (`class` and `web` modes).
* `figures/*`: Figures used in the materials.
* `style/*`: Style files used for compiling the materials.
* `reference.tex`: Reference sheet for definitions, theorems, etc.  Students love this.

## Slides

The slides are written 

Slides have `webonly`-mode material, which is meant to be worked on a blackboard or written on the slide (using an iPad or something) during lecture.  This is handled differently, depending on the [compile mode](#compile-modes).

If you have two projectors, *use them both*!  Some of the lectures are designed to refer back to previous slides from the same lecture.

### Compile Modes

Slides can be compiled in one of five modes:
* `texing`: This is what happens when you compile `slides.tex`.  It compiles in `presentation` mode, with `webonly` material rendered semi-transparent.  This is useful when you're actively working on the slides.
* `class`: This is what happens when you compile `slides-class.tex`.  It compiles in `presentation` mode, with `webonly` material blanked out.  This is meant for in-class slides.

* why I included proofs
* explain webonly and compile modes
* compile twice
* autogen
* procedures for doing slides
