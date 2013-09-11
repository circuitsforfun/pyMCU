
import pymcu
import time
import pywapi
 
 
mb = pymcu.mcuModule() # Initialize mcu find first available module
mb.lcd()               # Initialize the LCD
 
yahoo_result = pywapi.get_weather_from_yahoo('10001')                  # Use Google as weather source with zip code 10001
mb.lcd(1,yahoo_result['condition']['text'])               # Display current conditions on first line of LCD
mb.pausems(100)                                                          # Small delay between next LCD command
mb.lcd(2,'Temp ' + str(int(yahoo_result['condition']['temp']) * 9.0 / 5.0 + 32) + ' F') # Display Temperature on second line of LCD
