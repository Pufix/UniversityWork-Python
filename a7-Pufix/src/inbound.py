import INjson
import INtxt
import INpick
import INsql
def pull_db():
    d = {}
    with open('src/settings.properties') as f:
        for line in f:
            if line[-1]=='\n':
                line=line[:-1]
            if line[0]!='[':
                key, value = line.split('=')
                d[key] = value
    if d['dbname']=='json':
        return INjson.loading()
    elif d['dbname']=='txt':
        return INtxt.loading()
    elif d['dbname']=='pickle':
        return INpick.loading()
    elif d['dbname']=='sql':
        return INsql.loading(d['user'],d['password'])
