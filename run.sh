#!/bin/bash

N=15 # Время обновления данных в минутах
BASE_PATH="/your/path" # базовый путь до директории с проектом

BOT_PATH="$BASE_PATH/boti4.py"
PARSER_PATH="$BASE_PATH/parsi4.py"
UPDATER_PATH="$BASE_PATH/updati4.py"

# Обновленный CRON_JOB для запуска каждые 15 минут с 8 утра до 12 часов ночи
CRON_JOB="*/$N 8-23 * * * cd $BASE_PATH && python3 $PARSER_PATH && sleep 5 && python3 $UPDATER_PATH"

# Проверяем, существует ли уже задача в crontab
EXISTS=$(crontab -l | grep -F "$CRON_JOB")

if [[ -z "$EXISTS" ]]; then
  # Добавляем задачу в crontab, если её ещё нет
  (crontab -l ; echo "$CRON_JOB") | crontab -
  echo "Task added to crontab"
fi

# Запуск парсера
python3 "$PARSER_PATH"

# Запуск бота
echo "Starting bot..."
python3 "$BOT_PATH"
