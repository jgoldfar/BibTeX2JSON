# bibtex2json

[![Build Status](https://travis-ci.org/jgoldfar/BibTeX2JSON.svg?branch=master)](https://travis-ci.org/jgoldfar/BibTeX2JSON)

Small script for the conversion of bibtex files into JSON (actually, a simplified format, as well as (eventually) [BibJSON](http://okfnlabs.org/projects/bibjson/)).

## Usage

```
bibtex2json.py inputFile outputFile

# Or

cat inputFile | bibtex2json.py outputFile

# Or

cat inputFile | bibtex2json.py > outputFile

```
