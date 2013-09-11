import pymcu    # Import pyMCU module
 
mb = pymcu.mcuModule()  # Create a new pyMCU class object from first found pyMCU board
 
# Play DTMF Tones for phone number (123)-456-7890
myboard.dtmfOut(1, 1)
myboard.dtmfOut(1, 2)
myboard.dtmfOut(1, 3)
myboard.dtmfOut(1, 4)
myboard.dtmfOut(1, 5)
myboard.dtmfOut(1, 6)
myboard.dtmfOut(1, 7)
myboard.dtmfOut(1, 8)
myboard.dtmfOut(1, 9)
myboard.dtmfOut(1, 0)
