FROM python:3.9

EXPOSE 5000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app

#Add Flask app to working directory
ADD . /app

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]