#!/usr/bin/env python3

class Game:
    def __init__(self):
        # TODO : Missing Player abstraction ?
        self.player_names = []
        self._position = [0] * 6
        self._coins = [0] * 6
        self.in_penalty_box = [0] * 6

        self.current_player = 0
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
        self.player_names.append(player_name)
        self._position[len(self.player_names)] = 0
        self._coins[len(self.player_names)] = 0
        self.in_penalty_box[len(self.player_names)] = False

        self._display_new_player(player_name)

    def _display_new_player(self, player_name):
        print(player_name + " was added")
        print("They are player number %s" % len(self.player_names))

    def roll(self, roll):
        self._display_player_roll(roll)

        if self.in_penalty_box[self.current_player]:
            roll_is_even = roll % 2 == 0
            if roll_is_even:
                self._display_not_getting_out_penalty_box()
                self.is_getting_out_of_penalty_box = False
            else:
                self.is_getting_out_of_penalty_box = True
                self._display_getting_out_penalty_box()

        if not self.in_penalty_box[self.current_player] or self.is_getting_out_of_penalty_box:
            self._move_player(roll)
            self._display_player_place_and_category()
            self._ask_question()

    def _display_not_getting_out_penalty_box(self):
        print("%s is not getting out of the penalty box" % self.player_names[self.current_player])

    def _display_player_place_and_category(self):
        print(self.player_names[self.current_player] + '\'s new location is ' + str(self._position[self.current_player]))
        print("The category is %s" % self._current_category)

    def _move_player(self, roll):
        self._position[self.current_player] += roll
        if self._position[self.current_player] > 11:
            self._position[self.current_player] -= 12

    def _display_getting_out_penalty_box(self):
        print("%s is getting out of the penalty box" % self.player_names[self.current_player])

    def _display_player_roll(self, roll):
        print("%s is the current player" % self.player_names[self.current_player])
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
        if self._position[self.current_player] == 0: return 'Pop'
        if self._position[self.current_player] == 4: return 'Pop'
        if self._position[self.current_player] == 8: return 'Pop'

        if self._position[self.current_player] == 1: return 'Science'
        if self._position[self.current_player] == 5: return 'Science'
        if self._position[self.current_player] == 9: return 'Science'

        if self._position[self.current_player] == 2: return 'Sports'
        if self._position[self.current_player] == 6: return 'Sports'
        if self._position[self.current_player] == 10: return 'Sports'

        return 'Rock'

    def was_correctly_answered(self):
        # TODO : CQS non respecté
        if self.in_penalty_box[self.current_player] and not self.is_getting_out_of_penalty_box:
            self._select_next_player()
            return True
        else:
            self._add_coins_to_player()
            self._display_correct_answer_and_player_coins()
            winner = self._did_player_win()
            self._select_next_player()
            return winner

    def _select_next_player(self):
        self.current_player += 1
        if self.current_player == len(self.player_names):
            self.current_player = 0

    def _add_coins_to_player(self):
        self._coins[self.current_player] += 1

    def _display_correct_answer_and_player_coins(self):
        print('Answer was correct!!!!')
        print(self.player_names[self.current_player] + ' now has ' + str(self._coins[self.current_player]) + ' Gold Coins.')

    def wrong_answer(self):
        self._display_move_player_in_penalty_box()
        self.in_penalty_box[self.current_player] = True
        self._select_next_player()
        return True

    def _display_move_player_in_penalty_box(self):
        print('Question was incorrectly answered')
        print(self.player_names[self.current_player] + " was sent to the penalty box")

    def _did_player_win(self):
        return not (self._coins[self.current_player] == 6)


from random import randrange


def play_game():
    game = Game()
    game.add('Chet')
    game.add('Pat')
    game.add('Sue')
    not_a_winner = True
    while not_a_winner:
        game.roll(randrange(5) + 1)

        if randrange(9) == 7:
            not_a_winner = game.wrong_answer()
        else:
            not_a_winner = game.was_correctly_answered()


if __name__ == '__main__':
    play_game()
