# Guide de lancement du serveur Django - Ynov Air

Ce guide vous explique comment configurer et lancer votre serveur Django pour le projet Ynov Air.

## Prérequis

- Python 3.x installé sur votre machine
- Le code source du projet
- Un fichier `requirements.txt` présent dans le projet

## Étapes d'installation et de lancement

### 1. Créer l'environnement virtuel

Ouvrez votre terminal dans le dossier du projet et exécutez :

```bash
python -m venv ynov_air
```

Cette commande crée un environnement virtuel isolé nommé `ynov_air` pour votre projet.

### 2. Activer l'environnement virtuel

**Sur Windows :**
```bash
ynov_air\Scripts\activate
```

**Sur macOS/Linux :**
```bash
source ynov_air/bin/activate
```

Vous devriez voir `(ynov_air)` apparaître au début de votre ligne de commande, indiquant que l'environnement est actif.

### 3. Installer les dépendances

Avec l'environnement virtuel activé, installez tous les packages nécessaires :

```bash
pip install -r requirements.txt
```

Cette commande installe Django et toutes les autres bibliothèques listées dans le fichier `requirements.txt`.

### 4. Créer les migrations de base de données

Générez les fichiers de migration pour votre base de données :

```bash
python manage.py makemigrations
```

Cette commande détecte les changements dans vos modèles et crée les fichiers de migration correspondants.

### 5. Appliquer les migrations

Appliquez les migrations à votre base de données :

```bash
python manage.py migrate
```

Cette commande crée les tables dans votre base de données selon vos modèles Django.

### 6. Lancer le serveur de développement

Démarrez le serveur Django :

```bash
python manage.py runserver
```

Le serveur démarre par défaut sur `http://127.0.0.1:8000/`

## Accéder à votre application

Une fois le serveur lancé, ouvrez votre navigateur et accédez à :

```
http://127.0.0.1:8000/
```

ou

```
http://localhost:8000/
```

## Arrêter le serveur

Pour arrêter le serveur, appuyez sur `Ctrl + C` dans votre terminal.

## Désactiver l'environnement virtuel

Lorsque vous avez terminé, vous pouvez désactiver l'environnement virtuel :

```bash
deactivate
```

## Commandes utiles supplémentaires

### Créer un super utilisateur (admin)
```bash
python manage.py createsuperuser
```

### Accéder à l'interface d'administration
```
http://127.0.0.1:8000/admin/
```

### Lancer le serveur sur un port différent
```bash
python manage.py runserver 8080
```

### Lancer le serveur accessible depuis d'autres machines
```bash
python manage.py runserver 0.0.0.0:8000
```

## Résolution de problèmes

### L'environnement virtuel ne s'active pas
- Vérifiez que Python est bien installé
- Sur Windows, essayez d'exécuter PowerShell en tant qu'administrateur

### Erreurs lors de l'installation des dépendances
- Assurez-vous que pip est à jour : `python -m pip install --upgrade pip`
- Vérifiez votre connexion internet

### Le port 8000 est déjà utilisé
- Utilisez un autre port : `python manage.py runserver 8080`
- Ou arrêtez l'application qui utilise le port 8000

## Notes importantes

- Toujours activer l'environnement virtuel avant de travailler sur le projet
- Ne commitez jamais le dossier `ynov_air/` dans votre système de contrôle de version
- Le serveur de développement Django ne doit pas être utilisé en production
