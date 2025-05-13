FROM python:latest

WORKDIR /src

COPY requirements.txt /src/

RUN pip install -u pip
RUN install -r requirements.txt

COPY . /src/

CMD ["gunicorn", "A.wsgi", ":8000"]

