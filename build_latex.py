#!/usr/bin/env python3

# This file is called before each commit to generate all up to date PDFs
# before sending them to Bitbucket.

from subprocess import call
for i in ("french.tex",):
  call(["pdflatex", i])
