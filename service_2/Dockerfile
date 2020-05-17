FROM python:3.7-alpine

# Create app directory
WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

# Bundle app source
COPY . /app

EXPOSE 9090

CMD ["python", "run.py"]