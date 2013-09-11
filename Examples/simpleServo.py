import pymcu    # Import pyMCU module
 
mb = pymcu.mcuModule()  # Create a new pyMCU class object from first found pyMCU board
 
# This will move a typical servo to one extent of it's range
# (or on a continuous servo will cause it to spin at full speed in one direction)
mb.pulseOut(1,500,50)  # Generate a 500 ms pulse on Digital Pin 1, repeat 50 times
 
# This will move a typical servo the other extent of it's range
# (or on a continuous servo will cause it to spin at full speed in the other direction)
mb.pulseOut(1,2000,50) # generate a 2000 ms pulse on Digital Pin 1, repeat 50 times
 
# This will move the servo to one extent then step by 20 ms pulse length back to the other end of the range
# (or on a continuous servo will spin at full speed in one direction, slow down, come to a stop,
# then speed back up and spin at full speed in the other direction)
for x in range(500,2000,20):
    mb.pulseOut(1,x,5)
    mb.pausems(10)

