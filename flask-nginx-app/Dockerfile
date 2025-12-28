# -------- Base Image --------
FROM python:3.12-slim

# -------- Set Environment --------
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# -------- Install System Dependencies --------
RUN apt-get update && apt-get install -y \
    build-essential \
    default-libmysqlclient-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# -------- Create App Directory --------
WORKDIR /app

# -------- Install Python Dependencies --------
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# -------- Copy Application Code --------
COPY app.py .
COPY templates ./templates
COPY static ./static

# -------- Expose Port --------
EXPOSE 8000

# -------- Run with Gunicorn --------
CMD ["gunicorn", "--workers", "3", "--bind", "0.0.0.0:8000", "app:app"]

