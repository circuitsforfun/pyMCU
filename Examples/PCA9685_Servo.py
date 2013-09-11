# For more info visit: http://www.circuitsforfun.com/smf/index.php?topic=42.0

import pymcu
import time


i2cAddr = 0x80  # change this for the address you set the board to with the jumpers

def setPWM(channel, on, off):
    mb.i2cWrite(i2cAddr, 6 + (4 * channel), on & 0xFF)
    mb.i2cWrite(i2cAddr, 7 + (4 * channel), on >> 8)
    mb.i2cWrite(i2cAddr, 8 + (4 * channel), off & 0xFF)
    mb.i2cWrite(i2cAddr, 9 + (4 * channel), off >> 8)

mb = pymcu.mcuModule()

# init PWM Board
mb.i2cWrite(i2cAddr, 0x00 , 0x00)   # clear Mode1
mb.pausems(1)
mb.i2cWrite(i2cAddr, 0x00, 0x31) # go to sleep
mb.pausems(1)
mb.i2cWrite(i2cAddr, 0xFE, 100) # Set frequency to 60Hz
mb.pausems(1)
mb.i2cWrite(i2cAddr, 0x00, 0xA1) # Mode1 Set to our preferred mode[ Reset, INT_CLK, Auto-Increment, Normal Mode]
mb.pausems(1)
mb.i2cWrite(i2cAddr, 0x01, 0x04) # Mode2 Set to our preferred mode[Output logic state not inverted, Outputs change on STOP]
mb.pausems(1)

servoNum = 0  # change this to control servo number 0 thru 15

while 1:
    setPWM(servoNum, 0, 150)  # Servo Min
    time.sleep(1)
    setPWM(servoNum, 0, 600)  # Servo Max
    time.sleep(1)
