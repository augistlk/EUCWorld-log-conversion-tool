import pandas
import globalValues

def convertDateTime(readData: pandas.DataFrame, writeData: pandas.DataFrame):
    dateTime= readData["datetime"]
    dateColumn = pandas.Series([""])
    timeColumn = pandas.Series([""])

    i=0
    for x in dateTime:
        date=x[:10]
        time=x[11:23]
        dateColumn.loc[i] = date
        timeColumn.loc[i] = time
        i+=1
    
    writeData.insert(0,globalValues.WheelLogColumns[0], dateColumn)
    writeData.insert(1,globalValues.WheelLogColumns[1], timeColumn)