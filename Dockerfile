# Usar la imagen base de Python 3.11
FROM python:3.11

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar los archivos de tu proyecto al directorio de trabajo
COPY . .

# Definir la variable de entorno para el entorno virtual
ENV VIRTUAL_ENV=/app/.venv_docker

# Crear un entorno virtual en el contenedor
RUN python -m venv $VIRTUAL_ENV

# Establecer la variable PATH para usar el entorno virtual
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Actualizar pip e instalar las dependencias del proyecto
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Comando por defecto para ejecutar el backend de Reflex
CMD ["reflex", "run", "--env", "prod", "--backend-only"]

