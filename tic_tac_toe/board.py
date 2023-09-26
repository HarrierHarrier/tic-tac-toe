from enum import Enum


class CellValue(str, Enum):
    empty = ' '
    cross = 'X'
    naught = 'O'


class Cell:
    """Клетка игрового поля."""
    def __init__(self, row: int, col: int, value: str) -> None:
        self.row = row
        self.col = col
        self.value = CellValue(value)

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}({self.row}, {self.col}, {self.value})"
        )


class Board:
    """Игровое поле."""
    def __init__(self, size: int = 3) -> None:
        self.size = size
        # Генерация пустых клеток поля
        self.cells = [
            [Cell(i, j, ' ') for j in range(self.size)]
            for i in range(self.size)
        ]

    def display(self) -> None:
        """Выводит поле в текущем состоянии."""
        border_length = self.size * 4 + 1
        print('-' * border_length)
        for row in self.cells:
            print('|', ' | '.join(item.value for item in row), '|')
            print('-' * border_length)

    def accept_move(self, row: int, col: int, mark: str) -> None:
        """Записывает изменения на игровое поле."""
        self.cells[row][col].value = CellValue(mark)

    @property
    def empty_cells(self) -> list[list[Cell]]:
        return [
            cell for row in self.cells for cell in row
            if cell.value == CellValue.empty
        ]
