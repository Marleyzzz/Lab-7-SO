# Imagine de bază
FROM python:3.9-slim

# Setează directorul de lucru
WORKDIR /app

# Copiază fișierele aplicației
COPY app.py /app/
COPY templates /app/templates/
COPY requirements.txt /app/

# Instalează dependențele
RUN pip install --no-cache-dir -r requirements.txt

# Expune portul pentru Flask
EXPOSE 5000

# Rulează aplicația
CMD ["python", "app.py"]
