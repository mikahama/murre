import os
import logging

from mikatools import *

from onmt_runner import Translator
from .dialects import supported_dialects


class UnknownDialectException(Exception):
	"""docstring for UnknownDialectException"""
	def __init__(self):
		super(UnknownDialectException, self).__init__()


model = None

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
	model = Translator.load(script_path("models/generate/flags_dist"))


def _translate(texts):
	if model is None:
		_load_model()

	res = model.translate_many(texts)
	return res