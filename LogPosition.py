from SerialDataHandler import SerialDataHandler
from UTMmodule import UTMmodule
import time

serialHandler = SerialDataHandler('COM1', 115200)
f = open(r"E:/New folder/BK/HK221/Luan_van_tot_nghiep/Temporary/LogPosition/data.txt", 'r')

while True:
    serialHandler.send("m")
    lat_nmea, lon_nmea = serialHandler.receiveTwoInputs()
    lat = UTMmodule.nmeaToDec(lat_nmea)
    lon = UTMmodule.nmeaToDec(lon_nmea)
    print(str(lat) + " " + str(lon))
    #print(serialHandler.receiveOneInput())