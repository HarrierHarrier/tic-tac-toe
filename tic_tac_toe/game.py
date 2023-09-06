import random
import sys

from board import Board
from player import BasePlayer, ComputerPlayer, HumanPlayer


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

    def check_victory(self, player: BasePlayer) -> None:
        conditions = (
            # Проверка строк
            any(
                all(cell.value == player.mark for cell in row)
                for row in self.board.cells
            ),
            # Проверка столбцов
            any(
                all(row[i].value == player.mark for row in self.board.cells)
                for i in range(self.board.size)
            ),
            # Проверка диагоналей
            any([
                all(
                    row[i].value == player.mark
                    for i, row in enumerate(self.board.cells)
                ),
                all(
                    row[-i].value == player.mark
                    for i, row in enumerate(self.board.cells, 1)
                )
            ])
        )
        if any(conditions):
            print(f"Игрок {player} выиграл!")
            sys.exit()

    def check_draw(self) -> None:
        if len(self.board.empty_cells) == 0:
            print("Ничья!")
            sys.exit()
