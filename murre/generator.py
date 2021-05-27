import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
import logging

from mikatools import *

import tensorflow as tf
import tensorflow_addons as tfa
import pyonmttok
from .dialects import supported_dialects

logger = tf.get_logger()
logger.setLevel(logging.ERROR)

class UnknownDialectException(Exception):
	"""docstring for UnknownDialectException"""
	def __init__(self):
		super(UnknownDialectException, self).__init__()


try:
    tfa.seq2seq.gather_tree(0, 0, 0, 0)
except:
    pass

model = None
tokenizer = None

def _chunks(l, n):
	"""Yield successive n-sized chunks from l."""
	for i in range(0, len(l), n):
		yield l[i:i + n]

def generate(sentences, dialect):
	if dialect not in supported_dialects():
		raise UnknownDialectException(dialect + " is not a supported dialect! The supported dialects are: " + ", ".join(supported_dialects()))
	res = []
	for sentence in sentences:
		if isinstance(sentence, str):
			sentence = sentence.split(" ")
		s = [" ".join(w) for w in sentence]
		chunks = _chunks(s, 3)
		parts = [dialect + " " + " _ ".join(x).lower() for x in chunks]
		r_parts = _translate(parts)
		r = []
		for r_part, o_part in zip(r_parts, parts):
			res_tokens = r_part.split("_")
			o_tokens = o_part.split("_")
			if len(res_tokens) > len(o_tokens):
				res_tokens = res_tokens[:len(o_tokens)]
			r.append("_".join(res_tokens).replace(" ",""))


		r = "_".join(r)
		res.append(r.replace("_"," "))
	return res


def _load_model():
	global model
	global tokenizer
	model = tf.saved_model.load(script_path("models/generate/flags_dist"))
	tokenizer = pyonmttok.Tokenizer("none")


def _translate(texts):
	if model is None:
		_load_model()
	_translate_fn = model.signatures["serving_default"]

	inputs = _preprocess(texts)
	outputs = _translate_fn(**inputs)
	return _postprocess(outputs)

def _preprocess(texts):
	all_tokens = []
	lengths = []
	max_length = 0
	for text in texts:
		tokens = text.split(" ")
		length = len(tokens)
		all_tokens.append(tokens)
		lengths.append(length)
		max_length = max(max_length, length)
	for tokens, length in zip(all_tokens, lengths):
		if length < max_length:
			tokens += [""] * (max_length - length)

	inputs = {
		"tokens": tf.constant(all_tokens, dtype=tf.string),
		"length": tf.constant(lengths, dtype=tf.int32)}
	return inputs

def _postprocess( outputs):
	texts = []
	for tokens, length in zip(outputs["tokens"].numpy(), outputs["length"].numpy()):
		tokens = tokens[0][:length[0]].tolist()
		texts.append(tokenizer.detokenize(tokens))
	return texts