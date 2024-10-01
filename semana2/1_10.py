def convertTempCF(celsius):
    farenheint = ((9/5)*celsius) + 32
    return farenheint

tempCelsius = 24
tempFarenheint = convertTempCF(tempCelsius)
print(tempFarenheint)