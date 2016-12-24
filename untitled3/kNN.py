#All you had to do was follow the damn train, CJ !

from numpy import *
import operator

group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1], [2, 3], [3, 4]])
labels = ['A', 'A', 'B', 'B', 'C', 'C']
types = ['A', 'B', 'C']
newVector=[2, 2]
distancesToConsider=3                                           #Basically the accuracy of the probablity and a little accuracy of the overall result,
                                                                #don't make it larger than len(labels) or even getting it closer to that may cause
                                                                #wrong or inaccurate results. try to keep it at max of len(labels)/2

def createDataSet():
	return group, labels

def findDistances(group, newVector):
	distances = [0 for i2 in range(len(group))]
	for i in range(0, len(group), 1):
		d=((newVector[0]-group[i][0])**2+(newVector[1]-group[i][1])**2)**(0.5)
		distances[i]=d
	return distances

def sortClassWithDistances(labels, distances, distancesToConsider):
    sortedLabels = [')' for i in range(distancesToConsider)]
    for i in range(distancesToConsider):
        lowestTemp = 1000
        lowestTempIndex = 0
        for j in range(len(distances)):
            if lowestTemp>distances[j]:
                lowestTemp=distances[j]
                lowestTempIndex = j
        distances[lowestTempIndex]=1000
        sortedLabels[i] = labels[lowestTempIndex]
    return sortedLabels

def findMajorityLabel(labels, types):
    highestCount=0
    highestCountIndex=1000
    for i in range(len(types)):
        tempCount=0
        for j in range(len(labels)):
            if labels[j]==types[i]:
                tempCount=tempCount+1
        if highestCount<tempCount:
            highestCount=tempCount
            highestCountIndex=i
    probablity = highestCount/len(labels)

    return types[highestCountIndex], probablity

group, labels = createDataSet()
# print(group, '\n', labels)
distances =findDistances(group, newVector)

distances = array(distances)
# print(distances)
sortedLabelIndicies = sortClassWithDistances(labels, distances, distancesToConsider)
# print(sortedLabelIndicies)

majorityElement, probablity=findMajorityLabel(sortedLabelIndicies, types)
print(majorityElement, "with probablity of ", probablity*100)
