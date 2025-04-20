# 1. Use the official Python 3.10 slim image as the base
FROM python:3.10-slim-buster

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy everything from the current host directory to /app in the container
COPY . /app

# 4. Update package lists and install AWS CLI
RUN apt-get update -y && apt-get install -y awscli

# 5. Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 6. Define the default command to run your app
CMD ["python3", "app.py"]