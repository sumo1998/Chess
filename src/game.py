"""
    NormalBoard
    FishcerRandomBoard
    4 way Chess Board

    DIFFERENT
    - Squares change
    - Position of pieces change
    - Number of players change

    COMMON
    - setup the game
    - players
"""

from abc import ABC, abstractmethod
from time import sleep
from typing import TypeVar
from boards import Board, NormalBoard

B = TypeVar("B",bound=Board)

class Game(ABC):
    board: B
    @abstractmethod
    def setup(self) -> B:
        """
        Should create the appropriate board and any additional processing logic (Ex: Updating user history etc)
        """
        raise NotImplementedError

    async def start_game(self) -> None:
        """
        Starts the game
        """
        while not self.board.is_game_over():
            print("Game running ")
            sleep(1)


class NormalGame(Game):
    def __init__(self) -> None:
        super().__init__()
        self.board = self.setup()

    def setup(self) -> B:
        return NormalBoard()



    
        

