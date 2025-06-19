#!/bin/sh
echo "[$(date)] Cron triggered" >> /var/log/cron.log
python /app/main.py >> /var/log/cron.log 2>&1