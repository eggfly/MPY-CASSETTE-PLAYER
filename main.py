from lib import tft_config
import st7789
import framebuf
import time

tft=tft_config.config(1)
tft.init()
tft.fill(0)
tft.jpg('img/logo1.jpg',65,10, st7789.SLOW)


fb = tft.jpg_decode('img/'+'1'+'.jpg')
fbuf = framebuf.FrameBuffer((fb[0]), 60, 60, framebuf.RGB565)
fbuf2 = framebuf.FrameBuffer(bytearray(60*60*2), 60, 60, framebuf.RGB565)

for i in range(180):
    t = time.ticks_us()
    fbuf2.rotate(fbuf, i*24)
    t2 = time.ticks_us()
    print(t2 - t, "us")
    tft.blit_buffer(fbuf, 0, 75, 60, 60)
    tft.blit_buffer(fbuf2, 180, 74, 60, 60)
    if i == 0:
        time.sleep_ms(5000)
    time.sleep_ms(500)
