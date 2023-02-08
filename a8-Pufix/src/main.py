from ui.ui import ui as userint
from repository.repo import repository
from services.serv import service
import colorama
def main():
    for i in range(200):
        print()
    repo=repository()
    serv=service(repo)
    ui=userint(serv)
    running=True
    while running:
        running=ui.cmd()
main()


