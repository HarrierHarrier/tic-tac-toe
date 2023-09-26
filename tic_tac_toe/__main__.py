from tic_tac_toe.game import Game


def greet_user() -> None:
    """Приветственное сообщение пользователю."""
    print(
        'Добро пожаловать в игру "Крестики-нолики"!'
        '\nЧтобы выйти из игры, введите символ "q".'
    )


def main():
    # Вступительное сообщение
    greet_user()
    # Начало партии
    game = Game()
    while True:
        # Ходы сторон
        for player in game.opponents:
            # Ход текущего игрока
            player.make_move(game.board)
            # Отображение текущего состояния игрового поля
            game.board.display()
            # Проверка условия победы
            game.check_victory(player=player)
            # Проверка ничьей
            game.check_draw()


if __name__ == '__main__':
    main()
