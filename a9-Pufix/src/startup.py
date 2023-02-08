import ui.consoleUI
import ui.renderedUI
def start():
    d = {}
    with open('src/interface.properties') as f:
        for line in f:
            if line[-1]=='\n':
                line=line[:-1]
            if line[0]!='[':
                key, value = line.split('=')
                d[key] = value

    print('\n'*200)
    if d['interface']=='console':
        ui.consoleUI.initialize()
    else:
        ui.renderedUI.initialize()
start()