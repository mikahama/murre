from mikatools import *
import os

def main():
	url = "https://github.com/mikahama/murre/raw/master/murre/models/"
	models = ["murre_norm_default.pt", "murre_norm_paper.pt", "swedish_normalization.pt", "agricola.pt"]
	for i, model in enumerate(models):
		print("Downloading normalizer ", i+1, "out of", len(models) )
		download_file(url + model, script_path("models/" + model), show_progress=True)
	files = ["generate/flags_dist/saved_model.pb", "generate/flags_dist/variables/variables.data-00000-of-00002", "generate/flags_dist/variables/variables.data-00001-of-00002", "generate/flags_dist/variables/variables.index"]
	os.makedirs(script_path("models/generate/flags_dist/variables/"), exist_ok=True)
	os.makedirs(script_path("models/generate/flags_dist/assets/"), exist_ok=True)
	for i, file in enumerate(files):
		print("Downloading generator ", i+1, "out of", len(files) )
		download_file(url + file, script_path("models/" + file), show_progress=True)

if __name__== "__main__":
  main()