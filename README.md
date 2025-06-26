# 📦 FastAPI Dify Sync API

A modular FastAPI app to export product data from RDS MySQL and sync it as Markdown documents to [Dify](https://dify.ai) knowledge base.

## 🚀 Features

- ✅ Sync RDS MySQL products to Markdown
- ✅ Upload Markdown to Dify Knowledge Base
- ✅ Organized router structure with `.env` configuration

## 🧱 Project Structure

```
cjc101-starscout-databasesync-api/
├── main.py                # FastAPI app entry point
├── sync_products.py       # Sync logic and API route
├── .env.sample            # Example env file
├── .gitignore
├── .dockerignore
├── products.md            # Generated markdown file (ignored)
```

## ⚙️ Setup

### 1. Clone this repo

```bash
git clone https://github.com/YOUR_USERNAME/fastapi-dify-sync.git
cd fastapi-dify-sync
```

### 2. Create `.env`

```bash
cp .env.sample .env
```

Edit `.env` with your RDS and Dify credentials.

### 3. Install dependencies

```bash
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### 4. Run FastAPI

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

Then open your browser: [http://localhost:8000/docs](http://localhost:8000/docs)

## 🐳 Docker (Optional)

```bash
docker build -t fastapi-dify .
docker run -p 8000:8000 fastapi-dify
```

## 🔐 Environment Variables

Please refer to `.env.sample` for all required settings.

## 📤 API Endpoints

- `GET /products/sync-to-dify` — Export products and upload to Dify

## 📄 License

MIT © CJC101-StarScout


---

## 🚀 Deploy to AWS App Runner

### 1. 準備 GitHub Repo
- 確保已上傳 `Dockerfile`、`.env.sample` 等必要檔案
- `.env` 請勿上傳！改在 App Runner 設定中手動填入環境變數

### 2. 登入 AWS Console → App Runner
- 選擇「Source code repository」
- 選 GitHub 並授權你的帳號
- 選擇此專案 Repo 與分支

### 3. 設定 Build & Runtime
- Runtime: Dockerfile
- Port: `8000`

### 4. 設定環境變數
將 `.env.sample` 內容轉成實際變數填入，如：

```
DB_HOST=...
DB_USER=...
DB_PASSWORD=...
DB_NAME=...
DIFY_BASE_URL=...
DIFY_API_KEY=...
DIFY_DATASET_ID=...
```

### 5. 點擊「Deploy service」即可！

---

完成後，你就能透過 App Runner 部署好的網址直接使用 API！

例如：
`https://your-app-id.awsapprunner.com/products/sync-to-dify`



---

## 🐳 Dockerfile 建立方式

請在專案根目錄新增 `Dockerfile`：

```Dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## 🚀 部署到 AWS App Runner

1. 推送你的專案到 GitHub（已完成）
2. 前往 AWS App Runner 控制台
3. 建立服務 → 從原始碼部署
4. 連結 GitHub，選擇此 repo
5. 建置命令請留空
6. 啟動命令請填：

```
uvicorn main:app --host 0.0.0.0 --port 8000
```

7. 儲存環境變數（與 .env 一致）
8. 點選「建立並部署」

部署後你會取得一組網址，即為你專案的 API 網址。

---

## 📎 範例部署網址

```
https://your-service-id.us-east-1.awsapprunner.com/products/sync-to-dify
```

---

## 🙋 常見錯誤排查

- `.env` 沒設定對 → 無法連 RDS
- `.env` 被 commit → 檢查 `.gitignore`
- Dify 回傳 `process_rule` 錯誤 → 請確認 request payload 正確

