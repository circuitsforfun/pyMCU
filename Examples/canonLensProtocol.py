import pymcu
 
fstops = {0:'0',0x8:'1',0xB:'1.1',0xC:'1.2',0xD:'1.2',0x10:'1.4',0x13:'1.6', \
          0x14:'1.8',0x15:'1.8',0x18:'2',0x1B:'2.2',0x1C:'2.5',0x1D:'2.5',0x20:'2.8', \
          23:'3.2',0x24:'3.2',0x25:'3.5',0x28:'4',0x2B:'4.5',0x2C:'4.5',0x2D:'5', \
          0x30:'5.6',0x33:'6.3',0x34:'6.7',0x35:'7.1',0x38:'8',0x3B:'9',0x3C:'9.5', \
          0x3D:'10',0x40:'11',0x43:'13',0x44:'13',0x45:'14',0x48:'16',0x4B:'18', \
          0x4C:'19',0x4D:'20',0x4E:'20',0x4F:'20',0x50:'22',0x53:'25',0x54:'27', \
          0x55:'29',0x58:'32',0x5A:'32',0x5B:'36',0x5C:'38',0x5D:'40',0x60:'45', \
          0x63:'51',0x64:'54',0x65:'57',0x68:'64',0x6B:'72',0x6C:'76',0x6D:'80',0x70:'91'}
 
mb = pymcu.mcuModule()
mb.lcd()
 
print "Enable SPI"
mb.spiEnable(1,100,0,0)
 
# Init Lens
lcheck = 0
while lcheck != 170:
    il = mb.spiTransfer([0,0xA,0,0xA,0], 400)
    lcheck = il[4]
 
focalMin = 0
focalMax = 0
print "Init Lens"
mb.lcd(1,'Init Lens       ')
il = mb.spiTransfer([0,0xA,0,0xA,0,0,0,0x80,0xA,0x98,1,0,0,0,0,0,0xB0,0,0,0,0xB0,0,0,0], 400)
focalMin = (il[10] << 8) | il[11]
focalMax = (il[12] << 8) | il[13]
print "Focal", str(focalMin) + '-' +  str(focalMax)
print "F-Stop", str(fstops[int(il[21])]) + '-' + str(fstops[int(il[23])])
mb.lcd(1,'Focal ' + str(focalMin) + '-' + str(focalMax))
mb.lcd(2,'FStop ' + str(fstops[int(il[21])]) + '-' + fstops[int(il[23])])
mb.pausems(2000) # Wait and give some time to read the LCD
mb.lcd()
# Clear F-Stop (Full Open)
print "Clear F-Stop"
mb.lcd(1,'Clear F-Stop    ')
mb.spiTransfer([0x90,0,0,0,0xC,0x13,0x80,0x90,0,0,0xF,0xA,0],300)
 
mb.pausems(500)
 
# F-Stop Full Close
print "F-Stop Full Close"
mb.lcd(1,'F-Stop Close    ')
mb.spiTransfer([0x13,0x58,0])
 
mb.pausems(500)
 
# Clear F-Stop (Full Open)
print "Clear F-Stop"
mb.lcd(1,'Clear F-Stop    ')
mb.spiTransfer([0x90,0,0,0,0xC,0x13,0x80,0x90,0,0,0xF,0xA,0],300)
 
mb.pausems(500)
 
# Focus Test Far
focusAmt = 100
print "Focus Test Far"
mb.lcd(1,'Focus Test Far  ')
for x in range(20):
    mb.spiTransfer([0xA])
    mb.pausems(20)
    mb.spiTransfer([0x50,0x2F,0xE0,0,0,0xEA,0,0,0,0,0,0,0x44,0,focusAmt],300)
    mb.pausems(20)
    mb.spiTransfer([0x90,0])
    mb.pausems(20)
    mb.spiTransfer([0xE,0])
    mb.pausems(100)
 
 
# Focus Test Near
focusAmt = 155
print "Focus Test Near"
mb.lcd(1,'Focus Test Near ')
for x in range(20):
    mb.spiTransfer([0xA])
    mb.pausems(20)
    mb.spiTransfer([0x50,0x2F,0xE0,0,0,0xE8,0,0,0,0,0,0,0x44,0xFF,focusAmt],300)
    mb.pausems(20)
    mb.spiTransfer([0x90,0])
    mb.pausems(20)
    mb.spiTransfer([0xE,0])
    mb.pausems(100)
 
mb.lcd(1,'Test Complete   ')
