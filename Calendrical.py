import argparse
import Calendrical_functions as cf
from Calendrical_Classes import Year


def main():
    version = '1.0'
    parser = argparse.ArgumentParser(prog="Calendrical")
    parser.add_argument("year", help="the input year", type=int)
    parser.add_argument("-file", "--filename", type=str, default="calendar_output", help="set output file name")
    parser.add_argument("-v", "--version", action='version', version=version)
    args = parser.parse_args()
    feed_array = [args.year - 1, args.year, args.year + 1]
    cf.html_writer(feed_array, args.filename)


if __name__ == "__main__":
    main()
