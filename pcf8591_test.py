import time
#board pins
#pin 3=SDA
#pin 5=SCL


from smbus import SMBus

bus = SMBus(1)

last_reading =-1
ain = 0

LIGHT = 0
MOISTURE = 1
AUTOINCREMENT = 4

bus.write_byte(0x48,AUTOINCREMENT)
while(0 == 0):
	light = bus.read_word_data(0x48, MOISTURE)
	moisture = bus.read_word_data(0x48, LIGHT)
	print('light: {}, moisture: {}'.format(light & 0xff , moisture & 0xff))
	time.sleep(1)
