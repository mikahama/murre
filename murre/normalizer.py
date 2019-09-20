from mikatools import *
from natas.normalize import call_onmt


def _chunks(l, n):
	n = max(1, n)
	return [l[i:i+n] for i in range(0, len(l), n)]

def _dechunk(l):
	c = [x[0] for x in l]
	c = " _ ".join(c)
	c = c.replace(" ", "")
	c = c.replace("_"," ")
	return c


def normalize_sentence(tokens, wnut19_model=False):
	if wnut19_model:
		#Trained on Linux, so it doesn't work on Mac for instance :-(
		model_name = "murre_norm_paper.pt"
	else:
		#Same model trained on MacOS, slightly higher character error rate
		model_name = "murre_norm_default.pt"
	model_name = script_path("models/" + model_name)
	chunks_l = _chunks([" ".join(x) for x in tokens],3)
	chunks = [" _ ".join(x) for x in chunks_l]
	res = call_onmt(chunks, model_name, n_best=1)
	return _dechunk(res)