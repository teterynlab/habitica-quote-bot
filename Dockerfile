FROM python:3.11-slim

WORKDIR /app
COPY . .

RUN pip install --no-cache-dir -r requirements.txt && \
    apt-get update && apt-get install -y cron && \
    echo "0 7 * * * root python /app/main.py cron >> /var/log/cron.log 2>&1" > /etc/cron.d/habitica-cron && \
    chmod 0644 /etc/cron.d/habitica-cron && \
    touch /var/log/cron.log

CMD ["bash", "-c", "cron && python /app/main.py"]