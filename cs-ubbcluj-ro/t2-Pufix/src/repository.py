from domain import Player
import random
import copy
def powerTwo(number):
    i =1
    while i <= number:
        i *= 2
    return i/2
    
class repository:
    def __init__(self):
        self.players=[]
        self.pull()
        self.nextRound=[]
        self.roundType=""
    
    def add_player(self,player):
        self.players.append(player)

    def get_player(self,uuid):
        for i in range(len(self.players)):
            if self.players[i].uuid == uuid:
                return i
        return None
        
        
    def get_players(self):
        return self.players

    def pull(self):
        f=open("src/storage.txt","r")
        for line in f:
            player_uuid,player_name,player_score=line.split(",")
            player=Player(player_uuid,player_name,int(player_score))
            self.add_player(player)


            
    def verifyNextRound(self):
        if self.nextRound == []:
            if len(self.players) == 1:
                self.roundType = "winner"
            else:
                power= int(powerTwo(len(self.players)))
                if power != len(self.players):
                    self.roundType= "Qualifier"
                    diff = len(self.players) - power
                    diff *=2
                    self.players.sort(key=lambda x: x.strength, reverse=True)
                    participants = self.players[len(self.players)-diff:]
                    while len(participants)>0:
                        player1=participants.pop(random.randint(0,len(participants)-1))
                        player2=participants.pop(random.randint(0,len(participants)-1))
                        self.nextRound.append(["qual",player1,player2])
                else:
                    self.roundType= "Last "+str(power)
                    participants = copy.deepcopy(self.players)
                    while len(participants)>0:
                        player1=participants.pop(random.randint(0,len(participants)))
                        player2=participants.pop(random.randint(0,len(participants)))
                        self.nextRound.append(["last",player1,player2])

    def playRound(self):
        if self.roundType == "winner":
            return self.players[0]
        else:
            match=self.nextRound.pop(0)
            if match[0]=='qual':
                winner =1
                chance=match[1].strength+match[2].strength
                outcome = random.randint(0,chance)
                if outcome <= match[1].strength:
                    winner = 1
                else:
                    winner = 2
                if winner ==1:
                    self.players.pop(self.get_player(match[2].uuid))
                    return match[1]
                else:
                    self.players.pop(self.get_player(match[1].uuid))
                    return match[2]
            else:
                winner =1
                chance=match[1].strength+match[2].strength
                outcome = random.randint(0,chance)
                if outcome <= match[1].strength:
                    winner = 1
                else:
                    winner = 2
                if winner ==1:
                    self.players.pop(self.get_player(match[2].uuid))
                    return match[1]
                else:
                    self.players.pop(self.get_player(match[1].uuid))
                    return match[2]

                    
                    
            
if __name__ == "__main__":
    repo=repository()
    for player in repo.get_players():
        print(player)
        