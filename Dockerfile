FROM python:3.12.0-slim-bookworm

WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the application code
COPY app .

# Set environment variables with default values
ENV HOST=0.0.0.0
ENV PORT=8080
ENV RELOAD=True

# Expose the port defined by the PORT environment variable
EXPOSE $PORT

# Command to run the application using the defined environment variables
CMD ["python", "main.py"]
