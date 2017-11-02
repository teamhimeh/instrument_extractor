from enum import Enum
import numpy as np
from numpy.random import *
import argparse

class Onkai(Enum):
    C = 0
    C_s = 1
    D = 2
    D_s = 3
    E = 4
    F = 5
    F_s = 6
    G = 7
    G_s = 8
    A = 9
    A_s = 10
    B = 11

def gen_score(len_bar):
    arr = [[Onkai(randint(12)) for _ in range(12)] for i in range(len_bar)]
    #arr = []
    #for i in range(len_bar):
    #    arr.append([])
    #    for h in range(12):
    #        arr[i].append(Onkai(randint(12)))
    return arr

def main():
    arr = gen_score(32)
    filelist = {Onkai.C:'c', Onkai.C_s:'cs',Onkai.D:'d', Onkai.D_s:'ds',Onkai.E:'e', Onkai.F:'f', Onkai.F_s:'fs',Onkai.G:'g', Onkai.G_s:'gs',Onkai.A:'a', Onkai.A_s:'as',Onkai.B:'b'}
    wav_arr = []
    pos = 0.0
    for bar in arr:
        for sound in bar:
            wav_arr.append([pos,filelist[sound]])
            pos += 60.0/(160*12)
    print(wav_arr)

if __name__ == '__main__':
    main()
