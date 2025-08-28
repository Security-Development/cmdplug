from argparse import ArgumentParser, Namespace
from cmdplug import Command, __command_init__

class Calculator(Command):
    NAME="calculator"
    HELP="for example"

    @classmethod
    def add_arguments(cls, parser: ArgumentParser):
        parser.add_argument("-x", "--x", help="x variable", type=int)
        parser.add_argument("-y", "--y", help="y variable", type=int)

    def run(self, args: Namespace) -> int:
        x, y = args.x, args.y
        print(f"x({x}) + y({y}) = {args.x + args.y}")
        return 0
    
if __name__ == "__main__":
    __command_init__()