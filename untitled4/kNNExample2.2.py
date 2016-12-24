from numpy import *
originalDataSet = [[4, 2, 1], [2, 5, 6], [-1 , 8, 10], [4, 2, 1], [2, 5, 6], [-1 , 8, 10]]
originalLabelTypes = ['normal', 'good', 'great']
originalLabels = ['normal', 'good', 'great', 'normal', 'good', 'great']
newVector = [-10, 10, 12]
precision = 1

def findDistances():
    distances=[0 for i in range(len(originalDataSet))]
    for i in range(len(originalDataSet)):
        tempDist = 0
        for j in range(len(newVector)):
            tempDist = tempDist + (newVector[j]-originalDataSet[i][j])**2
        distances[i]=tempDist**(0.5)
    return distances

def sortDistancesAndSortLabels(distances):
    newSortedLabels=["null" for i in range(len(originalLabels))]
    distances=array(distances).argsort()
    print(distances)
    for i in range(len(newSortedLabels)):
        newSortedLabels[distances[i]]=originalLabels[i]
    return newSortedLabels

def findMaximal(labels):
    highestCount = 0
    highestCountIndex = 1000
    for i in range(len(originalLabelTypes)):
        tempCount = 0
        for j in range(len(labels)):
            if labels[j] == originalLabelTypes[i]:
                tempCount = tempCount + 1
        if highestCount < tempCount:
            highestCount = tempCount
            highestCountIndex = i

    return originalLabelTypes[highestCountIndex]

print(findDistances())
print(sortDistancesAndSortLabels(findDistances()))
print(findMaximal(sortDistancesAndSortLabels(findDistances())))