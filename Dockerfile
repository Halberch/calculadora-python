# Usamos una imagen base oficial de Python ligera (slim)
# El README indica Python 3.9+
FROM python:3.9-slim

# Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos primero el archivo de dependencias para aprovechar la caché de Docker
COPY requirements.txt .

# Instalamos las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el resto del código de la aplicación
COPY . .

# Exponemos el puerto 5000 (el que usa Flask por defecto en tu app.py)
EXPOSE 5000

# Comando para iniciar la aplicación
CMD ["python", "app.py"]