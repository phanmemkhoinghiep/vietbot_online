# !/usr/bin/python
# -*- coding: utf-8 -*-
#-*-coding:gb2312-*-
import time
# import imp
import sys
import json
import os
from os import listdir
from os import path
import importlib
import threading
import spidev
import RPi.GPIO as GPIO

with open('config.json') as config_json:
    config_data = json.load(config_json)

led_off_mode=None
led_off_color=None
led_wakeup_mode=None
led_wakeup_color=None
mic_type=''
for p in config_data['mic']:
    if p['is_active']:
        mic_type =p['type']


if mic_type == 'ReSpeaker 2-Mics Pi HAT'or mic_type == 'ReSpeaker 4-Mics Pi HAT':
    class APA102():
        def __init__(self, count=1, gpio_data=14, gpio_clock=15, gpio_cs=None, brightness=1.0, force_gpio=False, invert=False, spi_max_speed_hz=1000000):
            """Initialise an APA102 device.

            Will use SPI if it's available on the specified data/clock pins.

            :param pixel_count: Number of individual RGB LEDs
            :param gpio_data: BCM pin for data
            :param gpio_clock: BCM pin for clock
            :param gpio_cs: BCM pin for chip-select
            :param force_gpio: Specify true to force use of GPIO bitbanging

            """

            self._gpio_clock = gpio_clock
            self._gpio_data = gpio_data
            self._gpio_cs = gpio_cs
            self._invert = invert

            if invert:
                # TODO Add invert support for SPI
                force_gpio = True

            self._gpio = None
            self._spi = None
            self._brightness = brightness

            self._sof_length = 4  # SOF bytes
            self._eof_length = 4  # EOF bytes
            buffer_length = count * 4

            self._buf = []

            for _ in range(self._sof_length):
                self._buf.append(0b00000000)

            self._buf += [0b11100000 | int(self._brightness * 31) for _ in range(buffer_length)]

            for _ in range(self._eof_length):
                self._buf.append(0b11111111)

            if not force_gpio and gpio_data == 10 and gpio_clock == 11 and gpio_cs in (None, 7, 8):
                cs_channel = 0
                if gpio_cs is not None:
                    cs_channel = [8, 7].index(gpio_cs)
                self._spi = spidev.SpiDev(0, cs_channel)
                self._spi.max_speed_hz = spi_max_speed_hz
                if gpio_cs is None:
                    self._spi.no_cs = True
                self._gpio_cs = None

            elif not force_gpio and gpio_data == 20 and gpio_clock == 21 and gpio_cs in (None, 18, 17, 16):
                cs_channel = 0
                if gpio_cs is not None:
                    cs_channel = [18, 17, 16].index(gpio_cs)
                self._spi = spidev.SpiDev(0, cs_channel)
                self._spi.max_speed_hz = spi_max_speed_hz
                if gpio_cs is None:
                    self._spi.no_cs = True
                self._gpio_cs = None

            else:
                self._gpio = GPIO
                self._gpio.setmode(GPIO.BCM)
                self._gpio.setup(gpio_data, GPIO.OUT, initial=1 if self._invert else 0)
                self._gpio.setup(gpio_clock, GPIO.OUT, initial=1 if self._invert else 0)
                if self._gpio_cs is not None:
                    self._gpio.setup(self._gpio_cs, GPIO.OUT)

        def _write_byte(self, byte):
            for _ in range(8):
                self._gpio.output(self._gpio_data, not (byte & 0x80) if self._invert else (byte & 0x80))
                self._gpio.output(self._gpio_clock, 0 if self._invert else 1)
                time.sleep(0)
                byte <<= 1
                self._gpio.output(self._gpio_clock, 1 if self._invert else 0)
                time.sleep(0)

        def set_pixel(self, x, r, g, b):
            """Set a single pixel

            :param x: x index of pixel
            :param r: amount of red (0 to 255)
            :param g: amount of green (0 to 255)
            :param b: amount of blue (0 to 255)

            """
            offset = self._sof_length + (x * 4) + 1
            self._buf[offset:offset + 3] = [b, g, r]

        def set_brightness(self, x, brightness):
            """Set global brightness of a single pixel

            :param x: x index of pixel
            :param brightness: LED brightness (0.0 to 1.0)

            """
            offset = self._sof_length + (x * 4)
            self._buf[offset] = 0b11100000 | int(31 * brightness)

        def show(self):
            """Display the buffer

            Outputs the buffer to connected LEDs using either bitbanged GPIO or SPI.

            """
            if self._gpio_cs is not None:
                self._gpio.output(self._gpio_cs, 0)

            if self._spi is not None:
                self._spi.xfer3(self._buf)

            else:
                for byte in self._buf:
                    self._write_byte(byte)

            if self._gpio_cs is not None:
                self._gpio.output(self._gpio_cs, 1)
    APA102= APA102()
    try:
        import queue as Queue
    except ImportError:
        import Queue as Queue
    class Pixels:
        if mic_type == 'ReSpeaker 2-Mics Pi HAT':
            PIXELS_N = 3
        elif mic_type == 'ReSpeaker 4-Mics Pi HAT':
            PIXELS_N = 4
        def __init__(self):
            self.basis = [0] * 3 * self.PIXELS_N
            self.basis[0] = 2
            self.basis[3] = 1
            self.basis[4] = 1
            self.basis[7] = 2

            self.colors = [0] * 3 * self.PIXELS_N
            self.dev = APA102(num_led=self.PIXELS_N)

            self.next = threading.Event()
            self.queue = Queue.Queue()
            self.thread = threading.Thread(target=self._run)
            self.thread.daemon = True
            self.thread.start()

        def wakeup(self, direction=0):
            def f():
                self._wakeup(direction)

            self.next.set()
            self.queue.put(f)

        def listen(self):
            self.next.set()
            self.queue.put(self._listen)

        def think(self):
            self.next.set()
            self.queue.put(self._think)

        def speak(self):
            self.next.set()
            self.queue.put(self._speak)

        def off(self):
            self.next.set()
            self.queue.put(self._off)

        def _run(self):
            while True:
                func = self.queue.get()
                func()

        def _wakeup(self, direction=0):
            for i in range(1, 25):
                colors = [i * v for v in self.basis]
                self.write(colors)
                time.sleep(0.01)

            self.colors = colors

        def _listen(self):
            for i in range(1, 25):
                colors = [i * v for v in self.basis]
                self.write(colors)
                time.sleep(0.01)

            self.colors = colors

        def _think(self):
            colors = self.colors

            self.next.clear()
            while not self.next.is_set():
                colors = colors[3:] + colors[:3]
                self.write(colors)
                time.sleep(0.2)

            t = 0.1
            for i in range(0, 5):
                colors = colors[3:] + colors[:3]
                self.write([(v * (4 - i) / 4) for v in colors])
                time.sleep(t)
                t /= 2

            # time.sleep(0.5)

            self.colors = colors

        def _speak(self):
            colors = self.colors
            gradient = -1
            position = 24

            self.next.clear()
            while not self.next.is_set():
                position += gradient
                self.write([(v * position / 24) for v in colors])

                if position == 24 or position == 4:
                    gradient = -gradient
                    time.sleep(0.2)
                else:
                    time.sleep(0.01)

            while position > 0:
                position -= 1
                self.write([(v * position / 24) for v in colors])
                time.sleep(0.01)

            # self._off()

        def _off(self):
            self.write([0] * 3 * self.PIXELS_N)

        def write(self, colors):
            for i in range(self.PIXELS_N):
                self.dev.set_pixel(i, int(colors[3*i]), int(colors[3*i + 1]), int(colors[3*i + 2]))

            self.dev.show()
    pixels = Pixels()

elif mic_type=='ReSpeaker 2-Mics Pi HAT with WS281x LED':

    from pixel_ring.apa102 import APA102
    from rpi_ws281x import PixelStrip, Color
    import argparse

    # LED strip configuration:
    LED_COUNT = 16      # Number of LED pixels.
    #LED_PIN = 12         # GPIO pin connected to the pixels (18 uses PWM!).
    LED_PIN = 10        # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
    LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
    LED_DMA = 10          # DMA channel to use for generating signal (try 10)
    LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
    LED_INVERT = False    # True to invert the signal (when using NPN transistor level shift)
    LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
    strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    strip.begin()

    def colorWipe(strip, color, wait_ms=20):
        """Wipe color across display a pixel at a time."""
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, color)
            strip.show()
            time.sleep(wait_ms / 2000.0)


    def theaterChase(strip, color, wait_ms=25, iterations=5):
        """Movie theater light style chaser animation."""
        for j in range(iterations):
            for q in range(3):
                for i in range(0, strip.numPixels(), 3):
                    strip.setPixelColor(i + q, color)
                strip.show()
                time.sleep(wait_ms / 3000.0)
                for i in range(0, strip.numPixels(), 3):
                    strip.setPixelColor(i + q, 0)

    def wheel(pos):
        """Generate rainbow colors across 0-255 positions."""
        if pos < 85:
            return Color(pos * 3, 255 - pos * 3, 0)
        elif pos < 170:
            pos -= 85
            return Color(255 - pos * 3, 0, pos * 3)
        else:
            pos -= 170
            return Color(0, pos * 3, 255 - pos * 3)


    def rainbow(strip, wait_ms=5, iterations=3):
        """Draw rainbow that fades across all pixels at once."""
        for j in range(128 * iterations):
            for i in range(strip.numPixels()):
                strip.setPixelColor(i, wheel((i + j) & 255))
            strip.show()
            time.sleep(wait_ms / 5000.0)


    def rainbowCycle(strip, wait_ms=5, iterations=3):
        """Draw rainbow that uniformly distributes itself across all pixels."""
        for j in range(128 * iterations):
            for i in range(strip.numPixels()):
                strip.setPixelColor(i, wheel(
                    (int(i * 256 / strip.numPixels()) + j) & 255))
            strip.show()
            time.sleep(wait_ms / 7000.0)


    def theaterChaseRainbow(strip, wait_ms=50):
        """Rainbow movie theater light style chaser animation."""
        for j in range(256):
            for q in range(1):
                for i in range(0, strip.numPixels(), 3):
                    strip.setPixelColor(i + q, wheel((i + j) % 255))
                strip.show()
                time.sleep(wait_ms / 1000.0)
                for i in range(0, strip.numPixels(), 3):
                    strip.setPixelColor(i + q, 0)

    try:
        import queue as Queue
    except ImportError:
        import Queue as Queue


    class Pixels:
        PIXELS_N = 3

        def __init__(self):
            self.basis = [0] * 3 * self.PIXELS_N
            self.basis[0] = 2
            self.basis[3] = 1
            self.basis[4] = 1
            self.basis[7] = 2

            self.colors = [0] * 3 * self.PIXELS_N
            self.dev = APA102(num_led=self.PIXELS_N)

            self.next = threading.Event()
            self.queue = Queue.Queue()
            self.thread = threading.Thread(target=self._run)
            self.thread.daemon = True
            self.thread.start()

        def wakeup(self, direction=0):

    #        rainbow(strip)

            def f():
                self._wakeup(direction)
            self.next.set()
            self.queue.put(f)
        def listen(self):
    #        
            
    #        theaterChase(strip, Color(0, 0, 127))
            self.next.set()
            self.queue.put(self._listen)
        def think(self):
            
            self.next.set()
            self.queue.put(self._think)
        def speak(self):
           # theaterChaseRainbow(strip)  
    #        rainbowCycle(strip)
            self.next.set()
            self.queue.put(self._speak)
        def off(self):
            
            self.next.set()
            self.queue.put(self._off)
        def _run(self):
            while True:
                func = self.queue.get()
                func()
        def _wakeup(self,direction=0):
            colorWipe(strip, Color(0, 255, 0))
            colorWipe(strip, Color(0, 0, 255))
            self.write([0] * 3 * self.PIXELS_N)
        def _listen(self):
            rainbow(strip)
            self.write([0] * 3 * self.PIXELS_N)
        def _think(self):
            rainbowCycle(strip)
            self.write([0] * 3 * self.PIXELS_N)
        def _speak(self):      
           theaterChaseRainbow(strip)
        def _off(self):
            colorWipe(strip, Color(0, 0, 0))
            self.write([0] * 3 * self.PIXELS_N)
        def write(self, colors):
            for i in range(self.PIXELS_N):
                self.dev.set_pixel(i, int(colors[3*i]), int(colors[3*i + 1]), int(colors[3*i + 2]))

            self.dev.show()
        def _volume(self, volume): 
            NUMLED=round(volume/8)
            strip1 = PixelStrip(NUMLED, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
            strip1.begin()    
            for i in range(strip1.numPixels()):
                strip1.setPixelColor(i, Color(0, 255, 0))
                strip1.show()
                time.sleep(0.2)
    pixels = Pixels()        
    
elif mic_type == 'ReSpeaker Mic Array v2.0':
    import usb.core
    import usb.util
    import json
    for p in config_data['mic']:
        if p['is_active']:
            led_off_mode=p['led_off_mode']
            led_off_color=p['led_off_color']
            led_wakeup_mode=p['led_wakeup_mode']
            led_wakeup_color=p['led_wakeup_color']            
    class PixelRing:
        TIMEOUT = 8000

        def __init__(self, dev):
            self.dev = dev

        def write(self, cmd, data=[0]):
            self.dev.ctrl_transfer(
                usb.util.CTRL_OUT | usb.util.CTRL_TYPE_VENDOR | usb.util.CTRL_RECIPIENT_DEVICE,
                0, cmd, 0x1C, data, self.TIMEOUT)

        def trace(self):
            self.write(0)

        def mono(self, color):
            self.write(1, [(color >> 16) & 0xFF, (color >> 8) & 0xFF, color & 0xFF, 0])

        def set_color(self, rgb=None, r=0, g=0, b=0):
            if rgb:
                self.mono(rgb)
            else:
                self.write(1, [r, g, b, 0])

        def set_brightness(self, brightness):
            self.write(0x20, [brightness])
        
        def set_color_palette(self, a, b):
            self.write(0x21, [(a >> 16) & 0xFF, (a >> 8) & 0xFF, a & 0xFF, 0, (b >> 16) & 0xFF, (b >> 8) & 0xFF, b & 0xFF, 0])

        def set_vad_led(self, state):
            self.write(0x22, [state])

        def set_volume(self, volume):
            self.write(0x23, [volume])

        def change_pattern(self, pattern=None):
            print('Not support to change pattern')

        def close(self):
            """
            close the interface
            """
            usb.util.dispose_resources(self.dev)

        def off(self,color):
            if color == None:
                self.mono(0)
            else:
                self.write(1, [(color >> 16) & 0xFF, (color >> 8) & 0xFF, color & 0xFF, 0])

        def listen(self,color,direction=None):
            if color == None:
                self.write(2)
            else:
                self.write(1, [(color >> 16) & 0xFF, (color >> 8) & 0xFF, color & 0xFF, 0])
        wakeup = listen

        def think(self):
            self.write(5)

        wait = think

        def spin(self):
            self.write(4)

        speak = spin
        
        def show(self, data):
            self.write(6, data)

        customize = show

    def find(vid=0x2886, pid=0x0018):
        dev = usb.core.find(idVendor=vid, idProduct=pid)
        if not dev:
            return

        # configuration = dev.get_active_configuration()

        # interface_number = None
        # for interface in configuration:
        #     interface_number = interface.bInterfaceNumber

        #     if dev.is_kernel_driver_active(interface_number):
        #         dev.detach_kernel_driver(interface_number)

        return PixelRing(dev)

    find =find()



def led_controll(state,volume):
    if state=='OFF' and volume ==0:
        if mic_type == 'ReSpeaker 2-Mics Pi HAT' or mic_type == 'ReSpeaker 4-Mics Pi HAT': 
            pixels.off()
        elif mic_type == 'ReSpeaker 2-Mics Pi HAT with WS281x LED': 
            pixels._off()
        elif mic_type == 'ReSpeaker Mic Array v2.0':
            if led_off_mode==1:
                find.off(None)
            elif led_off_mode==2:
                find.off(led_off_color)
                # find.mono()
        else:
            pass                
    elif state=='WAKEUP' and volume ==0:
        if mic_type == 'ReSpeaker 2-Mics Pi HAT' or mic_type == 'ReSpeaker 4-Mics Pi HAT': 
            pixels.wakeup()
        elif mic_type == 'ReSpeaker 2-Mics Pi HAT with WS281x LED': 
            pixels.wakeup()
        elif mic_type == 'ReSpeaker Mic Array v2.0':
            if led_wakeup_mode==1:            
                find.wakeup(None)
            elif led_wakeup_mode==2:
                find.wakeup(led_wakeup_color)
                # find.mono(led_wakeup_color)                    
        else:
            pass        
    elif state=='THINK' and volume ==0:
        if mic_type == 'ReSpeaker 2-Mics Pi HAT' or mic_type == 'ReSpeaker 4-Mics Pi HAT': 
            pixels.think()
        elif mic_type == 'ReSpeaker 2-Mics Pi HAT with WS281x LED': 
            pixels.think()        
        elif mic_type == 'ReSpeaker Mic Array v2.0':
            find.think()
        else:
            pass        
    elif state=='SPEAK' and volume ==0:
        if mic_type == 'ReSpeaker 2-Mics Pi HAT' or mic_type == 'ReSpeaker 4-Mics Pi HAT': 
            pixels.speak()
        elif mic_type == 'ReSpeaker 2-Mics Pi HAT with WS281x LED': 
            pixels.speak()                
        elif mic_type == 'ReSpeaker Mic Array v2.0':
            find.speak()
        else:
            pass            
    elif state=='None' and volume!=0:
        if mic_type == 'ReSpeaker 2-Mics Pi HAT':    
            pass
        elif mic_type == 'ReSpeaker 4-Mics Pi HAT':
            pass
        elif mic_type == 'ReSpeaker 2-Mics Pi HAT with WS281x LED':
            pixels._volume(volume)
        elif mic_type == 'ReSpeaker Mic Array v2.0':
            find.set_volume(round(volume/12)-1)
        else:
            pass



# def main():
        
# if __name__ == '__main__':

    # main()
