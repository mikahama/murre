# 🐶 Murre 🐕
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3473427.svg)](https://doi.org/10.5281/zenodo.3473427)

The amazing Murre (*genitive Murren* 🐕) will normalize non-standard Finnish (puhekieli) to standard Finnish (kirjakieli). 
This repository is maintained by [Mika Hämäläinen](https://mikakalevi.com).

## Installation

This library is designed for Python 3 and it may not work on Python 2.

    pip3 install murre
    python3 -m murre.download
    
## Usage

To normalize Finnish, all you need to do is to run:

    from murre import normalize_sentence
    
    print(normalize_sentence("mä syön paljo karkkii".split(" ")))
    >> minä syön paljon karkkia

To use the same chunk level BRNN model as described in the paper, you can pass *wnut19_model=True*, however this model might only work on Linux.

You can normalize multiple sentences at the same time by running

    from murre import normalize_sentences
    
	sents = ["kissa syö karkkii", "jok laulaa tuol puole", "en tiiä oikee et kuka se o", "kyl on hölömöö"]
	sentences = [x.split(" ") for x in sents] #tokenize each sentence [["kissa", "syö", "karkkii"], ["jok", "laulaa"...]...]

	print(normalize_sentences(sentences))
    >> ['kissa syö karkkia', 'joka laulaa tuolla puolen', 'en tiedä oikein että kuka se on', 'kyllä on hölmöä']

## Cite

Niko Partanen, Mika Hämäläinen, and Khalid Alnajjar. 2019. [Dialect Text Normalization to Normative Standard Finnish](https://www.aclweb.org/anthology/D19-5519/). In *the Proceedings of the 5th Workshop on Noisy User-generated Text (W-NUT)*.
