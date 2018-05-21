#!/bin/sh
date >> /data/orangePI.log.txt

d="ttyACM0"

sleep 15
while [ 1==1 ]
do
  s="$(ls /dev/ | grep $d)"
  #echo "$s"
  #echo "$d"
  if [ "$s" != "$d" ]
    then 
      echo "[ERR]Read USB"
  else
      echo  "[OK] Read USB"
      /usr/bin/python /data/graduate-project/server.py &
      break
  fi
done


