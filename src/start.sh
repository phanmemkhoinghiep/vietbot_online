#!/bin/bash
#!/usr/bin/sudo /usr/bin/python3.7
#!/home/pi/.local/lib/python3.7/site-packages
export XDG_RUNTIME_DIR="/home/pi"
STRING="Automatic launching vietbot..."
PYTHON="/usr/bin/python3.7"
BOT_ROOT="/home/pi/vietbot/src"
BOT="start.py"

# pushd . > /dev/null 2>&1
cd $BOT_ROOT

echo $STRING
$PYTHON -m "$BOT"

# popd > /dev/null 2>&1