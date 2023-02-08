from ui import ui as userint
def main():
    print('\n'* 100)
    ui = userint()
    running = 1
    while running!=0:
        ui.printing()
        running=ui.get_move()
    ui.printing()
    
if __name__ == '__main__':
    main()
