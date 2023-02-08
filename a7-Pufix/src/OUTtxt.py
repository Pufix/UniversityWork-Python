import json
def pushing(array):
	endresult='{ "0":'+json.dumps(array[0].__dict__)
	for i in range(1,len(array)):
		endresult +=', "'+str(i)+'": '
		jsonStr = json.dumps(array[i].__dict__)
		endresult +=jsonStr
	f = open("src/db2.txt","w")
	f.write(endresult+"}")
	f.close()