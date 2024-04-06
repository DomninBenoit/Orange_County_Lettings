# Base image
FROM python:3.9-slim as application-stage

# Set working directory
WORKDIR /app

# Install OpenSSL and any other dependencies
RUN apt-get update && apt-get install -y openssl nginx

# Copy the requirements.txt
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Collect static files
RUN python manage.py collectstatic --no-input --clear

# Copy static files from application stage to NGINX
COPY static /static

# Copy NGINX configuration
COPY config/nginx/nginx.conf /etc/nginx/sites-enabled/default

RUN nginx -g "daemon on;"

# Copy entrypoint script and give execution permissions
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Start with the entrypoint script
ENTRYPOINT ["/entrypoint.sh"]
