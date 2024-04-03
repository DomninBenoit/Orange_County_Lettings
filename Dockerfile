# Étape 1: Construire l'image de l'application Django avec Gunicorn
FROM python:3.9-slim as application-stage

WORKDIR /app

# Install OpenSSL pour la commande suivante et autres dépendances
RUN apt-get update && apt-get install -y openssl

# Copie le fichier requirements.txt dans le conteneur
COPY requirements.txt .

# Generate Django secret key (Vous pouvez aussi le passer comme variable d'environnement au runtime)
ENV SECRET_KEY="$(openssl rand -base64 64)"

# Install les dépendances du projet
RUN pip install --no-cache-dir -r requirements.txt

# Copie le reste du code source de l'application dans le conteneur
COPY . .

# Collecte les fichiers statiques (CSS, JavaScript, images)
RUN python manage.py collectstatic --no-input --clear

# Copie le script entrypoint personnalisé
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Définie la variable d'environnement pour les fichiers statiques
ENV DJANGO_SETTINGS_MODULE=oc_lettings_site.settings

# Définir le script d'entrée comme point d'entrée
ENTRYPOINT ["/entrypoint.sh"]

# Étape 2: Construire l'image NGINX
FROM nginx:alpine as nginx-stage

# Copy static files from application stage to NGINX
COPY --from=application-stage /app/static /static

# Copy NGINX configuration
COPY config/nginx/nginx.conf /etc/nginx/nginx.conf

# Expose port for HTTP
EXPOSE 80

# Start NGINX
CMD ["nginx", "-g", "daemon off;"]
