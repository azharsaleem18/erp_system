# Use an official Python image as base
FROM python:3.12 AS builder

# Set the working directory
WORKDIR /app

# Install required system dependencies including PostgreSQL client and Redis CLI
RUN apt-get update && apt-get install -y \
    software-properties-common \
    build-essential \
    libpq-dev \
    postgis \
    postgresql-client \
    gdal-bin \
    libgeos-dev \
    libproj-dev \
    libsqlite3-dev \
    redis-tools \ 
    && rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# --------- Final Runtime Stage ---------
FROM python:3.12-slim AS runtime

# Set working directory
WORKDIR /app

# Install required system dependencies including PostgreSQL client and Redis CLI
RUN apt-get update && apt-get install -y \
    postgresql-client \
    gdal-bin \
    libgeos-dev \
    libproj-dev \
    libsqlite3-dev \
    redis-tools \  
    && rm -rf /var/lib/apt/lists/*

# Copy installed dependencies from builder stage
COPY --from=builder /usr/local/lib/python3.12 /usr/local/lib/python3.12
COPY --from=builder /usr/local/bin /usr/local/bin

# Copy project files into the container
COPY . .

# Ensure STATIC_ROOT directory exists
RUN mkdir -p /app/staticfiles

# Expose port 8000
EXPOSE 8000

# Collect static files before running the app
RUN python manage.py collectstatic --noinput

# Run Django server
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "core.asgi:application", "-k", "uvicorn.workers.UvicornWorker"]
