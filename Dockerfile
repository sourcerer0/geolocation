FROM python:latest

CMD python3
WORKDIR /root

COPY . /root
RUN python3 -m setup install
