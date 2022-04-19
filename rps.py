import random

"""This program plays a game of Rock, Paper, Scissors"
between two Players, and 
reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class 
for all of the Players
in this game"""

class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass

class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)

def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))

class Game:
    score = 0
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        if beats(one, two) == True and beats(one, two) == False:
            self.p1.score += 1
            print("Player 1 wins this round")
        elif beats(one, two) == False and beats(one, two) == True:
            self.p2.score += 1
            print("Player 2 wins this round")
        else:
            print("-- IT'S A TIE --")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        print("SCORE")
        print(
            f'Human: {self.player1.score} | Computer: {self.player2.score}\n')

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
        print("Game over!")


if __name__ == '__main__':
    game = Game(RandomPlayer(), RandomPlayer())
    game.play_game()