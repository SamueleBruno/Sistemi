import random

def lancioDadi():

    f = open("casuali.txt", "w")

    l1=[random.randint(1, 6) for k in range(0, 10)]
    l2=[random.randint(1, 6) for k in range(0, 10)]

#for i in range(0, 10):
#    f.write(f"{l1[i]}, {l2[i]}\n")

    for n1, n2 in zip(l1, l2):
        f.write(f"{n1}, {n2}\n")


    f.close()

def main():
    lancioDadi()


if __name__ == "__main__":
    main()
