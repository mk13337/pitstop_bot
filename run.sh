#!/bin/bash

N=15 # Time update in minutes
BASE_PATH="/your/path"

CRON_JOB="*/$N 8-23 * * * cd $BASE_PATH && python3 parsi4.py && sleep 5 && python3 updati4.py"

EXISTS=$(crontab -l | grep -F "$CRON_JOB")

if [[ -z "$EXISTS" ]]; then
  (crontab -l ; echo "$CRON_JOB") | crontab -
  echo "Task added to crontab"
fi

python3 "$PARSER_PATH"

echo "Starting bot..."
cd "$BASE_PATH"
python3 boti4.py
