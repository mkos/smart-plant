import time
#board pins
#pin 3=SDA
#pin 5=SCL


from smbus import SMBus

bus = SMBus(1)

last_reading =-1
ain = 0
bus.write_byte(0x48,0)
while(0 == 0):
	reading = bus.read_byte(0x48)
	print('reading: {}'.format(reading))
	time.sleep(1)
