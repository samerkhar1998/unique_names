# Use an official lightweight Python image.
FROM python:3.9-slim

# Set the working directory to /app inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./src /app/src
COPY ./data /app/data
COPY ./requirements.txt /app/requirements.txt

# Run src/main.py when the container launches
CMD ["python", "src/main.py"]
