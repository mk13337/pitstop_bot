#!/bin/bash

N=15 # Время обновления данных в минутах
BASE_PATH="/your/path" # базовый путь до директории с проектом


BOT_PATH="$BASE_PATH/boti4.py"
PARSER_PATH="$BASE_PATH/parsi4.py"
UPDATER_PATH="$BASE_PATH/updati4.py"

CRON_JOB="*/$N * * * * $PARSER_PATH && sleep 10 && $UPDATER_PATH"

EXISTS=$(crontab -l | grep -F "$CRON_JOB")

if [[ -z "$EXISTS" ]]; then
  (crontab -l ; echo "$CRON_JOB") | crontab -
  echo "Task added to crontab"
fi

python3 "$PARSER_PATH"

# Запуск бота
echo "Starting bot..."
python3 "$BOT_PATH"
