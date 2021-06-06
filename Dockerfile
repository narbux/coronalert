FROM python:3.8-alpine

ENV PYTHONUNBUFFERED 1

WORKDIR /ctj

COPY . .

RUN pip3 --disable-pip-version-check --no-cache-dir install -r /ctj/requirements.txt

CMD ["python", "/ctj/main.py"]
