# Evaluating Ceph as a Filesystem for HPC

This is the LaTeX source of my Master's thesis "Evaluating Ceph as a Filesystem for HPC".

This LaTeX template has been adapted from the HPS report template and the thesis template of the institute of computer science of the university of Göttingen.

## Usage

The template uses LaTeX, therefore, it must be compiled by a TeX engine supporting pdflatex to produce a PDF file.
This can be a local installation of TeX such as TeX Live or MiKTeX or a web application such as Overleaf.

Furthermore, this template provides a Makefile for producing a PDF from the command line on systems that have make installed.

Use `make` to produce a fast rebuild of the document.
Use `make biber` to make a clean rebuild including the bibliography.

The first build should use `make biber`.

To expand the bibliography, references should be added in the biblatex format to ref.bib.

Usage of svg files is possible but might require adding the flag `--shell-escape` in the Makefile to the pdflatex commands and an installation of Inkscape to enable the conversion of svg images to pdf images as required for adding them into the final PDF.

When starting to work with the template, one should at first configure the document configuration found in main.tex.

## License

Copyright (c) 2026 Tim Dettmar

The contents of this thesis are licensed under the CC-BY-SA 4.0 license.  
Exceptions include the university and department logos which may not be reproduced outside the context of this thesis.

## Contact & Credits

For question about the content of the thesis, I can be contacted via email -> hpc@timd.io

This template was adapted from the official thesis template of the institute of computer science by
Lars Quentin (lars.quentin@stud.uni-goettingen.de) and Jonathan Decker (jonathan.decker@uni-goettingen.de).

Please direct any questions regarding the template to them.
