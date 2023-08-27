FROM python:3.8

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
COPY ./app.py /app/app.py

WORKDIR /app
CMD ["python", "app.py"]
