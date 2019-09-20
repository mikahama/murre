# 🐶 Murre 🐕
The amazing Murre (*genitive Murren* 🐕) will normalize non-standard Finnish (puhekieli) to standard Finnish (kirjakieli). 
This repository is maintained by [Mika Hämäläinen](https://mikakalevi.com).

## Installation

This library is designed for Python 3 and it may not work on Python 2.

    pip3 --no-cache-dir install pip==18.1
    pip3 install murre --process-dependency-links
    python3 -m murre.download
    
## Usage

To normalize Finnish, all you need to do is to run:

    from murre import normalize_sentence
    
    print(normalize_sentence("mä syön paljo karkkii".split(" ")))
    >> minä syön paljon karkkia

To use the same chunk level BRNN model as described in the paper, you can pass *wnut19_model=True*, however this model might only work on Linux.

## Cite

Niko Partanen, Mika Hämäläinen, and Khalid Alnajjar. Accepted. Dialect Text Normalization to Normative Standard Finnish. In *the Proceedings of the 5th Workshop on Noisy User-generated Text (W-NUT)*.
