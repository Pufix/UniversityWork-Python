from repository import repository
class service:
    def __init__(self):
        self.repo=repository()

    def get_players(self):
        players=self.repo.get_players()
        players.sort(key=lambda x: x.strength, reverse=True)
        result=""
        for player in players:
            result=result+str(player)+"\n"
        return result

    def verify(self):
        self.repo.verifyNextRound()

    def playRound(self):
        return self.repo.playRound()

    def display_rounds(self):
        return self.repo.nextRound