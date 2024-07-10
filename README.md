# Quick Django Docker Setup
### Command Line Tool for Django Developers with deadlines
### Windows only (for now)
## Installation

```
pip install quick-django-docker-setup
```

## Usage

**Just Type:**
```
quick-django-docker-setup
```
**And answer prompts questions about what to install.**

### Choices:
- 📚 **Poetry or requirements.txt**
- 🗃️ **PostgreSQL or SQLite**
- 🥬 **Use Dockerized Celery with Redis or no**
- 🔑 **Use JWT Authentication or no**
- 🖊️ **Use Registration or no**
- 📋️ **Use Swagger as API Docs or no**
- 📁 **Rename outer folder to "backend" or no**
- 📁 **Project name**


## How it works

**The program is written in python and uses a mix of system commands and file editting**

It doesn't use any external libraries, however it installs django and poetry if user doesn't have them installed.
However it uninstalls them as soon as it stops using the commands.

## Contribute

**You are free to contribute to the project**

**https://github.com/KrzysztofCzapla/quick-django-docker-setup**