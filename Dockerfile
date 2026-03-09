FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
# Remove -e . / . entries (they fail when app code isn't copied yet)
RUN grep -v -E '^(\s*-e\s+\.|\s*\.\s*)$' requirements.txt > requirements.clean.txt && mv requirements.clean.txt requirements.txt
RUN apt-get update && \
    apt-get install -y --no-install-recommends awscli && \
    pip install --no-cache-dir -r requirements.txt && \
    rm -rf /var/lib/apt/lists/*

COPY . .

CMD ["python", "app.py"]
