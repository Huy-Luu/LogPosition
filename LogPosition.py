from SerialDataHandler import SerialDataHandler
from UTMmodule import UTMmodule
import time
import time

serialHandler = SerialDataHandler('/dev/ttyClientB', 115200)
f = open(r"/home/hluu/LogPosition/data.txt", "a")

while True:
    serialHandler.send("m")
    lat_nmea, lon_nmea = serialHandler.receiveTwoInputs()
    lat = UTMmodule.nmeaToDec(lat_nmea)
    lon = UTMmodule.nmeaToDec(lon_nmea)
    print(str(lat) + " " + str(lon))
    f.write(str(lat) + "," + str(lon) + "\r")
    time.sleep(1)
    #print(serialHandler.receiveOneInput())
