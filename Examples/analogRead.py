
import pymcu           # Import the pymcu module
 
mb = pymcu.mcuModule() # Initialize mb (My Board) with mcuModule Class Object - Find first available pymcu hardware module.
while True:            # Create an endless loop
    adcVal = mb.analogRead(1) #read ADC on pin A1
    adcFrac = adcVal/1024.0 #fractional from 0-5V
    adcVolts = adcFrac*5.0 #voltage assuming VCC=5V
    print "current reading: %d%% (%.02fV)"%(adcFrac*100,adcVolts)
    mb.pausems(100)    # pause for 100 milliseconds
