#!/bin/sh
sleep 10
screen -A -m -d -S remoteled sudo python /home/pi/Projects/remote-led/script.py
