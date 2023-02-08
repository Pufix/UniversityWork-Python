from repository import repository
from services import service
from ui import ui as userinterface
def main():
    ui=userinterface()
    running=True
    while running:
        try:
            ui.print_menu()
            cmd=ui.read_command()
            if cmd==0:
                running=False
            elif cmd==1:
                print("\n"*200)
                ui.print_players()
            elif cmd==2:
                print("\n"*200)
                ui.display_rounds()
            elif cmd==3:
                print("\n"*200)
                ui.playNext()
        except:
            pass
main()