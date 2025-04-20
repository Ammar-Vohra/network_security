# 1. Use the official Python 3.10 slim image as the base
FROM python:3.10-slim-buster

# 2. Set the working directory in the container to /app
WORKDIR /app

# 3. Copy everything from your local directory into /app in the container
COPY . /app

# 4. Update apt and install AWS CLI
RUN apt update -y && apt install -y awscli

# 5. Install Python dependencies from requirements.txt
RUN apt-get update && pip -r requirements.txt

# 6. Run app.py when the container starts
CMD ["python3", "app.py"]
