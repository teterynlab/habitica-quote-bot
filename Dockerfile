FROM python:3.11-slim

WORKDIR /app
COPY . .

RUN apt-get update && apt-get install -y cron tzdata && \
    pip install requests && \
    chmod +x /app/run.sh && \
    echo "0 7 * * * root /app/run.sh >> /var/log/cron.log 2>&1" > /etc/cron.d/habitica-cron && \
    chmod 0644 /etc/cron.d/habitica-cron && \
    touch /var/log/cron.log

CMD ["sh", "-c", "cron && tail -f /var/log/cron.log"]