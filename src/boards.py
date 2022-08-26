from abc import ABC, abstractmethod


class Board(ABC):
    @abstractmethod
    def is_game_over(self) -> bool:
        pass

class NormalBoard(Board):
    def is_game_over(self) -> bool:
        return False