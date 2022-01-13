FROM python:3.7-slim

ARG USRNAME
ARG PSWRD 

ENV BASIC_AUTH_USERNAME=$USRNAME
ENV BASIC_AUTH_PASSWORD=$PSWRD

COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip3 install -r requirements.txt
COPY ./src /app/src
COPY ./models /app/models

ENTRYPOINT [ "python3" ]
CMD [ "src/app/api.py" ]