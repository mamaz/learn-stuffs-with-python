from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("number", help="input the number", type=int)
parser.add_argument("--echo",help="echo the string you put in here")
args = parser.parse_args()

if args.number is not None:
    print(args.number)
else:
    print("a number is needed")
