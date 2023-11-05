from events import AnsweredCorrectly, AnsweredIncorrectly, QuestionAsked, PlayerMoved, PenaltyBoxLeaved, \
    PenaltyBoxNotLeaved, Rolled, PlayerAdded
from player import Player


class Game:
    def __init__(self):
        self._events = []
        self._players: list[Player] = []

        self.current_player_index = 0
        self.is_getting_out_of_penalty_box = False

        pop_questions = []
        science_questions = []
        sports_questions = []
        rock_questions = []

        for i in range(50):
            pop_questions.append("Pop Question %s" % i)
            science_questions.append("Science Question %s" % i)
            sports_questions.append("Sports Question %s" % i)
            rock_questions.append("Rock Question %s" % i)

        self._deck = {
            'Pop': pop_questions,
            'Science': science_questions,
            'Sports': sports_questions,
            'Rock': rock_questions,
        }

    def add(self, player_name):
        self._players.append(Player(player_name))

        self._dispatch_player_added(player_name)

    def roll(self, roll):
        self._dispatch_rolled(roll)

        if self._player().in_penalty_box():
            roll_is_even = roll % 2 == 0
            if roll_is_even:
                self._dispatch_penalty_box_not_leaved()
                self.is_getting_out_of_penalty_box = False
            else:
                self.is_getting_out_of_penalty_box = True
                self._dispatch_penalty_box_leaved()

        if not self._player().in_penalty_box() or self.is_getting_out_of_penalty_box:
            self._player().move(roll)
            self._dispatch_player_moved()
            self._ask_question()

    def _player(self):
        return self._players[self.current_player_index]

    def _ask_question(self):
        question = self._deck[self._current_category].pop(0)
        self._events.append(QuestionAsked(question))

    @property
    def _current_category(self):
        categories = ['Pop', 'Science', 'Sports', 'Rock']
        category_index = self._player().position() % len(categories)
        return categories[category_index]

    def answer_correctly(self):
        if self._player().in_penalty_box() and not self.is_getting_out_of_penalty_box:
            self._select_next_player()
        else:
            self._player().add_coin()
            self._dispatch_answered_correctly()
            self._select_next_player()

    def _select_next_player(self):
        self.current_player_index += 1
        if self.current_player_index == len(self._players):
            self.current_player_index = 0

    def answer_incorrectly(self):
        self._dispatch_answered_incorrectly()
        self._player().move_in_penalty_box()
        self._select_next_player()

    def has_winner(self) -> bool:
        for player in self._players:
            if player.has_won():
                return True
        return False

    def _dispatch_player_added(self, player_name):
        self._events.append(PlayerAdded(player_name, len(self._players)))

    def _dispatch_penalty_box_not_leaved(self):
        self._events.append(PenaltyBoxNotLeaved(self._player().name()))

    def _dispatch_player_moved(self):
        self._events.append(PlayerMoved(self._player().name(), self._player().position(), self._current_category))

    def _dispatch_penalty_box_leaved(self):
        self._events.append(PenaltyBoxLeaved(self._player().name()))

    def _dispatch_rolled(self, roll):
        self._events.append(Rolled(self._player().name(), roll))

    def _dispatch_answered_correctly(self):
        self._events.append(AnsweredCorrectly(self._player().name(), self._player().coins()))

    def _dispatch_answered_incorrectly(self):
        self._events.append(AnsweredIncorrectly(self._player().name()))

    def pop_events(self):
        r = self._events
        self._events = []
        return r
