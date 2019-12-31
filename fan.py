import time
from fanshim import FanShim

config = {
	# sysfs file
	'temp_file': '/sys/class/thermal/thermal_zone0/temp',
	# polling loop wait
	'period': 1.0,
	# threshold temp
	'threshold': 40.0,
	# LED
	'color_on': [0, 255, 0],
	'color_off': [255, 0, 0],
}

fanshim = FanShim()

def get_temp(temp_f):
	temp_f.seek(0)
	return int(temp_f.read()) / 1000.0

def change_state(fan):
	print('Change fan state', fan)
	fanshim.set_fan(fan)
	if fan:
		fanshim.set_light(*config['color_on'])
	else:
		fanshim.set_light(*config['color_off'])

def loop(*, temp_f, prev_state):
	temp = get_temp(temp_f)
	print(temp)
	next_state = temp >= config['threshold']
	if prev_state != next_state:
		change_state(next_state)
	return next_state

def main():
	with open(config['temp_file'], 'r') as f:
		state = None
		while True:
			state = loop(temp_f=f, prev_state=state)
			time.sleep(config['period'])

main()
