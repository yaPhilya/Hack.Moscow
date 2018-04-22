FROM python:3.6

ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

ADD . .

CMD gunicorn --bind 0.0.0.0:5123 server.production:app --log-file -