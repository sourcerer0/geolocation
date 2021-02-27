FROM python:latest

CMD python3
WORKDIR /root

COPY geo /root
RUN python3 -m setup install
