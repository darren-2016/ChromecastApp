from __future__ import print_function
import pychromecast

print ("Chromecast Application")

chromecasts = pychromecast.get_chromecasts()
print (chromecasts)
for cc in chromecasts:
    print (cc.device.friendly_name)

