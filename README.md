# raspberry-PiLight

Connect to raspberry via SSH:

##"Fetch and run" script
Basically file has to be created iin root directory to be able easily fetch changes from repo

```#!/bin/bash
cd /
git clone https://github.com/akimaleo/raspberry-PiLight.git
git pull origin master
sudo PYTHONPATH=".:build/lib..linux-armv7l-2.7" python raspberry-PiLight/code/__init__.py &```