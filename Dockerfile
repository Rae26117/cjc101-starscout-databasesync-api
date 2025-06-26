FROM python:3.11-slim

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    rm -rf ~/.cache && \
    find . -type d -name "__pycache__" -exec rm -r {} + && \
    find . -type f -name "*.pyc" -delete

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
