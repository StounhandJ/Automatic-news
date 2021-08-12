FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY supervisor /etc/supervisor/conf.d/
RUN apt-get update && apt-get install -y supervisor

COPY . .

CMD ["/usr/bin/supervisord"]