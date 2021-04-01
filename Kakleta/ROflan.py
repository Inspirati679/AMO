import math

x1, y1, x2, y2, x3, y3 = int(input()), int(input()), int(input()), int(input()), int(input()), int(input())
l1 = y1 - x1
l2 = y2 - x2
l3 = y3 - x3
s = 1
l = []
l4 = []

for i in range(3):
    l.append(globals()["l" + str(i + 1)])
    l4.append(globals()["l" + str(i + 1)])
counter2 = 0

for j in range(3):
    main = []
    for i in range(3):
        main.append([globals()["x" + str(i + 1)], globals()["y" + str(i + 1)]])
    if ( ):
        break

    else:
        t = min(l)
        counter = 0
        for i in range(len(l)):
            if l[i] == t:
                counter = i
        del main[counter]
        if main[1][0] - main[0][1] < t:
            for m in range(len(l4)):
                if l4[m] == t:
                    t5 = m
            print(t5 + 1)
            s = 0
            break
        del l[counter]
        counter2 += 1
if s == 1:
    print(0)
