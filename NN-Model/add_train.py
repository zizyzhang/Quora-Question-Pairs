from itertools import islice
import random

dupMap = {}
edited = 0
editedNotDirect = 0
runCount = 0
indexList = {}
qsMap = {}

supFile = open('data/train.sup', 'w')
newQN = 404290


def add_dup(q1, q2):
    if q1 == q2:
        return
    if q1 not in dupMap:
        dupMap[q1] = []
        indexList[q1] = 0
    if q2 not in dupMap[q1]:
        dupMap[q1].append(q2)


def infer(infer_list):
    global edited, editedNotDirect, runCount, newQN
    changed = False
    infer_list_new = []
    for key in infer_list:
        value = dupMap[key]
        for dupItem in value:
            if dupItem not in dupMap:
                dupMap[dupItem] = []
                indexList[dupItem] = 0
            if (key not in dupMap[dupItem]) and (dupItem != key):
                dupMap[dupItem].append(key)
                edited += 1
                changed = True
                if key not in infer_list_new:
                    infer_list_new.append(key)
            for ch1 in range(len(dupMap[key])):
                for ch2 in range(ch1 + indexList[key], len(dupMap[key])):
                    runCount += 1
                    if dupMap[key][ch1] not in dupMap:
                        dupMap[dupMap[key][ch1]] = []
                        indexList[dupMap[key][ch1]] = 0

                    if (dupMap[key][ch2] not in dupMap[dupMap[key][ch1]]) and (dupMap[key][ch1] != dupMap[key][ch2]):
                        dupMap[dupMap[key][ch1]].append(dupMap[key][ch2])
                        changed = True
                        if dupMap[key][ch1] not in infer_list_new:
                            infer_list_new.append(dupMap[key][ch1])
                        edited += 1
                        editedNotDirect += 1
                        if (dupMap[key][ch2] not in dupMap) or (
                                (dupMap[key][ch2] in dupMap) and (dupMap[key][ch1] not in dupMap[dupMap[key][ch2]])):
                            supFile.write('"%d","%d","%d","%s","%s","1"\n' % (
                                newQN, dupMap[key][ch2], dupMap[key][ch1], qsMap[dupMap[key][ch2]],
                                qsMap[dupMap[key][ch1]]))
                            newQN += 1
            indexList[key] = len(dupMap[key])
    if changed:
        infer(infer_list_new)


def add_neg():
    global newQN
    qNum = 0
    while qNum < 137000:
        q1_id = int(random.random() * 400000)
        q2_id = int(random.random() * 400000)

        if (q1_id in qsMap) and (q2_id in qsMap) and (q1_id in dupMap) and (q2_id not in dupMap[q1_id]):

                supFile.write('"%d","%d","%d","%s","%s","0"\n' % (
                    newQN, q1_id, q2_id, qsMap[q1_id],
                    qsMap[q2_id]))
                newQN += 1
                qNum += 1


with open('data/train.csv', encoding="utf-8") as fo:
    line = fo.readline()
    lineN = 0
    for line in islice(fo, 1, None):
        # if lineN == 15000:
        #     break

        try:
            lineN += 1
            if lineN % 50000 == 0:
                print(lineN)

            dId, q1Id, q2Id, q1, q2, isDup = line.split('","')
            q1Id = int(q1Id)
            q2Id = int(q2Id)
            qsMap[q1Id] = q1 if q1Id not in qsMap else qsMap[q1Id]
            qsMap[q2Id] = q2 if q2Id not in qsMap else qsMap[q2Id]

            isDup = bool(isDup[0] == "1")
            if isDup:
                add_dup(q1Id, q2Id)

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

infer(list(dupMap.keys()))
add_neg()
print('edited: %d' % edited)
print('editedNotDirect: %d' % editedNotDirect)
print('runCount: %d' % runCount)
supFile.close()
# print(dupMap)
