
import usb.core
import usb.util
import json


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


if __name__ == '__main__':
    import time

    pixel_ring = find()

    while True:
        try:
            pixel_ring.off(0xFFFF99) #Vàng
            time.sleep(3)
            # pixel_ring.off(0xFA8072) #Đỏ
            # time.sleep(3)
            # pixel_ring.off(0x00FF82) #Xanh
            # time.sleep(3)
            # pixel_ring.off(0x4464BB) #Xanh Coban 
            # time.sleep(3)
            # pixel_ring.off(0x3CFF00) #Xanh Lá 
            # time.sleep(3)
            # pixel_ring.think()
            # time.sleep(3)            
            # pixel_ring.spin()
            # time.sleep(3)            

        except KeyboardInterrupt:
            break

    pixel_ring.off(None)