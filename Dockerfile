FROM python:3.10-slim-buster
WORKDIR /app
COPY . /app

RUN apt-get update -y && apt install awscli -y

RUN apt-get update && pip install -r requirments.txt
CMD ["python3","app.py"]