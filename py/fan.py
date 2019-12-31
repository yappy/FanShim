import subprocess

stdout = subprocess.run(['vcgencmd', 'measure_temp'],
	check=True, capture_output=True).stdout
print(stdout.decode())
