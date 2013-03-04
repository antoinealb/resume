#!/usr/bin/bash

pdflatex french.tex
pdflatex english.tex

mv french.pdf pdf/
mv english.pdf pdf/
