import os
import shutil


def main():
    f = open("lawnmower.txt", 'r')
    for line in f.readlines():
        newLine = line.strip("\n")
        shutil.rmtree(newLine)
    os.remove("lawnmower.txt")

