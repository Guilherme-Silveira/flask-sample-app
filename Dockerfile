FROM python:3.9

WORKDIR /app

ADD . .

RUN python3 -m pip install -r requirements.txt

ENTRYPOINT ["python3"]

CMD ["app.py"]