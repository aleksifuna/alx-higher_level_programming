#!/usr/bin/python3
for i in range(1, 100):
    if i == 1:
        print("{:02d}".format(i), end='')
    else:
        if i < int(str("{:02d}".format(i))[::-1]):
            print(", {:02d}".format(i), end='')
print()
