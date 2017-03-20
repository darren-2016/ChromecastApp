############################################################
# Chromecast Application
# Control of Chromecast device from MacBook.
#

# Imports
from __future__ import print_function
import pychromecast

############################################################
# Function:    mediacast
# Description: 
# Parameters:  mcast
# Returns:     None
def mediacast(mcast):
    
    mcast.play_media('http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4', 'video/mp4')

    mcast.block_until_active()

    print (mcast.status)

    mcast.pause()

    mcast.play()

############################################################
# Function:    mediacaststop
# Description: 
# Parameters:  mcast
# Returns:     None
def mediacaststop(mcast):
    mcast.stop()


############################################################

print
print ("**************************")
print ("* Chromecast Application *")
print ("**************************")
print

chromecasts = pychromecast.get_chromecasts()
#print (chromecasts)

print ("Chromecast devices detected:")
for cc in chromecasts:
    print (cc.device.friendly_name)

cc.wait()
print (cc.device)

print (cc.status)

mc = cc.media_controller

mediacast(mc)

#mediacaststop(mc)



