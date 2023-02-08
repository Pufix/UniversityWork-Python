import json
import domain

def loading():
    array=[]
    f= open("src/db1.json","r")
    bok = json.loads(f.read())
    index = 0
    for i in bok:
        array.append(domain.book(bok[str(index)]))
        index+=1
    return array