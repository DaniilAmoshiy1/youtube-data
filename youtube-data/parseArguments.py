import argparse


def parser_args():
    parser = argparse.ArgumentParser(description='Parser for youtube links')

    parser.add_argument('url', type=str, help='URL плейлиста youtube')
    return parser.parse_args()

