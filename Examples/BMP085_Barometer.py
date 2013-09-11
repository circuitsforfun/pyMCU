
import pymcu
import time
from numpy import *
 
global OSS
 
# Calibration values
global ac1
global ac2
global ac3
global ac4
global ac5
global ac6
global b1
global b2
global mb
global mc
global md
global b5
temperature = 0
pressure = 0
 
myboard = pymcu.mcuModule() # Initialize mcu find first available module
 
def unsigned(n):
    return n & 0xFFFF
 
def bmp085ReadInt(address):
    data1 = myboard.i2cRead(0xEF,address,2)
    dt = (data1[0] << 8) | data1[1]
    return dt
 
def byte2word(byte1, byte2):
    dt = (byte1 << 8) | byte2
    return dt
 
def bmp085Calibration():
    global ac1
    global ac2
    global ac3
    global ac4
    global ac5
    global ac6
    global b1
    global b2
    global mb
    global mc
    global md
    global b5
    data1 = myboard.i2cRead(0xEF,0xAA,22)
    ac1 = int16(byte2word(data1[0], data1[1]))
    ac2 = int16(byte2word(data1[2], data1[3]))
    ac3 = int16(byte2word(data1[4], data1[5]))
    ac4 = uint16(byte2word(data1[6], data1[7]))
    ac5 = uint16(byte2word(data1[8], data1[9]))
    ac6 = uint16(byte2word(data1[10], data1[11]))
    b1 = int16(byte2word(data1[12], data1[13]))
    b2 = int16(byte2word(data1[14], data1[15]))
    mb = int16(byte2word(data1[16], data1[17]))
    mc = int16(byte2word(data1[18], data1[19]))
    md = int16(byte2word(data1[20], data1[21]))
     
def bmp085Read(address):
    data = myboard.i2cRead(0x77,address,1)
    return data
 
def bmp085ReadUT():
    myboard.i2cWrite(0xEE,0xF4, 0x2E)
    time.sleep(1)
    data = bmp085ReadInt(0xF6)
    ut = data
    return ut
 
def bmp085ReadUP():
    myboard.i2cWrite(0xEE,0xF4, 0x34 )
    time.sleep(.05)
    data1 = myboard.i2cRead(0xEF,0xF6, 3 )
    raw = byte2word(data1[0], data1[1])
    raw *= 256
    raw |= data1[2]
    raw /= 256
    up = raw
    return up
 
def bmp085GetTemperature(ut):
    global ac1
    global ac2
    global ac3
    global ac4
    global ac5
    global ac6
    global b1
    global b2
    global mb
    global mc
    global md
    global b5
 
    x1 = (ut - ac6) * ac5 / 32768
    x2 = (mc * 2048)/(x1 + md)
    b5 = x1 + x2
 
    return (b5 + 8) / 16
 
def bmp085GetPressure(up):
    global OSS
    global ac1
    global ac2
    global ac3
    global ac4
    global ac5
    global ac6
    global b1
    global b2
    global mb
    global mc
    global md
    global b5
    OSS = 0
 
    b6 = b5 - 4000;
    # Calculate B3
    x1 = (b2 * ((b6 * b6) / 4096)) / 2048
    x2 = (ac2 * b6) / 2048
    x3 = x1 + x2
    b3 = ((ac1 * 4 + x3) << OSS + 2) / 4
 
    # Calculate B4
    x1 = (ac3 * b6)/ 8192
    x2 = (b1 * ((b6 * b6) / 4096)) / 65536
    x3 = ((x1 + x2) + 2) / 4
    b4 = uint32(ac4 * (x3 + 32768) / 32768)
    b7 = uint32((up - b3) * 50000L)
 
    if b7 < 0x80000000:
        p = (b7 * 2) / b4
    else:
        p = (b7 * 2) / b3
 
    x1 = (p / 256) * (p / 256)
    x1 = (x1 * 3038) / 65536
    x2 = (-7357 * p) / 65536
    p += (x1 + x2 + 3791) / 16
 
    return p
 
if myboard.active == True:  # If an available module was found and initialized
 
    bmp085Calibration()
 
    while 1:
        temperature = bmp085GetTemperature(bmp085ReadUT())
        pressure = bmp085GetPressure(bmp085ReadUP())
        myboard.lcd(1,'                ')
        mb.pausems(10)
        myboard.lcd(1,'Temp: ' + str(float((temperature / 10.0) * 1.8 + 32)) + ' F' )
        mb.pausems(10)
        myboard.lcd(2,'                ')
        mb.pausems(10)
        myboard.lcd(2,'Pa: ' + str(pressure))
        #print 'Temperature = ' + str(float(temperature / 10.0)) + ' C'
        #print 'Temperature = ' + str(float((temperature / 10.0) * 1.8 + 32)) + ' F'
        #print 'Pressure = ' + str(pressure) + ' Pa\n'
        mb.pausems(1000)
