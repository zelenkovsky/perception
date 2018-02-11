FROM python

MAINTAINER Dmitry Zelenkovsky <Dmitry.Zelenkovsky@gmail.com>

RUN pip install matplotlib

WORKDIR /opt/perception

CMD [ "python", "detect.py" ]