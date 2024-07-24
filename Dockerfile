FROM python:3.10-slim

# Establecer variables de entorno
ENV PYTHONUNBUFFERED=1

# Actualizar el repositorio de paquetes e instalar dependencias del sistema
RUN apt-get update && \
    apt-get install -y \
        gettext \
        brltty \
        build-essential \
        gcc \
        libpq-dev \
        libmariadb-dev \
        libsystemd-dev \
        libffi-dev \
        libssl-dev \
        libpython3-dev \
        libcairo2-dev \
        librsync-dev \
        python3-dev \
        python3-pip \
        dbus \
        cups \
        liblouis-bin \
        pkg-config && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Establecer el directorio de trabajo
WORKDIR /home/django_app

# Copiar el archivo requirements.txt
COPY requirements.txt /home/django_app/requirements.txt

# Actualizar pip a la última versión
RUN pip install --upgrade pip

# Instalar las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de la aplicación
COPY . /home/django_app/

# Exponer el puerto en el que correrá la aplicación
EXPOSE 8000

# Comando por defecto para ejecutar el proyecto
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
