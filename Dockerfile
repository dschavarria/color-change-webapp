FROM alpine

RUN apk add py3-flask

COPY source-code /opt/source-code

ENTRYPOINT ["python3","/opt/source-code/app.py"]