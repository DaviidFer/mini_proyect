# Usa una imagen base de Python
FROM python:3.10-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos necesarios al contenedor
COPY ./app.py /app/app.py
COPY ./requirements.txt /app/requirements.txt

# Instala las dependencias
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Expone el puerto 8000
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]