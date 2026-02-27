#!/usr/bin/env python3

from rpg_char_gen.parser import arg_parser


def main():
    print(arg_parser().name)
    print("Hi world")


if __name__ == "__main__":
    main()
