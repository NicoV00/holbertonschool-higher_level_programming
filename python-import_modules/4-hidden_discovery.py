#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    direc = dir(hidden_4)
    for name in direc:
        if not name.startswith("__"):
            print(name)
