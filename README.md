# PiWebMonitor
A basic auto-updating Raspberry Pi resource monitor webpage which displays CPU temperature, CPU usage and RAM usage.
##### **WARNING:** This code constantly writes to disk and may decrease the lifespan of your storage device.
### Requirements
This code is written in Python 3 and requires the modules `gpiozero` and `psutil`, both of which can be installed using `pip`.
### Running the webpage
In order to run the webpage, first open `webpageUpdater.py` and leave it running, then open a new terminal and simultaneously run the command `python3 -m http.server 80`. Once this is running, you can visit the webpage by entering your Pi's local IP into a web browser.
###### The HTML code doesn't look great, but I wanted to compact it so I could easily write over lines.
