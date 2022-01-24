# raspberry-PiLight
# Android Bluetooth client git repo:
https://github.com/akimaleo/Android-PiLight

Connect to raspberry via SSH:

## "Fetch and run" script
Basically file has to be created iin root directory to be able easily fetch changes from repo

```#!/bin/bash
cd Desktop
git clone https://github.com/akimaleo/raspberry-PiLight.git
cd raspberry-PiLight
git pull origin master
sudo PYTHONPATH=".:build/lib..linux-armv7l-2.7" python code/__init__.py &
