import time
from fanshim import FanShim

config = {
	# sysfs file
	'temp_file': '/sys/class/thermal/thermal_zone0/temp',
	# polling loop wait
	'period': 1.0,

	# (threshold, OFF->ON, ON->OFF, R, G, B)
	'status': [
		(40.0,  True, False, 255,   0,   0),
		(30.0, False, False, 255, 255,   0),
		(None, False,  True,   0, 255,   0),
	],
}

fanshim = FanShim()

def get_temp(temp_f):
	temp_f.seek(0)
	return int(temp_f.read()) / 1000.0

def change_state(fan, r, g, b):
	print(f'Change fan/led state ({fan}, {r}, {g}, {b})')
	fanshim.set_fan(fan)
	fanshim.set_light(r, g, b)

def find_state(temp):
	for t, b1, b2, r, g, b in config['status']:
		if t == None or temp >= t:
			return t, b1, b2, r, g, b
	raise RuntimeError('Invalid status')

# state = (fan:bool, r, g, b:int)
def loop(*, temp_f, prev_state):
	temp = get_temp(temp_f)
	print(temp)

	_, on, off, r, g, b = find_state(temp)
	fan = prev_state[0]
	if (not fan) and on:
		fan = True
	elif fan and off:
		fan = False

	# Create next state (fan, f, g, b)
	next_state = (fan, r, g, b)
	# Touch H/W if at least one has been changed
	if prev_state != next_state:
		change_state(*next_state)

	return next_state

def main():
	with open(config['temp_file'], 'r') as f:
		# Initial state = (fan:off, rgb: last)
		_, _, _, r, g, b = config['status'][-1]
		state = (False, r, g, b)
		change_state(*state)
		while True:
			state = loop(temp_f=f, prev_state=state)
			time.sleep(config['period'])

try:
	main()
finally:
	fanshim.set_fan(False)
