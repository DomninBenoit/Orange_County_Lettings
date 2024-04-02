# Utiliser une image de base Python officielle
FROM python:3.9-slim

# Définie le répertoire de travail dans le conteneur
WORKDIR /app

# Copie le fichier requirements.txt dans le conteneur
COPY requirements.txt .

ENV SECRET_KEY="$(openssl rand -base64 64)"

# Install les dépendances du projet
RUN pip install --no-cache-dir -r requirements.txt

# Copie le reste du code source de l'application dans le conteneur
COPY . .

# Collecte les fichiers statiques (CSS, JavaScript, images)
RUN python manage.py collectstatic --no-input --clear

# Expose le port sur lequel l'application va s'exécuter
EXPOSE 8000

# Définie la variable d'environnement pour les fichiers statiques
ENV DJANGO_SETTINGS_MODULE=oc_lettings_site.settings

# Commande pour lancer l'application
CMD ["gunicorn", "oc_lettings_site.wsgi:application", "--bind", "0.0.0.0:8000"]
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
#CMD ["sleep", "infinity"]