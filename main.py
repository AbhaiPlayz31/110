import plotly.figure_factory as ff
import pandas as pd 
import statistics 
import random
import csv
import plotly.graph_objects as go

df = pd.read_csv('data.csv')



data = df['temp'].tolist()


def randomSetOfMean(counter):

    dataSet = []

    for i in range(0,counter):
        randomIndex = random.randint(0, len(data)-1)
        value = data[randomIndex]
        dataSet.append(value)
    
    sampleMean = statistics.mean(dataSet)

    return sampleMean


def showFig(meanList):
    df = meanList
    fig = ff.create_distplot([df], ['temp'], show_hist=False)
    mean = statistics.mean(meanList)
    print('Mean is:', mean)
    fig.add_trace(go.Scatter(x=[mean,mean], y=[0,1], mode='lines', name='mean'))
    fig.show()

def setUp():
    meanList=[]

    for i in range(0,1000):
        SetOfMean = randomSetOfMean(100)
        meanList.append(SetOfMean)
    showFig(meanList)



setUp()



sampleSTD = statistics.stdev(dataSet)






