#!/usr/bin/env python3
from game import Game
from events import AnsweredCorrectly, AnsweredIncorrectly, QuestionAsked, PlayerMoved, PenaltyBoxLeaved, \
    PenaltyBoxNotLeaved, Rolled, PlayerAdded
from random import randrange


def play_game():
    game = Game()
    game.add('Chet')
    game.add('Pat')
    game.add('Sue')
    while not game.has_winner():
        game.roll(randrange(5) + 1)

        if randrange(9) == 7:
            game.answer_incorrectly()
        else:
            game.answer_correctly()

        for event in game.pop_events():
            if isinstance(event, AnsweredCorrectly):
                print('Answer was correct!!!!')
                print(event.player_name + ' now has ' + str(event.player_coins) + ' Gold Coins.')
            if isinstance(event, AnsweredIncorrectly):
                print('Question was incorrectly answered')
                print(event.player_name + " was sent to the penalty box")
            if isinstance(event, QuestionAsked):
                print(event.question)
            if isinstance(event, PlayerMoved):
                print(event.player_name + '\'s new location is ' + str(event.player_position))
                print("The category is %s" % event.question_category)
            if isinstance(event, PenaltyBoxLeaved):
                print("%s is getting out of the penalty box" % event.player_name)
            if isinstance(event, PenaltyBoxNotLeaved):
                print("%s is not getting out of the penalty box" % event.player_name)
            if isinstance(event, Rolled):
                print("%s is the current player" % event.player_name)
                print("They have rolled a %s" % event.roll)
            if isinstance(event, PlayerAdded):
                print(event.player_name + " was added")
                print("They are player number %s" % event.players_count)


if __name__ == '__main__':
    play_game()
