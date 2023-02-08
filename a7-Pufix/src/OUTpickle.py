from pickle import dump
def pushing(array):
	f = open("src/db3.pickle","wb")
	dump(array,f)