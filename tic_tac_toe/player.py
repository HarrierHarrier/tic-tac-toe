import random
import sys

from tic_tac_toe.board import Board, CellValue


class BasePlayer:
    """Базовый класс игрока."""
    def __init__(self) -> None:
        self.mark: str | None = None
        self.target_row: int | None = None
        self.target_col: int | None = None

    def choose_cell(self, board: Board) -> None:
        """Выбор игроком клетки.

        Игрок-пользователь смотрит на поле в консольном выводе и сообщает о
        своём выборе через ввод.

        Игрок-компьютер ищет пустые клетки на поле и выбирает случайную из
        них.
        """
        pass

    def make_move(self, board: Board) -> None:
        """Совершение хода игроком."""
        print(f"Ход {self}")
        # Выбор клетки
        self.choose_cell(board)
        # Сообщение игровому полю о решении
        board.accept_move(
            row=self.target_row, col=self.target_col, mark=self.mark
        )

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}, mark '{self.mark}'"


class HumanPlayer(BasePlayer):
    """Подкласс игрока-пользователя."""
    def choose_cell(self, board: Board) -> None:
        print(
            "Введите координаты ячейки через запятую. Сначала номер строки,"
            " затем номер столбца."
        )
        # Получение координаты ячейки
        while True:
            user_input = input("Ваш выбор:  ")
            # Обработка команды на выход
            if user_input == 'q':
                print("До следующего раза!")
                sys.exit()
            coordinates = user_input.split(',')
            if len(coordinates) != 2:
                print(
                    "Нужно ввести два значения, разделённых запятой."
                    " Попробуйте ещё раз."
                )
                continue
            try:
                coordinates = [int(item.strip()) - 1 for item in coordinates]
                # Проверка того, что клетка находтся на поле
                if any(value >= board.size for value in coordinates):
                    print(
                        "Значения координат не должны превышать размера"
                        " игрового поля. Попробуйте ещё раз."
                    )
                    continue
                # Проверка, что клетка не занята
                board_cell = board.cells[coordinates[0]][coordinates[1]]
                if board_cell.value != CellValue.empty:
                    print(
                        "Эта клетка уже занята. Попробуйте ещё раз."
                    )
                    continue
                self.target_row, self.target_col = coordinates
                break
            except ValueError:
                print(
                    "Значения должны быть целыми числами. Попробуйте ещё раз."
                )


class ComputerPlayer(BasePlayer):
    """Подкласс игрока-компьютера."""
    def choose_cell(self, board: Board) -> None:
        if len(board.empty_cells) == 0:
            raise Exception("No empty cells left.")
        # Выбор случайной пустой клетки
        random_cell = random.choice(board.empty_cells)
        self.target_row, self.target_col = random_cell.row, random_cell.col
