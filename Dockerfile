# 使用精簡 Python 映像
FROM python:3.12-slim-bookworm

# 避免產生 __pycache__ 等中間檔
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# 建立工作目錄
WORKDIR /app

# 複製需求檔並安裝必要套件
COPY requirements.txt .

RUN apt-get update && \
    apt-get install -y gcc libffi-dev build-essential && \
    pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    apt-get remove -y gcc libffi-dev build-essential && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* ~/.cache

# 複製專案程式碼
COPY . .

# 開放 port
EXPOSE 8000

# 啟動 FastAPI 服務
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
