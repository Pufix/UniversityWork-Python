class Player:
    def __init__(self, uuid, name, strength):
        self.name = name
        self.uuid = uuid
        self.strength = strength 

    def __str__(self):
        return "Player " + self.uuid + " is " + self.name + " with a strength of " + str(self.strength)