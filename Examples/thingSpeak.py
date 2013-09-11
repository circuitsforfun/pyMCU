
import pymcu
import time
import httplib, urllib
 
mb = pymcu.mcuModule()
 
while 1:
    mb.lcd()
    ctemp = mb.i2cRead(145,0,2) # Read Temperature data address ( 1 0 0 1 A2 A1 A0 R ) = 10010001 (145 Decimal value) My A2, A1, A0 are all connected to ground
    bh = ctemp[0] << 3  # Shift left 3 bytes to make room for the other 3 bytes of the 11 byte temperature data.
    bl = ctemp[1] >> 5  # Get rid of the first 5 bytes by shifting right as they are ignored according to the datasheet
    ttemp = bh | bl     # Or the 2 bytes together to make the complete 11 byte temperature data.
    # Need to check first if the temperature data is going to be a negative or positive number
    if ctemp[0] >> 7 == 1: # Negative Temp (Need to do 2's Complement conversion)
        tempInC = ((ttemp ^ 2047) + 1) * -0.125
        tempInF = tempInC * 1.8 + 32.0
    else: # Positive Temp
        tempInC = ttemp * 0.125
        tempInF = tempInC * 1.8 + 32.0
    params = urllib.urlencode({'key': 'API_KEY_NOT_SHOWN','field1': tempInF})
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    conn = httplib.HTTPConnection("api.thingspeak.com")
    conn.request("POST", "/update", params, headers)
    response = conn.getresponse()
    print response.status, response.reason
    data = response.read()
    conn.close()
    mb.lcd(1,str(tempInC) + " C")
    mb.lcd(2,str(tempInF) + " F")
    time.sleep(300)
