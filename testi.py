from murre import normalize_sentence, normalize_sentences, dialectalize_sentences, dialectalize_sentence, supported_dialects

from murre import generator

#print(normalize_sentence("mä syön paljo karkkii".split(" ")))

"""
sents = ["kissa syö karkkii", "jok laulaa tuol puole", "en tiiä oikee et kuka se o", "kyl on hölömöö"]
sentences = [x.split(" ") for x in sents]

print(normalize_sentences(sentences))
"""

#print(generator._translate(["Etelä-Häme k i s s a n i _ j u o k s i _ p o i s"]))


sents = ["minä nauran ja kovaa", "hattu on päässä aina talvisin"]
sentences = [x.split(" ") for x in sents]

"""

print(dialectalize_sentences(sentences, "Inkerinsuomalaismurteet"))

print(dialectalize_sentence("minä ihmettelen ja suuresti".split(" "), "Keski-Karjala"))

print(supported_dialects())

"""

for dialect in supported_dialects():
	print(dialect)
	print(dialectalize_sentences(sentences, dialect))