import sys

args = sys.argv

if "--help" in args:
    print("This program lists all arguments")
    exit()

for arg in args:
    print(arg)
