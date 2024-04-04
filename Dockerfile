# Base image
FROM python:3.9-slim as application-stage

# Set working directory
WORKDIR /app

# Install OpenSSL and any other dependencies
RUN apt-get update && apt-get install -y openssl

# Copy the requirements.txt
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Collect static files
RUN python manage.py collectstatic --no-input --clear

# Expose the port the app runs on
EXPOSE 8000

# Define the command to run the application using Gunicorn
CMD ["gunicorn", "oc_lettings_site.wsgi:application", "--bind", "0.0.0.0:8000"]
