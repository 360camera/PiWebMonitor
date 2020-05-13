# 360camera's PiWebMonitor on Github
# https://github.com/360camera/PiWebMonitor
from time import sleep, strftime
from gpiozero import CPUTemperature
import psutil
cpu = CPUTemperature()

while True:
    # Read HTML file into list and close
    webpage = open("index.html", "r")
    pageList = webpage.readlines()
    webpage.close()
    # Modify certain lines in list
    pageList[1] = str(cpu.temperature) + "C\n"
    pageList[3] = str(psutil.cpu_percent()) + "%\n"
    pageList[5] = str(psutil.virtual_memory()[2]) + "%\n"
    pageList[7] = strftime("%H:%M:%S") + "\n"
    # Write list over HTML file and close
    webpage = open("index.html", "w")
    webpage.writelines(pageList)
    webpage.close()
    print("Overwrote file at " + strftime("%H:%M:%S") + ".")
    sleep(5)