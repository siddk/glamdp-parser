import io
import argparse
import sys

# build the labels
train_sentences = {}
classes = 0
labelsDict = {}
with io.open('train.bdm', 'r', encoding='utf-8') as trainfile:
    while True:
        sentence = trainfile.readline()
        if sentence == '':
            break
        tasks = []
        for i in xrange(3):
            start = trainfile.readline()[:-1]
            end = trainfile.readline()[:-1]
            tasks.append(end)
            trainfile.readline()
            trainfile.readline()
        label = -1
        for task in tasks:
            if task in labelsDict:
                label = labelsDict[task]
        if label == -1:
            label = classes
            classes += 1
        for task in tasks:
            if not task in labelsDict:
                labelsDict[task] = label
        train_sentences[sentence] = label
print len(train_sentences)

# label the test data
test_sentences = {}
with io.open('test.bdm', 'r', encoding='utf-8') as testfile:
    while True:
        sentence = testfile.readline()
        if sentence == '':
            break
        tasks = []
        for i in xrange(3):
            start = testfile.readline()[:-1]
            end = testfile.readline()[:-1]
            tasks.append(end)
            testfile.readline()
            testfile.readline()
        label = -1
        for task in tasks:
            if task in labelsDict:
                label = labelsDict[task]
        if label == -1:
            label = classes
            classes += 1
        test_sentences[sentence] = label
print len(test_sentences)
with io.open('train.txt', 'w', encoding='utf-8') as trainfile:
    for s, l in train_sentences.iteritems():
        trainfile.write(s)
        trainfile.write(unicode(str(l) + "\n"))
with io.open('test.txt', 'w', encoding='utf-8') as testfile:
    for s, l in test_sentences.iteritems():
        testfile.write(s)
        testfile.write(unicode(str(l) + "\n"))
