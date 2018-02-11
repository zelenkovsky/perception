FROM python

MAINTAINER Dmitry Zelenkovsky <Dmitry.Zelenkovsky@gmail.com>

RUN pip install numpy \
                pillow \
                matplotlib

WORKDIR /opt/perception

CMD [ "python", "detect.py" ]