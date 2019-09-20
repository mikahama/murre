from mikatools import *

def main():
	url = "https://github.com/mikahama/murre/raw/master/murre/models/"
	models = ["murre_norm_default.pt", "murre_norm_paper.pt"]
	for i, model in enumerate(models):
		print("Downloading", i+1, "out of", len(models) )
		download_file(url + model, script_path("models/" + model), show_progress=True)

if __name__== "__main__":
  main()