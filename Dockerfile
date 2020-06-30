FROM python:3.7-alpine as builder
WORKDIR /app
COPY . requirements.txt /app/
RUN pip install -r requirements.txt

FROM builder
WORKDIR /app
COPY . /app
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"] 