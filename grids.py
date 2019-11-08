from sudoku import Cell

easy_13553 = Cell.build(
    (1, 0, 1),
    (2, 0, 2),
    (3, 0, 3),
    (4, 0, 7),
    (5, 0, 9),
    (1, 4, 6),
    (1, 6, 1),
    (1, 7, 3),
    (2, 3, 5),
    (2, 6, 7),
    (3, 1, 6),
    (3, 2, 9),
    (3, 3, 8),
    (3, 4, 4),
    (3, 7, 2),
    (4, 1, 7),
    (4, 2, 8),
    (4, 6, 9),
    (4, 7, 1),
    (5, 1, 3),
    (5, 4, 1),
    (5, 5, 7),
    (5, 6, 4),
    (5, 7, 8),
    (6, 2, 1),
    (6, 5, 5),
    (7, 1, 9),
    (7, 2, 4),
    (7, 4, 2),
    (7, 8, 1),
    (8, 3, 1),
    (8, 4, 9),
    (8, 5, 6),
    (8, 6, 8),
    (8, 7, 5),
)

original = Cell.build(
    (1, 0, 2),
    (3, 0, 1),
    (5, 0, 5),
    (8, 0, 6),
    (0, 1, 1),
    (4, 1, 9),
    (5, 1, 2),
    (6, 1, 8),
    (7, 1, 5),
    (0, 2, 3),
    (2, 2, 5),
    (4, 2, 8),
    (2, 3, 7),
    (3, 3, 8),
    (6, 3, 5),
    (8, 3, 2),
    (0, 4, 4),
    (4, 4, 2),
    (8, 4, 9),
    (0, 5, 6),
    (2, 5, 2),
    (5, 5, 3),
    (6, 5, 4),
    (4, 6, 1),
    (6, 6, 7),
    (8, 6, 3),
    (1, 7, 8),
    (2, 7, 3),
    (3, 7, 6),
    (4, 7, 4),
    (8, 7, 5),
    (0, 8, 2),
    (3, 8, 5),
    (5, 8, 7),
    (7, 8, 8),
)

easy_120879 = Cell.build(
    (0, 1, 4),
    (0, 5, 3),
    (0, 8, 7),
    (1, 0, 3),
    (1, 2, 8),
    (1, 3, 7),
    (1, 5, 4),
    (1, 6, 6),
    (1, 7, 2),
    (2, 4, 5),
    (3, 1, 8),
    (3, 2, 5),
    (3, 5, 9),
    (3, 6, 4),
    (3, 8, 3),
    (4, 0, 4),
    (4, 1, 7),
    (4, 3, 6),
    (4, 5, 8),
    (4, 7, 5),
    (4, 8, 1),
    (5, 0, 6),
    (5, 2, 2),
    (5, 3, 1),
    (5, 6, 7),
    (5, 7, 9),
    (6, 9, 9),
    (7, 6, 6),
    (7, 7, 7),
    (7, 3, 3),
    (7, 1, 1),
    (7, 9, 9),
    (7, 5, 5),
    (8, 9, 9),
    (8, 5, 5),
    (8, 3, 3),
)

normal_225676 = Cell.build(
    (0, 0, 3),
    (0, 1, 6),
    (0, 3, 8),
    (0, 5, 7),
    (0, 8, 2),
    (1, 4, 2),
    (1, 6, 4),
    (1, 7, 8),
    (2, 1, 9),
    (2, 5, 3),
    (2, 6, 5),
    (3, 0, 6),
    (3, 1, 3),
    (3, 3, 9),
    (4, 1, 8),
    (4, 7, 7),
    (5, 5, 8),
    (5, 7, 4),
    (5, 8, 5),
    (6, 2, 6),
    (6, 3, 3),
    (6, 7, 5),
    (7, 1, 4),
    (7, 2, 8),
    (7, 4, 9),
    (8, 0, 5),
    (8, 3, 1),
    (8, 5, 4),
    (8, 7, 2),
    (8, 8, 9),
)

hard_3215 = Cell.build(
    (0, 3, 1),
    (0, 4, 9),
    (0, 5, 8),
    (0, 7, 7),
    (1, 5, 3),
    (1, 6, 1),
    (1, 7, 5),
    (2, 0, 1),
    (2, 8, 6),
    (3, 4, 1),
    (3, 6, 7),
    (3, 8, 5),
    (4, 1, 7),
    (4, 7, 8),
    (5, 0, 3),
    (5, 2, 4),
    (5, 4, 8),
    (6, 0, 5),
    (6, 8, 7),
    (7, 1, 8),
    (7, 2, 1),
    (7, 3, 2),
    (8, 1, 9),
    (8, 3, 8),
    (8, 4, 4),
    (8, 5, 5),
)

very_hard_423464 = Cell.build(
    (0, 1, 2),
    (0, 3, 1),
    (0, 4, 5),
    (0, 6, 8),
    (1, 5, 3),
    (1, 7, 2),
    (2, 4, 7),
    (2, 6, 5),
    (2, 8, 1),
    (3, 0, 8),
    (3, 2, 7),
    (3, 7, 5),
    (4, 0, 3),
    (4, 8, 7),
    (5, 1, 5),
    (5, 6, 4),
    (5, 8, 6),
    (6, 0, 2),
    (6, 2, 3),
    (6, 4, 8),
    (7, 1, 6),
    (7, 3, 3),
    (8, 2, 8),
    (8, 4, 6),
    (8, 5, 1),
    (8, 7, 4),
)

impossible_521901 = Cell.build(
    (0, 2, 4),
    (0, 4, 9),
    (1, 2, 8),
    (1, 5, 6),
    (1, 6, 7),
    (1, 7, 9),
    (2, 0, 2),
    (2, 1, 6),
    (2, 6, 4),
    (2, 7, 5),
    (3, 3, 9),
    (3, 5, 7),
    (3, 7, 8),
    (4, 0, 8),
    (4, 4, 3),
    (4, 8, 2),
    (5, 1, 5),
    (5, 3, 2),
    (5, 5, 8),
    (6, 1, 4),
    (6, 2, 2),
    (6, 7, 1),
    (6, 8, 5),
    (7, 1, 8),
    (7, 2, 6),
    (7, 3, 5),
    (7, 6, 3),
    (8, 4, 7),
    (8, 6, 8),
)
