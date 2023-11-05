from dataclasses import dataclass


@dataclass(frozen=True)
class AnsweredCorrectly:
    player_name: str
    player_coins: int


@dataclass(frozen=True)
class AnsweredIncorrectly:
    player_name: str


@dataclass(frozen=True)
class QuestionAsked:
    question: str


@dataclass(frozen=True)
class PlayerMoved:
    player_name: str
    player_position: int
    question_category: str


@dataclass(frozen=True)
class PenaltyBoxLeaved:
    player_name: str


@dataclass(frozen=True)
class PenaltyBoxNotLeaved:
    player_name: str


@dataclass(frozen=True)
class Rolled:
    player_name: str
    roll: int


@dataclass(frozen=True)
class PlayerAdded:
    player_name: str
    players_count: int
