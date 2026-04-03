from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .api.webhooks import webhooks_router

app = FastAPI(
    title="trampoBot API",
    description="Monitorador inteligente de vagas",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(webhooks_router)


@app.get("/health")
async def health():
    return {"status": "ok", "service": "trampoBot API"}