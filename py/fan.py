import time
import subprocess
import re

config = {
	# polling loop wait
	'period': 1.0,
	# thre
	'threshold': 40.0,
}

# [0-9]+ "." [0-9]+
temp_re = re.compile(r'\d+\.\d+')

def get_temp():
	temp_str = subprocess.run(['vcgencmd', 'measure_temp'],
		check=True, capture_output=True).stdout.decode()
	m = temp_re.search(temp_str)
	temp = float(m.group())
	return temp

def main_loop():
	temp = get_temp()
	print(temp)
	if temp >= config['threshold']:
		pass
	else:
		pass

def main():
	while True:
		main_loop()
		time.sleep(config['period'])

main()
