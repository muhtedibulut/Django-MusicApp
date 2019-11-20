FROM python:3
ENV PYTHONBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD music_app /code/
RUN pip install -r requirements.txt
ADD . /code