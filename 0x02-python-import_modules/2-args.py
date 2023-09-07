#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    arglen = len(argv)
    if arglen == 1:
        print("0 arguments.")
    elif arglen == 2:
        print("1 argument:")
        print("1: {}".format(argv[1]))
    else:
        print("{} arguments:".format(arglen - 1))
        for i in range(1, arglen):
            print("{:d}: {}".format(i, argv[i]))
