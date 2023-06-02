FROM python:3.9

WORKDIR /app

COPY . .

RUN pip install flask pony

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

CMD ["flask", "run", "--host=0.0.0.0"]
