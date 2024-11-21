FROM python:3.13.0-alpine3.20
LABEL maintainer="Benedict Hazel <bwhazel@gmail.com>"

ENV QUBIT_STATE_0="1.0"
ENV QUBIT_STATE_1="0.0"
ENV GATE="I"
ENV OUTPUT="github"

RUN pip install numpy

COPY action/*.py /action/

ENTRYPOINT python /action/main.py --qubit-state-0=${QUBIT_STATE_0} --qubit-state-1=${QUBIT_STATE_1} --gate=${GATE} --output=${OUTPUT}