from fastapi import APIRouter, Request, status

webhooks_router = APIRouter(prefix="/api/webhooks/v1")

@webhooks_router.post("/agent", status_code=status.HTTP_200_OK)
async def agent_webhook(request: Request):
    """
    Endpoint que recebe solicitações para o agente.
    """
    body = await request.json()
    print(f"Recebido dados do webhook: {body}")
    
    return {
        "message": "Webhook recebido com sucesso",
    }