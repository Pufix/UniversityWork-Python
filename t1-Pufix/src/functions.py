flights={}

def add_flight(code,duration,depart_city,destination_city):
    assert len(code)>=3,"Invalid flight code"
    assert len(depart_city)>=3,"Invalid depart city"
    assert len(destination_city)>=3,"Invalid destination city"
    assert int(duration) >=20,"Invalid flight duration"
    global flights
    flight={}
    flight['duration']=int(duration)
    flight['depart_city']=depart_city
    flight['destination_city']=destination_city
    flights[code]=flight

def del_flight(code):
    global flights
    try:# the modules tryes to delete the flight with at that code, passing if there is no flight with that code
        flights.pop(code)
        return 1
    except:
        return 0

def show_flights(origin):
    results=[]
    for id in flights:
        if flights[id]['depart_city']==origin:
            flight=flights[id]
            flight['id']=id
            results.append(flight)
    return sorted(results, key=lambda fligh: fligh['destination_city'])

def inc_flights(origin,delay):
    assert delay >=10 and delay <=60,"Invalid delay time!"
    for id in flights:
        if flights[id]['depart_city']==origin:
            flights[id]['duration']+=delay


def test_del_exiting_flight():
    add_flight('17W542','100','Cluj-Napoca','Timisoara')
    assert del_flight('17W542')==1

def test_del_exiting_flight():
    add_flight('17W542','100','Cluj-Napoca','Timisoara')
    assert del_flight('onion')==0

if __name__ == '__main__':
    test_del_exiting_flight()