import OUTjson
import OUTtxt
import OUTpickle
import OUTsql
def push_db(array:list,mods):
    d = {}
    with open('src/settings.properties') as f:
        for line in f:
            if line[-1]=='\n':
                line=line[:-1]
            if line[0]!='[':
                key, value = line.split('=')
                d[key] = value
    if d['dbname']=='json':
        OUTjson.pushing(array)
    elif d['dbname']=='txt':
        OUTtxt.pushing(array)
    elif d['dbname']=='pickle':
        OUTpickle.pushing(array)
    elif d['dbname']=='sql':
        OUTsql.pushing(array,mods,d['user'],d['password'])
        mods=[]