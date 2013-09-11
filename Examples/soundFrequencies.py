import pymcu    # Import pyMCU module
 
mb = pymcu.mcuModule()  # Create a new pyMCU class object from first found pyMCU board
 
# Play DoReMiFaSolLaTiDo
print 'Do...'
mb.freqOut(1,500,1047)  # Output 1047 Hz for 500 milliseconds
print 'Re...'
mb.freqOut(1,500,1175)  # Output 1175 Hz for 500 milliseconds
print 'Mi...'
mb.freqOut(1,500,1319)  # Output 1319 Hz for 500 milliseconds
print 'Fa...'
mb.freqOut(1,500,1396)  # Output 1396 Hz for 500 milliseconds
print 'Sol...'
mb.freqOut(1,500,1568)  # Output 1568 Hz for 500 milliseconds
print 'La...'
mb.freqOut(1,500,1760)  # Output 1760 Hz for 500 milliseconds
print 'Ti...'
mb.freqOut(1,500,1976)  # Output 1976 Hz for 500 milliseconds
print 'Do...'
mb.freqOut(1,500,2093)  # Output 2093 Hz for 500 milliseconds
