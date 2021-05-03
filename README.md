# 🐶 Murre 🐕
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3473427.svg)](https://doi.org/10.5281/zenodo.3473427)

![CC BY NC ND](https://i.creativecommons.org/l/by-nc-nd/4.0/88x31.png)

The amazing Murre (*genitive Murren* 🐕) will normalize non-standard Finnish (puhekieli) to standard Finnish (kirjakieli). 
This repository is maintained by [Mika Hämäläinen](https://mikakalevi.com).

## Installation

This library is designed for Python 3 and it may not work on Python 2.

    pip3 install murre
    python3 -m murre.download
    
## Normalize

To normalize Finnish, all you need to do is to run:

    from murre import normalize_sentence
    
    normalize_sentence("mä syön paljo karkkii")
    >> minä syön paljon karkkia

To use the same chunk level BRNN model as described in the paper, you can pass *wnut19_model=True*, however this model might only work on Linux.

You can normalize multiple sentences at the same time by running

    from murre import normalize_sentences
    
    sents = ["kissa syö karkkii", "jok laulaa tuol puole", "en tiiä oikee et kuka se o", "kyl on hölömöö"]
    normalize_sentences(sents)
    >> ['kissa syö karkkia', 'joka laulaa tuolla puolen', 'en tiedä oikein että kuka se on', 'kyllä on hölmöä']

### Historical Finnish

To normalize (and lemmatize) historical Finnish, run:

    from murre import normalize_sentence
    
    normalize_sentence("paluellen herra caiken", language="fin_hist")
    >> palvella herra kaikki
  
### Swedish

You can use the Swedish model by passing *language=swe*

    from murre import normalize_sentence
    
    normalize_sentence("int vet ja", language="swe")
    >> inte vet jag

## Generate

Murre can also generate different dialects. All you need to do, is to run:

    from murre import dialectalize_sentence
    dialectalize_sentence("kodin takana on koira", "Inkerinsuomalaismurteet")
    >> 'kojin takan on koira'

Or for multiple sentences:

    from murre import dialectalize_sentences
    sents = ["kissa syö karkkia", "kädellä on perhonen", "kettu juoksee sutta karkuun"]
    dialectalize_sentences(sents,'Kainuu')
    >> ['kissa syöpi karkkia', 'käellä om perhonej', 'kettu juoksee sutta karkuu']


The list of available dialects can be obtained by:

    from murre import supported_dialects
    supported_dialects()
    >> ['Pohjois-Satakunta', 'Keski-Karjala', 'Kainuu', 'Etelä-Pohjanmaa', 'Etelä-Satakunta', 'Pohjois-Savo', 'Pohjois-Karjala', 'Keski-Pohjanmaa', 'Kaakkois-Häme', 'PohjoinenKeski-Suomi', 'Pohjois-Pohjanmaa', 'PohjoinenVarsinais-Suomi', 'Etelä-Karjala', 'Länsi-Uusimaa', 'Inkerinsuomalaismurteet', 'LäntinenKeski-Suomi', 'Länsi-Satakunta', 'Etelä-Savo', 'Länsipohja', 'Pohjois-Häme', 'EteläinenKeski-Suomi', 'Etelä-Häme', 'Peräpohjola']

## Business solutions


<img src="https://rootroo.com/cropped-logo-01-png/" alt="Rootroo logo" width="128px" height="128px">

Non-standard dialectal data can be a mess to deal with when you are processing your customer data. Let us help! [Rootroo offers consulting related to text normalization](https://rootroo.com/). We have a strong academic background in the state-of-the-art AI solutions for every NLP need. Just contact us, we won't bite.

## Cite

**Normalization (Finnish)**

Niko Partanen, Mika Hämäläinen, and Khalid Alnajjar. (2019). [Dialect Text Normalization to Normative Standard Finnish](https://www.aclweb.org/anthology/D19-5519/). In *the Proceedings of the 5th Workshop on Noisy User-generated Text (W-NUT)*.


**Normalization (Swedish)**

Mika Hämäläinen, Niko Partanen and Khalid Alnajjar. (2020). [Normalization of Different Swedish Dialects Spoken in Finland](https://www.researchgate.net/publication/346933795_Normalization_of_Different_Swedish_Dialects_Spoken_in_Finland). In *the Proceedings of the 4th ACM SIGSPATIAL Workshop on Geospatial Humanities*.

**Dialect generation**

Mika Hämäläinen, Niko Partanen, Khalid Alnajjar, Jack Rueter & Thierry Poibeau (2020). [Automatic Dialect Adaptation in Finnish and its Effect on Perceived Creativity](https://www.researchgate.net/publication/344157810_Automatic_Dialect_Adaptation_in_Finnish_and_its_Effect_on_Perceived_Creativity). In *Proceedings of the 11th International Conference on Computational Creativity*. p. 204-211

**Historical Finnish**

Mika Hämäläinen, Niko Partanen and Khalid Alnajjar. (2021). Lemmatization of Historical Old Literary Finnish Texts in Modern Orthography. In *Actes de la Conférence sur le Traitement Automatique des Langues Naturelles (TALN)*.



## Data

The data used in the paper describing dialect generation has been published on Zenodo [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3885341.svg)](https://doi.org/10.5281/zenodo.3885341).
