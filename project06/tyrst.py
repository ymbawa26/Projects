
import sys
import elephant

def main(argv):

    for i in range(5):
        probDarting = 0.405 + i * 0.01
        print("Dating prob", probDarting)
        diff = elephant.elephantSim( probDarting )
        print("probDarting %.3f  diff %d" % (probDarting, diff))

    return

if __name__ == "__main__":
    main(sys.argv)