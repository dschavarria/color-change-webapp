FROM alpine

RUN apk add py3-flask

EXPOSE 8080/tcp

COPY source-code /opt/source-code

ENTRYPOINT ["python3","/opt/source-code/app.py"]