#!/usr/bin/env python3
from dataclasses import dataclass


@dataclass
class Player:
    _name: str
    _position: int = 0
    _coins: int = 0
    _in_penalty_box: bool = False

    def name(self) -> str:
        return self._name

    def move(self, roll):
        self._position += roll
        if self._position > 11:
            self._position -= 12

    def position(self) -> int:
        return self._position

    def add_coin(self):
        self._coins += 1

    def coins(self) -> int:
        return self._coins

    def move_in_penalty_box(self):
        # TODO : ask the PO - on ne sort jamais de la penalty box ??
        self._in_penalty_box = True

    def in_penalty_box(self) -> bool:
        return self._in_penalty_box

    def has_won(self) -> bool:
        return self._coins == 6


class Game:
    def __init__(self):
        self._players: list[Player] = []

        self.current_player_index = 0
        self.is_getting_out_of_penalty_box = False

        self.pop_questions = []
        self.science_questions = []
        self.sports_questions = []
        self.rock_questions = []

        for i in range(50):
            self.pop_questions.append("Pop Question %s" % i)
            self.science_questions.append("Science Question %s" % i)
            self.sports_questions.append("Sports Question %s" % i)
            self.rock_questions.append("Rock Question %s" % i)

    def add(self, player_name):
        self._players.append(Player(player_name))

        self._display_new_player(player_name)

    def _display_new_player(self, player_name):
        print(player_name + " was added")
        print("They are player number %s" % len(self._players))

    def roll(self, roll):
        self._display_player_roll(roll)

        if self._player().in_penalty_box():
            roll_is_even = roll % 2 == 0
            if roll_is_even:
                self._display_not_getting_out_penalty_box()
                self.is_getting_out_of_penalty_box = False
            else:
                self.is_getting_out_of_penalty_box = True
                self._display_getting_out_penalty_box()

        if not self._player().in_penalty_box() or self.is_getting_out_of_penalty_box:
            self._move_player(roll)
            self._display_player_place_and_category()
            self._ask_question()

    def _display_not_getting_out_penalty_box(self):
        print("%s is not getting out of the penalty box" % self._player().name())

    def _display_player_place_and_category(self):
        print(self._player().name() + '\'s new location is ' + str(self._player().position()))
        print("The category is %s" % self._current_category)

    def _move_player(self, roll):
        self._player().move(roll)

    def _player(self):
        return self._players[self.current_player_index]

    def _display_getting_out_penalty_box(self):
        print("%s is getting out of the penalty box" % self._player().name())

    def _display_player_roll(self, roll):
        print("%s is the current player" % self._player().name())
        print("They have rolled a %s" % roll)

    def _ask_question(self):
        # TODO : logique conditionnelle, code duplication
        if self._current_category == 'Pop': print(self.pop_questions.pop(0))
        if self._current_category == 'Science': print(self.science_questions.pop(0))
        if self._current_category == 'Sports': print(self.sports_questions.pop(0))
        if self._current_category == 'Rock': print(self.rock_questions.pop(0))

    @property
    def _current_category(self):
        # TODO : logique conditionnelle, duplication
        if self._player().position() == 0: return 'Pop'
        if self._player().position() == 4: return 'Pop'
        if self._player().position() == 8: return 'Pop'

        if self._player().position() == 1: return 'Science'
        if self._player().position() == 5: return 'Science'
        if self._player().position() == 9: return 'Science'

        if self._player().position() == 2: return 'Sports'
        if self._player().position() == 6: return 'Sports'
        if self._player().position() == 10: return 'Sports'

        return 'Rock'

    def answer_correctly(self):
        if self._player().in_penalty_box() and not self.is_getting_out_of_penalty_box:
            self._select_next_player()
        else:
            self._player().add_coin()
            self._display_correct_answer_and_player_coins()
            self._select_next_player()

    def _select_next_player(self):
        self.current_player_index += 1
        if self.current_player_index == len(self._players):
            self.current_player_index = 0

    def _display_correct_answer_and_player_coins(self):
        print('Answer was correct!!!!')
        print(self._player().name() + ' now has ' + str(self._player().coins()) + ' Gold Coins.')

    def answer_incorrectly(self):
        self._display_move_player_in_penalty_box()
        self._player().move_in_penalty_box()
        self._select_next_player()

    def _display_move_player_in_penalty_box(self):
        print('Question was incorrectly answered')
        print(self._player().name() + " was sent to the penalty box")

    def has_winner(self) -> bool:
        for player in self._players:
            if player.has_won():
                return True
        return False


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


if __name__ == '__main__':
    play_game()
