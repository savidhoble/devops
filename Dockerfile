# Use a lightweight Python image
FROM python:3.10-slim

# Set working directory in container
WORKDIR /app

# Copy dependency file and install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of the app
COPY . .

# Run the Flask app
CMD ["python", "app.py"]
