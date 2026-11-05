from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os

app = FastAPI(title="RevOps AI - Churn Predictor")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
dados_predicao = [
    {"id": "7741", "plano": "Diamante", "risco": 0.92, "fator_critico": "Ausência nos últimos 4 jogos"},
    {"id": "8820", "plano": "Ouro", "risco": 0.65, "fator_critico": "Queda no consumo da loja oficial"},
    {"id": "9933", "plano": "Prata", "risco": 0.12, "fator_critico": "Alta assiduidade (Sócio Engajado)"},
    {"id": "1024", "plano": "Bronze", "risco": 0.81, "fator_critico": "Inadimplência recente (15 dias)"},
    {"id": "2055", "plano": "Ouro", "risco": 0.45, "fator_critico": "Fim de contrato próximo"},
    {"id": "3190", "plano": "Diamante", "risco": 0.15, "fator_critico": "Upgrade recente de plano"},
    {"id": "4421", "plano": "Bronze", "risco": 0.88, "fator_critico": "Cartão de crédito recusado"},
    {"id": "5532", "plano": "Prata", "risco": 0.55, "fator_critico": "Redução na compra de ingressos extras"},
    {"id": "6698", "plano": "Diamante", "risco": 0.05, "fator_critico": "Presença em 100% dos jogos em casa"},
    {"id": "7712", "plano": "Bronze", "risco": 0.72, "fator_critico": "Nenhum acesso ao app há 60 dias"},
    {"id": "8899", "plano": "Ouro", "risco": 0.38, "fator_critico": "Mudança de endereço (outra cidade)"},
    {"id": "9001", "plano": "Prata", "risco": 0.79, "fator_critico": "Reclamação aberta no SAC pendente"}
]

@app.get("/")
async def carregar_dashboard():
    return FileResponse(os.path.join("templates", "index.html"))

@app.get("/api/churn")
async def obter_dados_churn():
    return {"status": "sucesso", "dados": dados_predicao}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)