import subprocess
import re

# [0-9]+ "." [0-9]+
temp_re = re.compile(r'\d+\.\d+')

temp_str = subprocess.run(['vcgencmd', 'measure_temp'],
	check=True, capture_output=True).stdout.decode()
m = temp_re.search(temp_str)
temp = float(m.group())
print(temp)
