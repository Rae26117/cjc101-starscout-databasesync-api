from fastapi import FastAPI
from sync_products import router as product_router

app = FastAPI(
    title="CJC101-StarScout: Product Sync to Dify",
    description="API to sync product data from RDS MySQL and upload as Markdown to Dify knowledge base",
    version="1.0.0"
)

# 掛載產品同步 API
app.include_router(product_router, prefix="/products", tags=["Product Sync"])

@app.get("/")
async def root():
    return {"message": "Welcome to cjc101-starscout Product Sync API"}
