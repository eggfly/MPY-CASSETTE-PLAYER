import gc
gc.enable()

from machine import SPI, Pin
import os

mp='/sd'
sdcs = Pin(17, Pin.OUT, value=1)
spi = SPI(0, sck=Pin(18), mosi=Pin(19), miso=Pin(16))

if ((sdcs is not None) and (mp is not None)):
    try:
        import sdcard
        import os
        sd = sdcard.SDCard(spi, sdcs)
        vfs = os.VfsFat(sd)
        os.mount(vfs, mp)
    except:
        print('sd error')

try:
    songs = sorted([('/sd/'+x[0]) for x in os.ilistdir('sd') if x[1] != 0x4000 ])
    print(songs)
except UnicodeError:
    print('SD卡含中文')
except OSError:
    print('SD未插入或损坏')

# for i in os.listdir('sd/music'): print(i)
