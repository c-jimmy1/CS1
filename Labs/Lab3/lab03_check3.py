import math

def next_bpop(bpop):
    new = math.floor((10 * bpop)/(1 + 0.1 * bpop)- 0.05 * bpop * fpop)
    return new

def next_fpop(fpop):
    new = math.floor(0.4 * fpop + 0.02 * fpop * bpop)
    return new

bpop = int(input("Number of bunnies ==> "))
print(bpop)
fpop = int(input("Number of foxes ==> "))
print(fpop)
i = 1
print("Year {0}: {1} {2}".format(i, bpop, fpop))

while i < 5:
    i+=1
    newbpop = next_bpop(bpop)
    newfpop= next_fpop(fpop)
    bpop = newbpop
    fpop = newfpop
    print("Year {0}: {1} {2}".format(i, bpop, fpop))




