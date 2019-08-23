#!/bin/bash

# turn on bash's job control
#set -m

# Start the primary process and put it in the background
gunicorn run:app -c ./gunicorn.conf.py >>/tmp/flask.log 2>&1 &


while sleep 30; do
  ps aux |grep gunicorn |grep -v grep >/dev/null 2>&1
  PROCESS_1_STATUS=$?
  # If the greps above find anything, they exit with 0 status
  # If they are not both 0, then something is wrong
  if [ $PROCESS_1_STATUS -ne 0 ]; then
    echo "One of the processes has already exited."
    exit 1
  fi
  tail -n 50 new.log
done