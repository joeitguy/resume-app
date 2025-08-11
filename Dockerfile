# Use a lightweight Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Optional: expose port (Heroku sets $PORT dynamically)
EXPOSE 8000

# Start the Flask app using Gunicorn
CMD gunicorn app:app --bind 0.0.0.0:$PORT
