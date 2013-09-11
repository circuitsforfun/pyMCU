# For more info visit: http://www.circuitsforfun.com/smf/index.php?topic=23.0

import pymcu

mb = pymcu.mcuModule() # Initialize mcu find first available module

def startTemp(): # Start Temp Read in DS18B20 Chip
    mb.owWrite(1,1,[0xCC, 0x44]) # Skip ROM search & do temp conversion

def convertTemp(readTemp):
    cTemp = None
    if (readTemp >> 10) == 1: # If bit 11 is 1 then Temperature is negative
        cTemp = ((readTemp ^ 65535) + 1) * -0.0625
    else: # else it's positive
        cTemp = readTemp * 0.0625
    return cTemp

def checkBusy():
    check = mb.owRead(1,4,1) # Read busy-bit
    return check

def readTemp():
    mb.owWrite(1,1,[0xCC, 0xBE]) # Skip ROM search & read scratchpad memory
    getTemp = mb.owRead(1,2,2) # Read Low and High bytes of DS18B20 temperature data
    rTemp = (getTemp[1] << 8 ) | getTemp[0] # Bitwise OR the low and high bytes into a single 12 bit value
    return rTemp

startTemp()
while 1:
    check = checkBusy() # Check if DS18B20 is busy
    if check != 0: # if busy don't try and read temp and wait for next time in loop
        temp = readTemp() # Read Temperature
        cTemp = convertTemp(temp) # Do Temperature Conversion
        print 'Temp: ' + str(cTemp) + 'C' # Print in Celcius
        print 'Temp: ' + str(cTemp * 1.8 + 32.0) + 'F' # Print in Fahrenheit
        startTemp() # Start next temperature read

    mb.pausems(500) # Wait half a second
