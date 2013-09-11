
import pymcu    # Import pyMCU module
 
# Create a list of lists to use as a way of turning on or off different segments to make the desired numbers
ledNums = [[1,2,3,4,5,6],[2,3],[1,2,4,5,7],[1,2,3,4,7],[2,3,6,7],[1,3,4,6,7],[1,3,4,5,6,7],[1,2,3],[1,2,3,4,5,6,7],[1,2,3,6,7]]
 
mb = pymcu.mcuModule()  # Create a new pyMCU class object from first found pyMCU board
mb.pinHigh(ledNums[8])  # Turn all segments off
 
x = 0  # Initialize our counting variable
while 1: # Create an endless loop
    mb.pinHigh(ledNums[8]) # Turn all segments off
    mb.pinLow(ledNums[x])  # Turn on the segments needed to make the number
    mb.pausems(500)        # Sleep for half a second
    x += 1                 # Increment our counter
    if x > 9:              # If counter is greater than 9 reset back to 0
        x = 0
