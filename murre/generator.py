import opennmt as onmt
from mikatools import *

import tensorflow as tf
import tensorflow_addons as tfa
try:
    tfa.seq2seq.gather_tree(0, 0, 0, 0)
except tf.errors.InvalidArgumentError:
    pass

model = None
checkpoint = None



def _load_model():
	global model
	model = tf.saved_model.load(script_path("models/generate/flags_dist"))


def translate(texts):
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
		texts.append(self._tokenizer.detokenize(tokens))
	return texts