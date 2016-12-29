
# Materials for Core Linear Algebra at Georgia Tech

## Getting Started

### Downloading

Make sure you have a recent version (2015+) of TeXLive / MacTeX installed.  Earlier versions will not compile some of the figures.

If you're comfortable with git, just clone this repository.

If not, you can always download the latest version as a ZIP file [here](https://github.com/QBobWatson/ref-155x/archive/master.zip).

### Overview

The slides are written in [Beamer](http://ctan.org/pkg/beamer).  Figures are written in [TikZ](http://ctan.org/pkg/pgf).  All materials use several of my style files (in `style/`):
* `jdr-macros.sty`: My generic LaTeX macros.
* `jdr-tikz.sty`: My TikZ extensions (in particular, facilities for 3D plots).
* `jdr-linalg.sty`: Macros common to the slides and other materials.
* `jdr-hwexam.sty`: Macros for quizzes, exams, etc.
* `jdr-style.sty`: Configures fonts, theorem environments, etc. for some material (not slides).
* `spalign.sty`: My [package](http://ctan.org/pkg/spalign) for quickly typesetting matrices.  (Should be included in TeXLive 2017+.)

These files are included automatically.

Most of the macros specific to the slides are defined in `slides.tex`.  The code has some documentation, but it's easiest to just look through the slides to find examples of how things work.

### Contents

This is a description of the included files.
* `slides*.tex`: Base files for compiling slides.
* `slides/*`: Slides content.
* `announcements.tex`: Announcements get compiled into certain slides.
* `compile.sh` (also `autogen.py`): Automation for compiling slides.
* `daily/`: The `compile.sh` script puts its output here.
* `slides-pdf/*`: Compiled versions of the current reference slides (`class` and `web` modes).
* `figures/*`: Figures used in the materials.
* `style/*`: Style files used for compiling the materials.
* `reference.tex`: Reference sheet for definitions, theorems, etc.  Students love this.

## Slides

The slides are written to be presented on a projector, but with most examples, proofs, etc. worked out on a blackboard.  (Really it's best if you have *two* projectors, so you can present the current slide while referring to a previous slide.)

To facilitate this, slides have a `webonly` mode, implemented as a `\begin{webonly}...\end{webonly}` environment, and a command `\webonlycmd{...}`.  This is for material that is meant to be worked on a blackboard or written on the slide (using an iPad or something) during lecture, but which does not appear on the in-class slides.  This material is handled differently by the other [compile modes](#compile-modes).

Many of the theorems do have proofs, generally contained in `webonly` mode.  In my opinion, it is important for the students to understand some of the proofs, in order to construct the conceptual framework in their own mind.  However, it is probably not so important to go over them during class, since the students won't follow them anyway.  My compromise is to mostly skip them during lecture, but keep them on the `web` mode slides, for reference.

The slides also include a number of in-class polls, about one per lecture.  I publish them on Piazza; my students respond on their mobile devices.  This works great.

### LaTeX Files

The slides are contained the following files:
* `slides.tex`: Master file.  Does all of the set-up, and defines slide-specific macros.
* `slides-class.tex`, `slides-web.tex`, `slides-blank.tex`, `slides-mine.tex`: These compile the slides in the different [compile modes](#compile-modes).
* `slides/*.tex`: The actual slide contents are contained in these slides.  They are organized by section in the book.
* `announcements.tex`: The daily announcements go here.

### Compile Modes

Slides can be compiled in one of five modes:
* `texing`: This is what you get when you compile `slides.tex`.  It compiles in `presentation` mode, with `webonly` material rendered semi-transparent.  This is useful when you're actively working on the slides.
* `class`: This is what you get when you compile `slides-class.tex`.  It compiles in `presentation` mode, with `webonly` material blanked out.  This is meant for in-class slides.
* `web`: This is what you get when you compile `slides-web.tex`.  It compiles in `handout` mode, with `webonly` material visible.  That day's announcements appear on the first slide.  This is meant to be put on the web after class.
* `blank`: This is what you get when you compile `slides-blank.tex`.  It compiles in `handout` mode, with `webonly` material blanked out, and the polls deleted.  That day's announcements appear on the first slide.  This is meant to be put on the web *before* class; students like to print these out and take notes in the blank spots.
* `mine`: This is what you get when you compile `slides-mine.tex`.  It compiles in `handout` mode, with `webonly` material rendered semi-transparent, and instructor notes (from the `\note{}` command) in a separate page to the right.  This is meant for the instructor to use during class.

### Preparing a Lecture

Here is the workflow for preparing a new lecture:

1. Update `\lecturedate{MM-DD}` at the top of `slides.tex` to the date of the lecture you're preparing.
2. Uncomment the `\input{slides/blah}` lines in `slides.tex` for the files containing material that you want to put in the lecture.  Comment out the rest of them--it takes a long time to parse a file even if Beamer doesn't render the slides contained in it.
3. Put the command `\lecture{}{MM-DD}` at the beginning of the material for that day's lecture, in the `slides/blah.tex` file.  Put `\lecture{}{MM-DD+1}` at the end of the material (really only necessary if you stop in the middle of `slides/blah.tex`).  Note that one lecture can span several `slides/blah.tex` files.
4. Make whatever changes you want to the LaTeX code in `slides/blah.tex`.  Compile `slides.tex` directly to see your changes--see [compile modes](#compile-modes) above.
5. Create that day's announcements in `announcements.tex` (this is easy; see the example `announcements.tex`).  The day's announcements are prepended to the slides in `web` and `blank` mode.

### Compiling a Lecture

Compile the slides for the modes you're going to use.  For instance, if you want the `web` mode file, compile `slides-web.tex`; it will be output to `slides-web.pdf`.

You'll usually need to compile each file *twice*.  This is due to TikZ pictures referring to each other; that uses the `.aux` file.

Copy `slides-web.pdf`, `slides-class.pdf`, etc. to wherever you need them. 
* I put `slides-class.pdf` and `slides-mine.pdf` on Dropbox, then access them from the console.
* I put `slides-blank.pdf` on my website before class, and `slides-web.pdf` on my website after class.

Alternatively, if you have a UNIX-like system (like a Mac), you can just run `./compile.sh` from a terminal (in the same directory with `slides.tex`).  This will compile all four modes, and create the files `daily/MM-DD-slides-(mode).pdf`.
