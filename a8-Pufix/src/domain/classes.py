class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    BLACK = '\033[30m'
    CLEAR = '\033[39m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    REVERSE = '\033[7m'
    HIDDEN = '\033[8m'
    RESET = '\033[0m'
    

class book:
    def __init__(self,dict):
        self.uuid = dict['uuid']
        self.name = dict['name']
        self.author = dict['author']
        self.rented = False
    def prt(self):
        if self.rented:
            print("    Book #"+bcolors.OKGREEN+str(self.uuid)+bcolors.CLEAR+" is "+bcolors.CYAN+str(self.name)+bcolors.CLEAR+" by "+bcolors.YELLOW+str(self.author)+bcolors.RED+" is rented"+bcolors.CLEAR)
        else:
            print("    Book #"+bcolors.OKGREEN+str(self.uuid)+bcolors.CLEAR+" is "+bcolors.CYAN+str(self.name)+bcolors.CLEAR+" by "+bcolors.YELLOW+str(self.author)+bcolors.GREEN+" is not rented"+bcolors.CLEAR)
            
            


class client:   
    def __init__(self,dict):
        self.uuid = dict['uuid']
        self.name = dict['name']
        
    def prt(self):
        print("    Client #"+bcolors.OKGREEN+str(self.uuid)+bcolors.CLEAR+" is "+bcolors.CYAN+str(self.name)+bcolors.CLEAR)
        
        
class rental:
    def __init__(self,uuid,bookrented,renter,datefrom,dateto):
        self.uuid = uuid
        self.book = bookrented
        self.client = renter
        self.datefrom = datefrom
        self.dateto = dateto
        
    def prt(self):
        if self.dateto!=0:
            print("    Rental #"+bcolors.GREEN+str(self.uuid)+'\033[39m'+" is "+'\033[31m'+str(self.book.name)+'\033[39m'+" by "+bcolors.YELLOW+str(self.book.author)+'\033[39m'+" rented by "+bcolors.BLUE+str(self.client.name)+'\033[39m'+" from "+bcolors.CYAN+str(self.datefrom)+'\033[39m'+" to "+bcolors.MAGENTA+str(self.dateto)+'\033[39m')
        else:
            print("    Rental #"+bcolors.GREEN+str(self.uuid)+'\033[39m'+" is "+'\033[31m'+str(self.book.name)+'\033[39m'+" by "+bcolors.YELLOW+str(self.book.author)+'\033[39m'+" rented by "+bcolors.BLUE+str(self.client.name)+'\033[39m'+" from "+bcolors.CYAN+str(self.datefrom)+'\033[39m'+" to "+bcolors.MAGENTA+"not returned"+'\033[39m')
    
    
    
        
                    