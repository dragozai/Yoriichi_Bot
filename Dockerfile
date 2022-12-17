FROM python:3.10.8-slim-buster

WORKDIR /app

RUN apt-get -y update

RUN apt-get -y install git gcc python3-dev zip

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "Yoriichi"]
