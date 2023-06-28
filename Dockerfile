# Use the official Python base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code to the working directory
COPY . .

# Expose the port that the Flask application will listen on
EXPOSE $PORT

# Start the Flask application
CMD gunicorn app:app --bind 0.0.0.0:$PORT
