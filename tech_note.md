# Reference Software
https://github.com/pimoroni/fanshim-python

# CPU 温度の取得
## vcgencmd
```
$ vcgencmd measure_temp
```
https://www.raspberrypi.org/documentation/raspbian/applications/vcgencmd.md

VideoCore General Command の略っぽい？
多分 VideoCore (GPU) に mailbox でコマンドを出して
返答を待っているか何かだと思われる。
SoC についている温度センサから値を取得するとのこと。
一応 Broadcom 的には GPU (3D graphics や動画圧縮伸長) に制御用 CPU がついている
製品のつもりなのかもしれない…。(CPU は ARM をそのまま載せてるだけだし)

温度をポーリングするたびにプロセスを起動するのは効率が悪すぎる。
やるなら vcgencmd のソースを参考に真似するのがよさそう。
短いし、"measure_temp" のような文字列が見えないし、argv をコピーしてそのまま
GPU に丸投げしているだけっぽい。
/opt/vc/ に C header/lib があるのでそいつらを使えばできるかも？

https://github.com/raspberrypi/userland/tree/master/host_applications/linux/apps/gencmd

## sysfs
```
/sys/class/thermal/thermal_zone0/temp
とりあえず中身を見るなら
$ cat /sys/class/thermal/thermal_zone0/temp
```
単位はミリ摂氏。(1/1000 すれば OK)
中身は見ていないが結局 vcgencmd と同じところにつながっているんじゃないかな。

ファイルシステム syscall が使える疑似ファイルシステムなので、各種言語の
各種ファイル操作 API が使える。
(変なバッファリングが入るとよくないのでなるべく生の syscall に近い方が望ましいが)
open しっぱなしにして offset = 0 に seek するとか pread で毎回絶対 offset 0 から
読むとかすれば許容可能な負荷で温度をポーリング可能と思われる。
(こちらを採用)
