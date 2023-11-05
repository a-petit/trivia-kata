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
