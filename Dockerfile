# Utiliza una imagen base de Python 3.12
FROM python:3.12

# Actualiza pip
RUN pip install --upgrade pip

# Copia los archivos de requisitos primero para aprovechar la caché de Docker
COPY requirements.txt .