import sys
import random
import argparse
import guess
import Uptoloop
parser = argparse.ArgumentParser(
        description="A guessing game"
    )
parser.add_argument(
        "-n","--name",metavar="Name",
        required=True,help="Name of the player"
)
args = parser.parse_args()
def arc():
    x=input(f"{args.name} enter 1 to play rock paper scissors \n2 to play guessing game \nand x to quit:")
    if x == '1':
        Uptoloop.rps(args.name)
    elif x == '2':
        guess.say(args.name)
    else:
        print("program exited")
        sys.exit

if __name__ == '__main__':
    arc()