import time
#board pins
#pin 3=SDA
#pin 5=SCL


from smbus import SMBus
from collections import OrderedDict

LIGHT = 0
MOISTURE = 1
DEVICE_ID = 0x48

bus = SMBus(1)

class PCF8591(object):

    autoincrement = 0x04

    def __init__(self, bus_handle, device_id):
        self.bus = bus_handle
        self.id = device_id

    def start(self):
        self.bus.write_byte(self.id, self.autoincrement)

    def read(self):
        result = []
        for i in range(4):
	    result.append(self.bus.read_word_data(self.id,i+1) & 0xff)

        return result


adc = PCF8591(bus, DEVICE_ID)
adc.start()

while(True):
        readings = OrderedDict(zip(['light', 'moisture', 'unused_3', 'unused_4'], adc.read()))
        print ', '.join(['{}: {}'.format(k,v) for k, v in readings.items() if not k.startswith('unused')])
	time.sleep(1)
