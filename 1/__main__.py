#!/usr/bin/python3

import curses
import typer

from command import command_mode
from cmdline import CmdLine
from game    import Game
from hello   import Hello
from sys     import stderr
from itertools import product


# init
def main(height: int, width: int):
  #  try:
  Game(height, width).run()
  #  except Exception as e:
    #  print(e, file=stderr)
    #  exit(1)
  exit(0)


if __name__ == '__main__':
  typer.run(main)
