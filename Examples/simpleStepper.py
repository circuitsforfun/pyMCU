# For more info visit: http://www.circuitsforfun.com/smf/index.php?topic=44.0

import pymcu

mb = pymcu.mcuModule()

stepType = 48  # Mitsumi 48 steps = 360 degrees
steps = [[3,4],[2,3],[1,2],[4,1]] # Step Sequence Pins
stepIndex = 0

def stepFWD(stepIndex):
    mb.pinLow([1,2,3,4])
    mb.pinHigh(steps[stepIndex])

def stepREV(stepIndex):
    mb.pinLow([1,2,3,4])
    mb.pinHigh(steps[stepIndex])

for x in range(stepType):
    stepFWD(stepIndex)
    stepIndex += 1
    if stepIndex > 3:
        stepIndex = 0
    mb.pausems(200)

for x in range(stepType):
    stepREV(stepIndex)
    stepIndex -= 1
    if stepIndex < 0:
        stepIndex = 3
    mb.pausems(200)
