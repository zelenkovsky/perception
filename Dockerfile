FROM python

MAINTAINER Dmitry Zelenkovsky <Dmitry.Zelenkovsky@gmail.com>

RUN pip install numpy \
                pillow \
                matplotlib \
                opencv-python

WORKDIR /opt/perception

CMD [ "python", "detect.py" ]