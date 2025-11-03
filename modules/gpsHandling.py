import pandas
import globalValues

def convertGPSdata(readData: pandas.DataFrame, writeData: pandas.DataFrame):
    for i in range(2,8):
        writeData[globalValues.WheelLogColumns[i]] = readData[globalValues.EUCWorldEquivalentColumns[i]]
    writeData["gps_distance"] = writeData["gps_distance"].fillna("0.000")
    writeData["gps_distance"] = (writeData["gps_distance"].astype("float32") * 1000).astype("int")
