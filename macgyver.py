#! /.envPy3 python3
# -*- coding: utf-8 -*-

"""
* MacGyver Game Labyrinthe *
Game in which to move MacGyver to recover.
All treasures through a labyrinth and join the guard.

If all the treasures have not been recovered before joining the guard
MacGyver dies.

"""

from class_mod.game import Game


def main():
    gui = Game()
    gui.mainloop()


if __name__ == '__main__':
    main()
