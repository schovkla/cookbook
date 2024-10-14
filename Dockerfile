# Použijeme oficiální Python image
FROM python:3.11-slim

# Nastavíme pracovní adresář uvnitř kontejneru
WORKDIR /app

# Zkopírujeme požadavky (requirements.txt) do kontejneru
COPY requirements.txt /app/

# Nainstalujeme závislosti
RUN pip install --no-cache-dir -r requirements.txt

# Zkopírujeme zbytek aplikace do kontejneru
COPY . /app/

# Nastavíme proměnnou prostředí pro Django
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Otevřeme port 8000 pro Django
EXPOSE 8000

# Spustíme Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
