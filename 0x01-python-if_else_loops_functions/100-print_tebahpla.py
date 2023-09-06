#!/usr/bin/python3
for i in range(122, 96, -1):
    if i % 2 == 0:
        conversion = 0
    else:
        conversion = 32
    print("{:c}".format(i - conversion), end='')
