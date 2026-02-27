import argparse


def arg_parser():
    parser = argparse.ArgumentParser(description="A cli tool for generating characters")
    parser.add_argument("name", help="Character's name")

    return parser.parse_args()
