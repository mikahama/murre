from .normalizer import normalize_sentence, normalize_sentences
from .dialects import supported_dialects
from .generator import generate as dialectalize_sentences

def dialectalize_sentence(sentence, dialect):
	return dialectalize_sentences([sentence], dialect)[0]