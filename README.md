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
