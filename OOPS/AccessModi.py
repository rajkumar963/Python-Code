# Access Modifiers:-
# 1. Public
# 2. Private
# 3. Protected
# 4. Default
# """

class Cricket:
    def __init__(self, player1, player2, fight):
        self.player1 = player1
        self.player2 = player2
        self.__fight = fight

        def __internal_conversation(self):
            print("I am an internal conversation")

        def play(self):
            print("I love to play cricket")

            cric=Cricket("MSDhoni","virat","i am big fan of virat and MSDhoni")
            print(cric.player1)
            cric.play()


        