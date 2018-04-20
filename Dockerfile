FROM python:3.6
ENV PYTHONBUFFERED 1
RUN mkdir /code
WORKDIR /code

ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
