import random

while(True):
    stop = 10000

    m = random.randrange(5, stop)
    stop = m
    l = random.randrange(4, stop)
    stop = l
    t = random.randrange(3, stop)
    stop = t
    c = random.randrange(2, stop)

    if not (m > l and l > t and t > c):
        print("Utilities out of order")
        exit()

    print("m=%d" % (m))
    print("l=%d" % (l))
    print("t=%d" % (t))
    print("c=%d" % (c))

    o1 = t*0.3+m*0.7
    o2 = c*0.3+l*0.2+m*0.5
    print("O1: %f" % (o1))
    print("O2: %f" % (o2))

    if o1 <= o2:
        print("Expected utilities out of order")
        exit()
