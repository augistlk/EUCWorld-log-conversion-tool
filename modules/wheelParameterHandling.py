import pandas
import globalValues

def convertWheelData(readData: pandas.DataFrame, writeData: pandas.DataFrame):
    for i in range(8, 22):
        if i != 13: 
            writeData[globalValues.WheelLogColumns[i]] = readData[globalValues.EUCWorldEquivalentColumns[i]]
        else:
            writeData[globalValues.WheelLogColumns[i]] = "0"
    writeData["pwm"] = 100 - writeData["pwm"].astype("int")
    writeData["distance"]= (writeData["distance"].astype("float32") * 1000).astype("int")
    writeData["totaldistance"]= (writeData["totaldistance"].astype("float32") * 1000).astype("int")