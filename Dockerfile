FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright browsers
RUN apt-get update && apt-get install -y wget gnupg curl && \
    playwright install --with-deps

# Copy source code
COPY login.py ./app
COPY .env .

# Run script
CMD ["python", "login.py"]
