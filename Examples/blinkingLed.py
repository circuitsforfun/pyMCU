import pymcu           # Import the pymcu module
 
mb = pymcu.mcuModule() # Initialize mb (My Board) with mcuModule Class Object - Find first available pymcu hardware module.
 
for x in range(1,25):  # Create a for next loop with 25 iterations
    mb.pinHigh(1)      # Set D1 pin High  (LED On)
    mb.pausems(500)    # Sleep for half a second
    mb.pinLow(1)       # Set D1 pin Low   (LED Off)
    mb.pausems(500)    # Sleep for half a second
