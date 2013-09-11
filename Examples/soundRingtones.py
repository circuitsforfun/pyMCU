import pymcu
import time
 
mb = pymcu.mcuModule()  # Create a new pyMCU class object from first found pyMCU board
 
# RTTL variable to hold RTTL song
RTTL = 'Bond:d=4,o=5,b=50:32p,16c#6,32d#6,32d#6,16d#6,8d#6,16c#6,16c#6,16c#6,16c#6,32e6,32e6,16e6,8e6,16d#6,16d#6,16d#6,16c#6,32d#6,32d#6,16d#6,8d#6,16c#6,16c#6,16c#6,16c#6,32e6,32e6,16e6,8e6,16d#6,16d6,16c#6,16c#7,c.7,16g#6,16f#6,g#.6'
 
# A Dictionary that contains the frequencies for each note
noteFreq = {'p':0,'a':3520,'a#':3729,'b':3951,'c':4186,'c#':4435,'d':4699,'d#':4978,'e':5274,'f':5588,'f#':5920,'g':6272,'g#':6645}
 
# This function will return the default Duration, Octave, and BeatsPerMinute from the RTTL data
def dob(dobData):
    dobVals = dobData.split(',')
    defaultDur = int(dobVals[0].split('=')[1])
    defaultOct = int(dobVals[1].split('=')[1])
    defaultBeats = int(dobVals[2].split('=')[1])
    return defaultDur, defaultOct, defaultBeats
 
# This function will return the duration per note from the RTTL note data
def durSplit(noteData):
    for d in noteData:
        if ord(d) >= 97 and ord(d) <= 122:
            durSplit = noteData.split(d)
            if len(durSplit[0]) > 0:
                return int(durSplit[0])
    return 0
 
# This function will return just the note for dictionary look up from the RTTL note data
def noteSplit(noteData):
    note = ''
    hasDot = False
    for d in noteData:
        if ord(d) >= 97 and ord(d) <= 122:
            note += d
        if ord(d) == 35:
            note += d
        if ord(d) == 46:
            hasDot = True
 
    return note, hasDot
 
# This function will return per note octave changes if specified in the RTTL note data
def noteOctave(noteData):
    if noteData[len(noteData)-1] >= 53 and noteData[len(noteData)-1] <= 56:
        return 8 - int(noteData[len(noteData)-1])
    else:
        return None
 
 
rttlParts = RTTL.split(':')  # Split the RTTL song data into it's 3 core parts
print 'Song: ', rttlParts[0] # Song Name
defaultDur, defaultOct, defaultBeats = dob(rttlParts[1]) # Get default Duration, Octave, and Beats Per Minute
print 'Note Duration: ', defaultDur
print 'Octave: ', defaultOct
print 'Beats Per Min: ', defaultBeats
 
rttlNotes = rttlParts[2].split(',')  # Split all the note data into a list
 
for note in rttlNotes: # Iterate through the note list
    note = note.strip() # Strip out any possible pre or post spaces in the note data
    durVal = durSplit(note) # Determine the per note duration if not default
    if durVal == 0: # If there is no per note duration then use default for that note
        durVal = defaultDur
    duration = 60000 / defaultBeats / durVal * 3 # Calculate the proper duration based on Beats Per Minute and Duration Value
    noteStr, hasDot = noteSplit(note) # Get note for dictionary lookup and check if the note has a dot
    nFreq = noteFreq[noteStr] # Look up note frequency from the dictionary
    if hasDot == True: # if it has a dot calculate the new duration
        duration *= 3 / 2
    octave = noteOctave(note) # Determine if there is per note octave change
    if octave != None: # if so calculate the new octave frequency
        nFreq /= octave
    else:              # else use the default octave frequency
        nFreq /= defaultOct
    if nFreq == 0:     # if nFreq is 0 then it's a pause note so pause for the required time
        time.sleep(float(duration / 1000.0))
    else:              # else play the note from the song
        mb.freqOut(1,duration,nFreq)

