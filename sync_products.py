from fastapi import APIRouter
from fastapi.responses import JSONResponse
import mysql.connector
import requests
import os
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()

# 環境變數設定
SOURCE_DB = {
    'host': os.getenv("DB_HOST"),
    'user': os.getenv("DB_USER"),
    'password': os.getenv("DB_PASSWORD"),
    'database': os.getenv("DB_NAME")
}

DIFY_BASE_URL = os.getenv("DIFY_BASE_URL")
DIFY_API_KEY = os.getenv("DIFY_API_KEY")
DIFY_DATASET_ID = os.getenv("DIFY_DATASET_ID")

HEADERS = {
    "Authorization": f"Bearer {DIFY_API_KEY}"
}

@router.get("/sync-to-dify")
def sync_products():
    try:
        # 連接資料庫
        conn = mysql.connector.connect(**SOURCE_DB)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM products")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()

        if not rows:
            return JSONResponse(content={"message": "⚠️ 資料表為空"}, status_code=200)

        # 轉為 Markdown
        md_lines = ["# 產品清單\n"]
        for row in rows:
            md_lines.append(f"## {row['name']}")
            md_lines.append(f"- **ID**: {row['id']}")
            md_lines.append(f"- **品牌**: {row.get('brand', 'N/A')}")
            md_lines.append(f"- **類型**: {row.get('type', 'N/A')}")
            md_lines.append(f"- **顏色**: {row.get('color', 'N/A')}")
            md_lines.append(f"- **價格**: {row.get('price', 'N/A')}")
            md_lines.append(f"- **描述**: {row.get('description', '')}")
            md_lines.append("")

        with open("products.md", "w", encoding="utf-8") as f:
            f.write("\n".join(md_lines))

        # 上傳 Markdown 檔案至 Dify 知識庫
        upload_url = f"{DIFY_BASE_URL}/v1/datasets/{DIFY_DATASET_ID}/document/create-by-file"
        with open("products.md", "rb") as f:
            files = {
                "file": ("products.md", f, "text/markdown")
            }
            data = {
                "knowledge_config": {
                    "process_rule": {
                        "mode": "automatic",
                        "segmentation": {
                            "max_tokens": 500
                        }
                    }
                }
            }
            res = requests.post(upload_url, headers=HEADERS, files=files, data={"json": str(data)})

        if res.status_code == 200:
            return {"message": f"✅ 嘗試上傳 {len(rows)} 筆資料"}
        else:
            return {
                "message": f"✅ 嘗試上傳 {len(rows)} 筆資料",
                "response": res.json()
            }

    except Exception as e:
        return {"error": str(e)}
