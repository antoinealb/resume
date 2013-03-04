This is the repository for my resume, written in Latex. PDF versions are
available in the pdfs folder.

To enable automatic generation of PDFs before commit, add the following
to .hg/hgrc :

[hooks]
pre-commit = ./build_pdfs.sh
