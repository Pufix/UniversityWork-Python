from pickle import load
def loading():
	f = open("src/db3.pickle","rb")
	return load(f)