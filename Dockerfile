FROM python:3.13.0-alpine3.20
LABEL maintainer="Benedict Hazel <bwhazel@gmail.com>"

RUN pip install numpy

COPY action/*.py /action/

ENTRYPOINT [ "python", "/action/main.py" ]