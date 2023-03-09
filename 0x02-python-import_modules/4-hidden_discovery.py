#!/usr/bin/python3
from hidden_4 import *

if __name == "__main__":
    arr = dir()
    for i in range(0, len(arr)):
        if arr[i][0:2] != "__":
            print("{}".format(arr[i]))
