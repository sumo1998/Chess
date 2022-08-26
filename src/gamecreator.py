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
from typing import TypeVar

from game import Game, NormalGame

G = TypeVar("G",bound=Game)
class GameCreator(ABC):
    
    @classmethod
    @abstractmethod
    def setup() -> G:
        """
        Return appropriate game, any additonal processing logic goes here
        """
        raise NotImplementedError


class NormalGameCreator(GameCreator):
    def setup() -> G:
        return NormalGame()
        

