FROM python:3.7-alpine

# Install pip
RUN python -m pip install --upgrade pip

# Create app directory
WORKDIR /app

# Bundle app source
COPY . /app

RUN pip install -r requirements.txt

EXPOSE 9090

CMD ["python", "run.py"]