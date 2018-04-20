from itertools import islice

with open('glove.txt') as f:
        line = f.readline()
        print("features# in embedding:%d"%(len(line.split(" "))-1))
        for line in islice(f,100000,130000):
            print(line)

print("lines: 2196016")