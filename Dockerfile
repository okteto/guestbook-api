FROM python:3.12-slim

# Create non-root user for security
RUN groupadd --gid 1001 appuser && \
    useradd --uid 1001 --gid 1001 --create-home --shell /bin/bash appuser

WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .

# Install dependencies with pip upgrade and security measures
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY main.py .
COPY app/ ./app/

# Change ownership to non-root user
RUN chown -R appuser:appuser /app

# Switch to non-root user
USER appuser

EXPOSE 8080

# Use exec form and specify uvicorn directly for better process handling
CMD ["uvicorn", "app.api:router", "--host", "0.0.0.0", "--port", "8080"]