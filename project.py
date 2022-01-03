import csv
import math
from numpy import square
import pandas as pd
import plotly.express as px

with open(r'C:\Users\lenovo\Desktop\Python\Class 105\data.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)
    d=file_data.pop(0)

number=len(d)

def findMean(data):
    total = 0
    mean = 0
    number = len(data)
    for marks in data:
        total = total+int(marks[1])
    mean = float(total/number)
    print("The Mean is", mean)
    return mean

def drawGraph(mean):
    df = pd.read_csv(r"C:\Users\lenovo\Desktop\Python\Class 105\data.csv")
    fig = px.scatter(df, x="Student_Number", y="Marks")
    fig.update_layout(
        shapes=[dict(type='line', x0=0, x1=number, y0=mean, y1=mean)])
    fig.update_yaxes(rangemode="tozero")
    fig.show()

def standardDeviation(mean):
    squaredList=[]
    for marks in file_data:
        dif=int(int(marks[1])-mean)
        sq=dif*dif
        squaredList.append(sq)
    total=0
    for marks in squaredList:
        total = total+marks
    result=total/(number-1)
    st_d=math.sqrt(result)
    print(st_d)

def main():
    a=findMean(file_data)
    #drawGraph(a)
    standardDeviation(a)
main()