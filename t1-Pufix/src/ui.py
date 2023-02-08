from functions import add_flight
from functions import show_flights
from functions import del_flight
from functions import inc_flights

def start():
    run = True
    add_flight('17W542','100','Cluj-Napoca','Timisoara')
    add_flight('1S35A1','200','Timisoara','Cluj-Napoca')
    add_flight('123456','75','Cluj-Napoca','Bucuresti')
    add_flight('654321','360','Bucuresti','Cluj-Napoca')
    add_flight('AC13DC','27','Cluj-Napoca','Tokyo')
    clean()
    while run:
        run = runtime()

def clean():
    for w in range(200):
        print()

def prtmenu():
    menu="""
Please enter your wanted function:
1. Add a flight 
2. Delete a flight
3. Show all flights departing from a city
4. Increase time due to strong winds
0. Exit

"""
    print(menu)

def runtime():
    prtmenu()
    cmd=input("Please enter your desired opertation: ")
    if cmd=='0':
        return False
    elif cmd=='1':
        code=input("Please enter the code of the flight: ")
        duration=input("Please enter the duration of the flight: ")
        origin=input("Please enter the city of departure of the flight: ")
        destination=input("Please enter the destination of the flight: ")
        clean()
        try:
            add_flight(code,duration,origin,destination)
        except AssertionError as err:
            print(err)
        print()
    elif cmd=='2':
        code=input("Please enter the code of the flight you want to delete: ")
        del_flight(code)
        clean()
    elif cmd=='3':
        origin=input("Please enter the city of departure for the flights: ")
        clean()
        flights=show_flights(origin)
        for flight in flights:
            print("Flight "+flight['id']+" is flying from "+flight['depart_city']+" to "+flight['destination_city']+ " with a duration of "+str(flight['duration'])+" minutes\n")
        print('\n')
    elif cmd=='4':
        origin=input("Please enter the city of departure for the flights: ")
        delay=int(input("Please enter the time delay: "))
        clean()
        try:
            inc_flights(origin,delay)
        except AssertionError as err:
            print(err)
    else:
        clean()
    return True



start()


