import time

config = {
	# sysfs file
	'temp_file': '/sys/class/thermal/thermal_zone0/temp',
	# polling loop wait
	'period': 1.0,
	# thre
	'threshold': 40.0,
}

def get_temp(temp_f):
	temp_f.seek(0)
	return int(temp_f.read()) / 1000.0

def loop(temp_f):
	temp = get_temp(temp_f)
	print(temp)
	if temp >= config['threshold']:
		pass
	else:
		pass

def main():
	with open(config['temp_file'], 'r') as f:
		while True:
			loop(f)
			time.sleep(config['period'])

main()
