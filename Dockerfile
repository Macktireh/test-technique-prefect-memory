FROM python:3.9 as python

# On s'assure que la sortie stardard de python n'utilise pas de tampon et
# s'affiche directement.
ENV PYTHONUNBUFFERED 1
# On désire pas que python crée des fichiers *.pyc
ENV PYTHONDONTWRITEBYTECODE 1

# Définition du répertoire de travail
WORKDIR /app

# Installation des dépendances générales à l'aide d'apt
RUN apt update && apt install --no-install-recommends -y \
    # dependencies for building Python packages
    build-essential \
    # On peut faire le ménage dans les fichiers non utilisés pour alléger notre image
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/*

# Installation des dépendances python
ADD . /app
RUN pip install -r requirements.txt

# Exposer le port
EXPOSE 5000

# commende
CMD [ "python", "app.py" ]

