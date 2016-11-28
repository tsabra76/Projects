#!/bin/sh
# add ip / hostname separated by white space
HOST="192.168.0.16" # IP address of device to search for
# no ping request
COUNT=1
# Loop to check for device on network
until [ $count -ne 0 ]
do
for myHost in $HOST
do
count=$(ping -c $COUNT $myHost | grep 'received' | awk -F',' '{ print $2 }' | awk '{ print $1 }')
if [ $count != 0 ]; then
# IP FOUND!
python /media/tarek/media/headlines.py
fi
done
done
