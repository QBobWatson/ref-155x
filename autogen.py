#!/usr/bin/env python3

# JDR: this script is for generating all the reference slides in the pdf/
# directory.

# Before running, uncomment (only) \include{autogen} in slides.tex, and
# set \lecturedate to empty.

import os
import sys
import argparse
from shutil import move
from subprocess import call as _call
from contextlib import contextmanager

PDF_DIR = 'slides-pdf'

def call(cmdline):
    ret = _call(cmdline)
    if ret != 0:
        print("\n\nCommand {} returned status {}\n"
              .format(' '.join(cmdline), ret))
        sys.exit(1)

@contextmanager
def temp_open(path):
    f = open(path, 'w')
    try:
        yield f
    finally:
        if not f.closed:
            f.close()
        os.remove(path)

def latex(texfile, outfile, *infiles):
    with temp_open('autogen.tex') as f:
        f.write('\n'.join(['\\input{slides/'+x+'}' for x in infiles]))
        f.close()
        cmdline = ['pdflatex', texfile]
        call(cmdline)
        call(cmdline)
        move(texfile + '.pdf', outfile)

parser = argparse.ArgumentParser(
    description="Generate reference slide pdfs")
parser.add_argument('-w', '--web', action='append', metavar='NNN',
                    help='compile this section, web mode')
parser.add_argument('-W', '--all-web', action='store_true',
                    help='compile all sections, web mode')
parser.add_argument('-c', '--class', action='append', dest='klass', metavar='NNN',
                    help='compile this section, class mode')
parser.add_argument('-C', '--all-class', action='store_true',
                    help='compile all sections, class mode')
parser.add_argument('-b', '--big-web-file', action='store_true',
                    help='compile web mode slides into one big file')
parser.add_argument('-B', '--big-blank-file', action='store_true',
                    help='compile blank mode slides into one big file')
args = parser.parse_args(sys.argv[1:])

if len(sys.argv) < 2:
    parser.error("Nothing to do!")
    sys.exit(1)

# Review files have the form NN5; main ones have the form NN0
all_files = [x[:-4] for x in os.listdir('slides') if x.lower()[-4:] == '.tex']
main_files = [x for x in all_files if x[2] == '0']

web_files = []
if args.all_web:
    web_files = all_files
else:
    s = set(args.web or [])
    web_files = [x for x in all_files if x[0:3] in s]

class_files = []
if args.all_class:
    class_files = all_files
else:
    s = set(args.klass or [])
    class_files = [x for x in all_files if x[0:3] in s]


for fname in web_files:
    print("\n\nCompiling {} in web mode\n\n".format(fname))
    latex('slides-web', os.path.join(PDF_DIR, fname + '-web.pdf'), fname)

for fname in class_files:
    print("\n\nCompiling {} in class mode\n\n".format(fname))
    latex('slides-class', os.path.join(PDF_DIR, fname + '-class.pdf'), fname)

if args.big_web_file:
    print("\n\nCompiling all material into a big file in web mode\n\n")
    latex('slides-web', os.path.join(PDF_DIR, 'all_web.pdf'), *main_files)

if args.big_blank_file:
    print("\n\nCompiling all material into a big file in blank mode\n\n")
    latex('slides-blank', os.path.join(PDF_DIR, 'all_blank.pdf'), *main_files)
