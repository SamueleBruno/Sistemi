import math


def QuadratiP(x):
    for numero in range(x):

        i=0

        while (i*i <= numero):

            i = i + 1

            if (i*i  == numero):

                print(i*i)

x = 200
QuadratiP(x)