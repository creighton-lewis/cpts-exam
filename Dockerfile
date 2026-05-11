# syntax=docker/dockerfile:1
ARG PYTHON_VERSION=3.14.4
FROM python:${PYTHON_VERSION}-slim 

# Keep the output unbuffered and avoid .pyc files
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Create a non‑root user (optional but recommended)
ARG UID=10001
RUN adduser --disabled-password --gecos "" --uid ${UID} appuser

WORKDIR /app

# Install only the Python dependencies (cached)
COPY requirements.txt .
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install --no-cache-dir -r requirements.txt

# Switch to non‑root user
USER appuser

# Copy the rest of the source code
COPY . .

# Default command – replace with your entry point
CMD ["python", "my_script.py"]
