from service import service 

def startup():
    try:
        commands = service()
        running = True
        menuprintint()
        while running:
            running=runtime(commands)
    except ValueError as err:
        print(err)
        
def runtime(commands:service):
    try:
        print()
        cmd=getCmd()
        if cmd[0]=='exit' or cmd[0]=='ragequit' or cmd[0]=='quit':
            return False
        elif cmd[0]=='help' or cmd[0]=='helpmepls':
            prtHelp()
        elif cmd[0]=='pull':
            commands.pull()
        elif cmd[0]=='push':
            commands.push()
        elif cmd[0]=='list':
            commands.afis()
        elif cmd[0]=='add':
            commands.add(cmd)
        elif cmd[0]=='undo':
            commands.undo()
        elif cmd[0]=='filter':
            commands.filter(cmd)

    except (ValueError, AssertionError) as err:
        print(err)
    return True


def getCmd():
    cmd=input()
    command=cmd.split()
    cmdList=[
        "exit",
        "quit",
        "ragequit",
        "help",
        "pull",
        "push",
        "helpmepls",
        "list",
        "add",
        "undo",
        "filter",
        ]
    ok=0
    assert len(command)!=0, ""
    if command[0] in cmdList:
        ok=1
    assert ok == 1, "ERROR: Invalid command!"
    return command



def menuprintint():
    menu="""
Library manager v1.0
Use commands in order to interact with the database
Use help in order to see what commands are avalable
"""
    print(menu)



def prtHelp():
    helpmen="""\

help
exit
quit
pull
push
list
add <book_name> by <author_name>
undo
filter <letter>
"""
    print(helpmen)