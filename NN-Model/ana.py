from itertools import islice

dupMap = {}
edited = 0
editedNotDirect = 0
runCount = 0
indexList = {}
qsMap = {}

supFile = open('data/train.sup', 'w')
newQN = 404290


sum = 0
with open('data/train.csv') as fo:
    line = fo.readline()
    lineN = 0
    for line in islice(fo, 1, None):
        # if lineN == 15000:
        #     break

        try:
            lineN += 1
            print(lineN)

            dId, q1Id, q2Id, q1, q2, isDup = line.split('","')
            q1Id = int(q1Id)
            q2Id = int(q2Id)
            qsMap[q1Id] = q1 if q1Id not in qsMap else qsMap[q1Id]
            qsMap[q2Id] = q2 if q2Id not in qsMap else qsMap[q2Id]

            isDup = bool(isDup[0] == "1")
            if isDup:
                sum+=1 if isDup else 0

        except:
            print(line.split('","'))

# add_dup(1, 3)
# add_dup(4, 5)
# add_dup(2, 7)
# add_dup(3, 8)
# add_dup(1, 10)
# add_dup(3, 11)
# add_dup(4, 11)
# add_dup(15, 1)

# infer(list(dupMap.keys()))
# print('edited: %d' % edited)
# print('editedNotDirect: %d' % editedNotDirect)
# print('runCount: %d' % runCount)
print(sum/lineN)

supFile.close()
# print(dupMap)
