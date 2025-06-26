# 🧠 FastAPI Dify Product Sync

這是一個使用 FastAPI 建立的 API，能夠從 AWS RDS MySQL 匯出商品資料，轉換成 Markdown 檔案，並上傳到 Dify 知識庫中進行 AI 文件強化與問答。

---

## 📁 專案結構

```
.
├── main.py               # FastAPI 主程式
├── .env                  # 環境變數（請勿上傳）
├── requirements.txt      # Python 套件需求
├── Dockerfile            # 容器化部署檔案
├── venv/                 # Python 虛擬環境
```

---

## ⚙️ 安裝步驟

### 1. 建立虛擬環境並安裝依賴

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. 設定 `.env` 檔

建立 `.env` 檔，內容如下：

```env
DB_HOST=your-rds-host.amazonaws.com
DB_USER=admin
DB_PASSWORD=your-password
DB_NAME=productdb

DIFY_BASE_URL=http://54.89.233.223
DIFY_API_KEY=your-dify-api-key
DIFY_DATASET_ID=b9fe13cb-db53-43a7-b8db-9a35c600b831
```

---

## 🚀 啟動方式

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

---

## 📦 Docker 部署（可部署至 AWS App Runner）

```bash
docker build -t fastapi-dify .
docker run -p 8000:8000 --env-file .env fastapi-dify
```

---

## 🧪 測試 API

使用瀏覽器或 Postman 存取以下端點：

- 匯出與上傳：
  ```
  GET http://localhost:8000/sync-products-to-dify
  ```

---

## 📚 關於

- 作者：你可以補上自己的名字
- 建置時間：2025-06-26
- 技術：FastAPI + Python + MySQL + Dify + Markdown + App Runner

---
