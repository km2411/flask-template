FROM python:3.7-alpine

# Install pip
RUN python -m pip install --upgrade pip

# Create app directory
WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

# Bundle app source
COPY . /app

EXPOSE 8080

CMD ["python", "run.py"]