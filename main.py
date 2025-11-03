import pandas
import globalValues
from modules.gpsHandling import convertGPSdata
from modules.dateTimeHandling import convertDateTime
from modules.wheelParameterHandling import convertWheelData

inputDir = input("Input directory of EUCWorld csv file:")
outputDir = input("Output directory of WheelLog equivalent csv file (if provided just filename, output will be in the same folder as main.py):")

readData = pandas.read_csv(inputDir, dtype="str")

writeData = pandas.DataFrame()

convertDateTime(readData, writeData)
convertGPSdata(readData, writeData)
convertWheelData(readData, writeData)

writeData = writeData.fillna("0")

writeData.to_csv(outputDir)

print("Done!")