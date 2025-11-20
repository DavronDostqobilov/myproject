FROM python:3.11-slim

WORKDIR /app

# Kerakli kutubxonalar
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn

# Kodni ko'chirish
COPY . .

# Statik fayllarni yig'ish
RUN python manage.py collectstatic --noinput

# SQLite faylga yozish huquqini berish (Muhim!)
RUN chown -R www-data:www-data /app
RUN chmod 755 /app
RUN chmod 664 /app/db.sqlite3 2>/dev/null || true

# Ishga tushirish
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "myproject.wsgi:application"]