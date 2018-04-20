# import file as file
moreThan30Count = 0
moreThan35Count = 0
moreThan40Count = 0
moreThan45Count = 0
qs = 0
lineN = 0
with open('data/train.csv') as fo:
    line = fo.readline()

    for line in fo:
        try:
            lineN += 1
            if lineN == 1:
                continue
            print(lineN)
            line = fo.readline()
            a, b, c, q1, q2, f = line.split('","')
            q1WordsLen = len(q1.split(' '))
            q2WordsLen = len(q2.split(' '))
            moreThan30Count += 1 if q1WordsLen > 30 else 0
            moreThan35Count += 1 if q1WordsLen > 35 else 0
            moreThan40Count += 1 if q1WordsLen > 40 else 0
            moreThan45Count += 1 if q1WordsLen > 45 else 0
            moreThan30Count += 1 if q2WordsLen > 30 else 0
            moreThan35Count += 1 if q2WordsLen > 35 else 0
            moreThan40Count += 1 if q2WordsLen > 40 else 0
            moreThan45Count += 1 if q2WordsLen > 45 else 0
        except:
            print(line.split('","'))


print("moreThan30Count:%d, rate: %f"%(moreThan30Count,moreThan30Count/ lineN))
print("moreThan35Count:%d, rate: %f"%(moreThan35Count,moreThan35Count/ lineN))
print("moreThan40Count:%d, rate: %f"%(moreThan40Count,moreThan40Count/ lineN))
print("moreThan45Count:%d, rate: %f"%(moreThan45Count,moreThan45Count/ lineN))
