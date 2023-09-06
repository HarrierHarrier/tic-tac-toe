# Tic tac toe

Консольная игра в крестики-нолики с компьютером.

## Запуск

Для запуска игры нужно запустить исполняемый файл `run.sh`.

## Управление

Во время своего хода нужно вводить координаты клетки, чтобы поставить свою метку. Первое число - номер строки, второе - номер столбца, нумерация начинается с 1. Например, координаты `1, 3` означают вот эту клетку:

```
-------------
|   |   | X |
-------------
|   |   |   |
-------------
|   |   |   |
-------------
```

Если ввод будет некорректным или клетка уже занята, будет выведено соответствующее сообщение, и координаты будут запрошены ещё раз.

Чтобы выйти из игры до её завершения, вместо координат нужно ввести `q`.
