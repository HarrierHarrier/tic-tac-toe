import random
import sys

from tic_tac_toe.board import Board, Cell, CellValue


class Player:
    """Базовый класс игрока."""
    def __init__(self, mark: CellValue = ' ') -> None:
        self.mark = mark
        self.target_row: int | None = None
        self.target_col: int | None = None

    def choose_cell(self, board: Board) -> Cell:
        """Выбор игроком клетки."""
        pass

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}, mark '{self.mark}'"


class HumanPlayer(Player):
    """Подкласс игрока-пользователя."""
    def choose_cell(self, board: Board) -> Cell:
        """Игрок-пользователь смотрит на поле в консольном выводе и сообщает о
        своём выборе через ввод."""
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
                chosen_cell = board.cells[coordinates[0]][coordinates[1]]
                if chosen_cell.value != CellValue.empty:
                    print(
                        "Эта клетка уже занята. Попробуйте ещё раз."
                    )
                    continue
                return chosen_cell
            except ValueError:
                print(
                    "Значения должны быть целыми числами. Попробуйте ещё раз."
                )


class ComputerPlayer(Player):
    """Подкласс игрока-компьютера."""
    def choose_cell(self, board: Board) -> Cell:
        """Игрок-компьютер ищет пустые клетки на поле и выбирает случайную из
        них."""
        if len(board.empty_cells) == 0:
            raise Exception("No empty cells left.")
        # Выбор случайной пустой клетки
        chosen_cell = random.choice(list(board.empty_cells))
        return chosen_cell
