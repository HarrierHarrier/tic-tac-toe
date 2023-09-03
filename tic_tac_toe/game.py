import random

from board import Board
from player import ComputerPlayer, HumanPlayer

class Game:
    def __init__(self) -> None:
        self.board = Board()
        self.opponents = [
            HumanPlayer(), ComputerPlayer()
        ]
        self.choose_sides()

    def choose_sides(self) -> None:
        """Выбор порядка ходов игроков."""
        # Случайное изменение порядка игроков и присвоение меток
        random.shuffle(self.opponents)
        for player, mark in zip(self.opponents, ('X', 'O')):
            player.mark = mark
        # Сообщение о порядке ходов
        if self.opponents[0].__class__ is ComputerPlayer:
            message = "Первым ходит компьютер."
        else:
            message = "Первый ход - ваш."
        print(message)
