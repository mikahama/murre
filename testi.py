from murre import normalize_sentence, normalize_sentences

#print(normalize_sentence("mä syön paljo karkkii".split(" ")))

sents = ["kissa syö karkkii", "jok laulaa tuol puole", "en tiiä oikee et kuka se o", "kyl on hölömöö"]
sentences = [x.split(" ") for x in sents]

print(normalize_sentences(sentences))