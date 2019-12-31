# FanShim
Driver & Application for Fan SHIM.

Fan SHIM: Cool fan for Raspberry Pi 4.

https://www.switch-science.com/catalog/5990/

## Setup
```
$ pip3 install -r requirements.txt
```

## Test exec
```
$ python3 fan.py
```

## Exec automatically on reboot
See `cron.txt`

### Search and kill it
```
$ ps aux | grep python
$ kill <pid>
```

## Print temperature for quick verification
```
$ ./gettemp.sh
```
