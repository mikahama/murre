from murre import normalize_sentence, normalize_sentences

#print(normalize_sentence("mä syön paljo karkkii".split(" ")))

sents = ["kissa syö karkkii", "jok joikhaa tuol puole", "emmä tiiä oikee et kuka se o", "kyl on ärsyttävää"]
sentences = [x.split(" ") for x in sents]

print(normalize_sentences(sentences))