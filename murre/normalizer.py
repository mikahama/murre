from mikatools import *
from natas.normalize import call_onmt

def dummy_picker(list, current_index, original_tokens):
	if len(list) == 0:
		return ""
	else:
		return list[0]

def _chunks(l, n):
	n = max(1, n)
	return [l[i:i+n] for i in range(0, len(l), n)]

def _dechunk(l,n_best=1, best_picker=dummy_picker, orig=[]):
	c = [best_picker([y.replace(" ", "") for y in x], i, orig) for i, x in enumerate(l)]
	c = "_".join(c)
	c = c.replace("_"," ")
	return c

def normalize_sentences(tokenized_sentences, wnut19_model=False, model_path=None, chunk_size=3, n_best=1, best_picker=dummy_picker, language="fin"):
	if language == "swe":
		chunk_size = 1
	elif language == "fin_hist":
		chunk_size = 3
	chunks = []
	sentence_map = []
	for i, tokenized_sentence in enumerate(tokenized_sentences):
		if isinstance(tokenized_sentence, str):
			tokenized_sentence = tokenized_sentence.split(" ")
			tokenized_sentences[i] = tokenized_sentence
		chunks_l = _chunks([" ".join(x) for x in tokenized_sentence],chunk_size)
		sent_chunks = [" _ ".join(x) for x in chunks_l]
		for c in sent_chunks:
			chunks.append(c)
			sentence_map.append(i)
	res = _normalize_chunks(chunks, wnut19_model=wnut19_model, model_path=model_path, n_best=n_best, language=language)
	normalized_sentences = []
	cur =0
	norm = []
	for i,s in enumerate(res):
		sent_i = sentence_map[i]
		if sent_i != cur:
			cur = sent_i
			normalized_sentences.append(norm)
			norm = []
		if sent_i == cur:
			norm.append(s)
	normalized_sentences.append(norm)
	r = [_dechunk(x, n_best=n_best, best_picker=best_picker, orig=y) for x, y in zip(normalized_sentences,tokenized_sentences)]
	return r




def normalize_sentence(tokens, wnut19_model=False,model_path=None, chunk_size=3, n_best=1, best_picker=dummy_picker, language="fin"):
	if language == "swe":
		chunk_size = 1
	elif language == "fin_hist":
		chunk_size = 3
	if isinstance(tokens, str):
		tokens = tokens.split(" ")
	chunks_l = _chunks([" ".join(x) for x in tokens],chunk_size)
	chunks = [" _ ".join(x) for x in chunks_l]
	res = _normalize_chunks(chunks, wnut19_model=wnut19_model, model_path=model_path, n_best=n_best, language=language)
	return _dechunk(res, n_best=n_best, best_picker=best_picker, orig=tokens)

def _normalize_chunks(chunks, wnut19_model=False, model_path=None, n_best=1, language="fin"):
	if model_path:
		model_name = model_path
	elif wnut19_model:
		#New default model, might not work on some systems
		model_name = "murre_norm_paper.pt"
		model_name = script_path("models/" + model_name)
	elif language == "swe":
		model_name = "swedish_normalization.pt"
		model_name = script_path("models/" + model_name)
	elif language == "fin_hist":
		model_name = "agricola.pt"
		model_name = script_path("models/" + model_name)
	else:
		#Same model trained on MacOS, slightly higher character error rate
		model_name = "murre_norm_default.pt"
		model_name = script_path("models/" + model_name)

	res = call_onmt(chunks, model_name, n_best=n_best)
	return res